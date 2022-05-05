"""The main module of build resources program."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from filecmp import cmpfiles
from importlib import resources
from pathlib import Path

from qdarktheme.util import get_qdarktheme_root_path, multi_replace
from tools.build_resources.color import RGBA

DIST_DIR_PATH = get_qdarktheme_root_path() / "themes"


@dataclass(unsafe_hash=True, frozen=True)
class _Url:
    """Class handling the properties of the $url{...} variable in the stylesheet template."""

    icon: str
    color_id: str
    rotate: str
    match_text: str
    file_name: str


def _remove_qss_comment(stylesheet: str) -> str:
    """Remove qss comment from the stylesheet string."""
    stylesheet = re.sub(r" */\*[\s\S]*?\*/", "", stylesheet)
    # Change blank lines to one blank line
    return re.sub(r"\n\s*\n", "\n", stylesheet)


def _parse_url(stylesheet: str) -> set[_Url]:
    """Parse $url{...} symbol in template stylesheet."""
    urls = set()
    for match in re.finditer(r"\$url\{.+\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$url", "")

        url_property: dict[str, str] = json.loads(json_text)
        icon = url_property["icon"]
        color_id = url_property["id"]
        rotate = url_property.get("rotate", "0")

        file_name = f"{icon.replace('.svg', '')}__{color_id}"
        file_name += "" if rotate == "0" else f"__rotate-{rotate}"
        urls.add(_Url(icon, color_id, rotate, match_text, file_name))
    return urls


def _build_init_file(theme: str, output_dir_path: Path) -> None:
    contents = f'"""Package containing the resources for {theme} theme."""\n'
    (output_dir_path / "__init__.py").write_text(contents)


def _build_svg_resources(
    theme: str, urls: set[_Url], colors: dict[str, str], svg_dir_path: Path, output_dir_path: Path
) -> None:
    svg_codes: dict[str, str] = {}  # {file name: svg code}
    output_dir_path.mkdir(exist_ok=True)
    svg_paths = (path for path in svg_dir_path.iterdir() if ".svg" in path.name)
    svg_codes = {path.name: path.read_text(encoding="utf-8") for path in svg_paths}

    def to_svg_color_format(color_hex: str) -> str:
        r, g, b, a = RGBA.from_hex(color_hex)
        if a == 1:
            return f'"{color_hex}"'
        # QSvg does not support #RRGGBBAA. Therefore, we need to set the alpha value to `fill-opacity` instead.
        return f'"rgb({r}, {g}, {b})" fill-opacity="{a}"'

    pattern = re.compile(r'xmlns="[\s\S]*?" ')
    svg_resources: dict[str, str] = {}

    for url in urls:
        color_hex = colors[url.color_id]
        # Change color and rotate. See https://stackoverflow.com/a/15139069/13452582
        new_contents = to_svg_color_format(color_hex)
        new_contents += "" if url.rotate == "0" else f' transform="rotate({url.rotate}, 12, 12)"'
        svg_code_converted = svg_codes[url.icon].replace('"#FFFFFF"', new_contents)
        svg_code_converted = pattern.sub("", svg_code_converted)
        svg_resources[url.file_name] = svg_code_converted.replace('"', '\\"')

    svg_resources_sorted = {file_name: code for file_name, code in sorted(svg_resources.items())}
    json_text = json.dumps(svg_resources_sorted)
    with (output_dir_path / "svg.py").open("w") as f:
        f.write(f'"""Contents that define svg for {theme} theme."""\n\n')
        f.write(f'SVG_RESOURCES = """\n{json_text}\n"""  # noqa: E501\n')


def _build_palette_file(colors: dict[str, str], output_dir_path: Path, palette_template: str) -> None:
    def to_arg_text(color_hex: str) -> str:
        r, g, b, a = RGBA.from_hex(color_hex)
        return f'"{color_hex}"' if a == 1 else f"{r}, {g}, {b}, {a*255}"

    replacements = {f'"${color_id}"': to_arg_text(color_hex) for color_id, color_hex in colors.items()}
    with (output_dir_path / "palette.py").open("w") as f:
        f.write(multi_replace(palette_template, replacements))


def _build_template_stylesheet(
    theme: str, stylesheet: str, urls: set[_Url], colors: dict[str, str], output_dir_path: Path
) -> None:
    def to_sheet_format(color_hex: str) -> str:
        rgba = RGBA.from_hex(color_hex)
        return color_hex if rgba[-1] == 1 else str(rgba)

    url_replacements = {url.match_text: f"url(${{path}}/{theme}/svg/{url.file_name}.svg)" for url in urls}
    colors_converted = {f"${color_id}": to_sheet_format(color_hex) for color_id, color_hex in colors.items()}
    template_stylesheet = multi_replace(stylesheet, {**url_replacements, **colors_converted})
    with (output_dir_path / "stylesheet.py").open("w") as f:
        f.write(f'"""Contents that define stylesheet for {theme} theme."""\n\n')
        f.write(f'STYLE_SHEET = """\n{template_stylesheet}\n"""\n')


def _generate_root_init_file(output_dir_path: Path, themes: list[str], doc_string: str = "", source: str = "") -> None:
    with (output_dir_path / "__init__.py").open("w") as f:
        if len(doc_string) != 0:
            f.write(doc_string + "\n")
        f.write(f"THEMES = {themes}\n".replace("'", '"').replace("[", "(").replace("]", ")"))
        if len(source) != 0:
            f.write(source + "\n")


def build_resources(build_path: Path, theme_file_paths: list[Path], root_init_file_doc: str) -> None:
    """Build resources for qdarktheme module."""
    stylesheet = _remove_qss_comment(resources.read_text("tools.build_resources", "base.qss"))
    urls = _parse_url(stylesheet)
    palette_template = resources.read_text("tools.build_resources", "palette.template.py")
    svg_dir_path = Path(__file__).parent / "svg"
    themes = []

    for theme_file_path in theme_file_paths:
        theme = theme_file_path.stem
        themes.append(theme)
        output_dir_path = build_path / theme
        output_dir_path.mkdir()

        hex_colors: dict[str, str] = json.loads(theme_file_path.read_bytes())

        _build_init_file(theme, output_dir_path)
        _build_svg_resources(theme, urls, hex_colors, svg_dir_path, output_dir_path)
        _build_palette_file(hex_colors, output_dir_path, palette_template)
        _build_template_stylesheet(theme, stylesheet, urls, hex_colors, output_dir_path)

    themes.sort()
    _generate_root_init_file(build_path, themes, root_init_file_doc)


def compare_all_files(dir1: Path, dir2: Path) -> list[str]:
    """Check if the contents of the files with the same name in the two directories are the same.

    Args:
        dir1: The directory containing files.
        dir2: The directory containing files.

    Returns:
        list[str]: A list of file names with different contents.
    """
    target_files = set()
    for file in dir2.glob("**/*"):
        if not file.is_file():
            continue
        target_files.add(str(file).replace(str(dir2), "")[1:])
    _, mismatch, err = cmpfiles(dir1, dir2, target_files)
    return [str(file) for file in mismatch + err]
