from __future__ import annotations

import json
import re
import shutil
import sys
from dataclasses import dataclass
from filecmp import cmpfiles
from importlib import resources
from pathlib import Path
from tempfile import NamedTemporaryFile
from xml.etree import ElementTree as ET  # nosec

from PySide6.scripts.pyside_tool import rcc

from builder.color import RGBA
from qdarktheme.util import get_project_root_path, multireplace

DIST_DIR_PATH = get_project_root_path() / "dist"


@dataclass(unsafe_hash=True, frozen=True)
class _Url:
    """Class handling the properties of the $url{...} variable in the stylesheet template."""

    icon: str
    color_id: str
    rotate: str
    match_text: str
    file_name: str


def _remove_comment(stylesheet: str) -> str:
    comment_pattern = re.compile(r" */\*[\s\S]*?\*/")
    match = comment_pattern.search(stylesheet)
    license_text = "/* MIT License */" if match is None else match.group()
    stylesheet_noncomment = comment_pattern.sub("", stylesheet)

    return license_text + re.sub(r"\n\s*\n", "\n", stylesheet_noncomment)


def _parse_url(stylesheet: str) -> set[_Url]:
    """Parse $url{...} simbol in template stylesheet."""
    urls = set()
    for match in re.finditer(r"\$url\{.+\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$url", "")

        url_property = json.loads(json_text)
        icon = url_property["icon"]
        color_id = url_property["id"]
        rotate = url_property.get("rotate", "0")

        file_name = f"{icon.replace('.svg', '')}__{color_id}__rotate-{rotate}.svg"
        urls.add(_Url(icon, color_id, rotate, match_text, file_name))
    return urls


def _build_svg_file(urls: set[_Url], colors: dict[str, RGBA], svg_dir_path: Path, output_dir_path: Path) -> None:
    svg_codes: dict[str, str] = {}  # {file name: svg code}
    output_dir_path.mkdir(exist_ok=True)
    svg_paths = [path for path in svg_dir_path.iterdir() if ".svg" in path.name]
    svg_codes = {path.name: path.read_text(encoding="utf-8") for path in svg_paths}

    # QSvg does not support #RRGGBBAA. Therefore, we need to set the alpha value to `fill-opacity` instead.
    def to_svg_color_format(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f'fill="rgb({r}, {g}, {b})" fill-opacity="{a}"'

    for url in urls:
        rgba = colors[url.color_id]
        # Change color and rotate. See https://stackoverflow.com/a/15139069/13452582
        new_contents = f'{to_svg_color_format(rgba)} transform="rotate({url.rotate}, 12, 12)"'
        svg_code_converted = svg_codes[url.icon].replace('fill="#FFFFFF"', new_contents)
        with (output_dir_path / url.file_name).open("w") as f:
            f.write(svg_code_converted)


def _build_palette_file(colors: dict[str, RGBA], output_dir_path: Path) -> None:
    def to_arg_text(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f"{r}, {g}, {b}, {a*255}"

    replacements = {f'"${color_id}"': to_arg_text(rgba) for color_id, rgba in colors.items()}
    palette_text = resources.read_text("builder", "palette.txt.py")
    with (output_dir_path / "palette.py").open("w") as f:
        f.write(multireplace(palette_text, replacements))


def _build_template_stylesheet(
    theme: str, stylesheet: str, urls: set[_Url], colors: dict[str, RGBA], output_dir_path: Path
) -> None:
    url_replacements = {url.match_text: f"url(${{path}}/dist/{theme}/svg/{url.file_name})" for url in urls}
    colors_converted = {f"${color_id}": str(rgba) for color_id, rgba in colors.items()}
    template_stylesheet = multireplace(stylesheet, {**url_replacements, **colors_converted})
    with (output_dir_path / "stylesheet.py").open("w") as f:
        f.write(f'STYLE_SHEET = """\n{template_stylesheet}\n"""\n')


def _generate_qt_resource_file(svg_dir_path: Path, output_dir_path: Path, theme: str) -> None:
    main_tag = ET.Element("RCC", {"version": "1.0"})
    qt_resource_tag = ET.SubElement(main_tag, "qresource", {"prefix": f"qdarktheme/dist/{theme}"})

    for file in svg_dir_path.iterdir():
        file_tag = ET.SubElement(qt_resource_tag, "file")
        file_tag.text = f"{svg_dir_path.name}/{file.name}"

    with NamedTemporaryFile(suffix=".qrc", dir=str(output_dir_path)) as f:
        qrc_file_path = output_dir_path / f.name
        ET.ElementTree(main_tag).write(str(qrc_file_path), "utf-8")
        py_resource_file_path = output_dir_path / "rc_icons.py"

        # Patch PySide6.scripts.pyside_tool
        temp_argv, temp_exit = sys.argv.copy(), sys.exit
        sys.argv[1:] = [str(qrc_file_path), "-o", str(py_resource_file_path)]
        # Not finish program with sys.exit()
        sys.exit = lambda _: "dummy"
        rcc()
        # Remove patch
        sys.argv, sys.exit = temp_argv, temp_exit

    py_resource_text_converted = py_resource_file_path.read_text().replace("PySide6", "qdarktheme.qtpy")
    py_resource_file_path.write_text(py_resource_text_converted)


def build_resources(build_path: Path, theme_file_paths: list[Path], stylesheet: str, svg_dir_path: Path) -> None:
    shutil.copy(Path(__file__).parent / "__init__.py", build_path / "__init__.py")
    stylesheet = _remove_comment(stylesheet)
    urls = _parse_url(stylesheet)
    for theme_file_path in theme_file_paths:
        theme = theme_file_path.stem
        output_dir_path = build_path / theme
        output_dir_path.mkdir()
        (output_dir_path / "__init__.py").touch()

        hex_colors = json.loads(theme_file_path.read_bytes())
        rgba_colors = {color_id: RGBA.from_hex(color_hex) for color_id, color_hex in hex_colors.items()}

        # Build contents
        _build_svg_file(urls, rgba_colors, svg_dir_path, output_dir_path / "svg")
        _build_palette_file(rgba_colors, output_dir_path)
        _build_template_stylesheet(theme, stylesheet, urls, rgba_colors, output_dir_path)
        # Generate qt resource file
        _generate_qt_resource_file(output_dir_path / "svg", output_dir_path, theme)


def compare_all_files(dir1: Path, dir2: Path) -> list[str]:
    target_files = set()
    for file in dir2.glob("**/*"):
        if not file.is_file():
            continue
        target_files.add(str(file).replace(str(dir2), "")[1:])
    _, mismatch, err = cmpfiles(dir1, dir2, target_files)
    files_changed = mismatch + err
    if not [file for file in files_changed if "rc_icons.py" not in file]:
        return []
    return [str(Path(dir1).relative_to(Path.cwd()) / file) for file in files_changed]
