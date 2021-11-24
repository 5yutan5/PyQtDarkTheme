# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import json
import pprint
import re
import shutil
import subprocess  # nosec
from dataclasses import dataclass
from filecmp import cmpfiles
from importlib import resources
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from xml.etree import ElementTree as ET  # nosec

import click

from builder.color import RGBA
from qdarktheme.util import get_project_root_path, multireplace

DIST_DIR_PATH = get_project_root_path() / "dist"


@dataclass(unsafe_hash=True, frozen=True)
class Url:
    """A class that handle the properties of the $url{...} variable in the stylesheet template."""

    icon: str
    color_id: str
    rotate: str
    match_text: str
    file_name: str


def remove_comment(stylesheet: str) -> str:
    comment_pattern = re.compile(r" */\*[\s\S]*?\*/")
    match = comment_pattern.search(stylesheet)
    license_text = "/* MIT License */" if match is None else match.group()
    stylesheet_noncomment = comment_pattern.sub("", stylesheet)

    return license_text + re.sub(r"\n\s*\n", "\n", stylesheet_noncomment)


def parse_url(stylesheet: str) -> set[Url]:
    """Parse $url{...} in template stylesheet."""
    urls = set()
    for match in re.finditer(r"\$url\{.+\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$url", "")

        url_property = json.loads(json_text)
        icon = url_property["icon"]
        color_id = url_property["id"]
        rotate = url_property.get("rotate", "0")

        file_name = f"{icon.replace('.svg', '')}__{color_id}__rotate-{rotate}.svg"
        urls.add(Url(icon, color_id, rotate, match_text, file_name))
    return urls


def build_svg_file(urls: set[Url], colors: dict[str, RGBA], output_dir_path: Path) -> None:
    svg_codes: dict[str, str] = {}  # {file name: svg code}
    for content in resources.contents("builder.svg"):
        if ".svg" not in content:  # Only svg file
            continue
        svg_codes[content] = resources.read_text("builder.svg", content)

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


def build_palette_file(colors: dict[str, RGBA], output_dir_path: Path) -> None:
    def to_arg_text(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f"{r}, {g}, {b}, {a*255}"

    replacements = {f'"${color_id}"': to_arg_text(rgba) for color_id, rgba in colors.items()}
    palette_text = resources.read_text("builder", "palette.txt.py")
    with (output_dir_path / "palette.py").open("w") as f:
        f.write(multireplace(palette_text, replacements))


def compare_all_files(output_dir: Path, temp_dir: Path) -> list[str]:
    target_files = set()
    for file in temp_dir.glob("**/*"):
        if not file.is_file():
            continue
        target_files.add(str(file).replace(str(temp_dir), "")[1:])
    _, mismatch, err = cmpfiles(output_dir, temp_dir, target_files)
    files_changed = mismatch + err
    return [str(Path(output_dir).relative_to(Path.cwd()) / file) for file in files_changed]


def generate_qt_resource_file(svg_dir_path: Path, output_dir_path: Path, theme: str) -> None:
    main_tag = ET.Element("RCC", {"version": "1.0"})
    qt_resource_tag = ET.SubElement(main_tag, "qresource", {"prefix": f"qdarktheme/dist/{theme}"})

    for file in svg_dir_path.iterdir():
        file_tag = ET.SubElement(qt_resource_tag, "file")
        file_tag.text = f"{svg_dir_path.name}/{file.name}"

    with NamedTemporaryFile(suffix=".qrc", dir=str(output_dir_path)) as f:
        qrc_file_path = output_dir_path / f.name
        ET.ElementTree(main_tag).write(str(qrc_file_path), "utf-8")

        py_resource_file_path = output_dir_path / "rc_icons.py"
        subprocess.check_call(["pyside6-rcc", qrc_file_path, "-o", py_resource_file_path])  # nosec
    py_resource_text_converted = py_resource_file_path.read_text().replace("PySide6", "qdarktheme.qtpy")
    py_resource_file_path.write_text(py_resource_text_converted)


def build_resources(root_path: Path, theme_file_path: Path, stylesheet: str, urls: set[Url]) -> None:
    theme = theme_file_path.stem
    output_dir_path = root_path / theme
    output_dir_path.mkdir()
    (output_dir_path / "__init__.py").touch()

    hex_colors = json.loads(theme_file_path.read_bytes())
    rgba_colors = {color_id: RGBA.from_hex(color_hex) for color_id, color_hex in hex_colors.items()}

    # Build svg
    svg_dir_path = output_dir_path / "svg"
    svg_dir_path.mkdir()
    build_svg_file(urls, rgba_colors, svg_dir_path)

    # Build palette file
    build_palette_file(rgba_colors, output_dir_path)

    # Build template stylesheet
    url_replacements = {url.match_text: f"url(${{path}}/dist/{theme}/svg/{url.file_name})" for url in urls}
    colors_converted = {f"${color_id}": str(rgba) for color_id, rgba in rgba_colors.items()}
    template_stylesheet = multireplace(stylesheet, {**url_replacements, **colors_converted})
    with (output_dir_path / "stylesheet.py").open("w") as f:
        f.write(f'STYLE_SHEET = """\n{template_stylesheet}\n"""\n')

    # Generate qt resource file
    dist_dir_rc_icons_path = DIST_DIR_PATH / theme / "rc_icons.py"
    if compare_all_files(DIST_DIR_PATH / theme, output_dir_path):
        generate_qt_resource_file(svg_dir_path, output_dir_path, theme)
    elif not dist_dir_rc_icons_path.exists():
        generate_qt_resource_file(svg_dir_path, output_dir_path, theme)
    else:
        shutil.copy(dist_dir_rc_icons_path, output_dir_path / "rc_icons.py")


def main() -> None:
    stylesheet = resources.read_text("builder", "base.qss")
    stylesheet = remove_comment(stylesheet)

    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        shutil.copy(Path(__file__).parent / "__init__.py", temp_dir_path / "__init__.py")

        for path in Path(__file__).parent.glob("theme/*.json"):
            if "validate.json" != path.name:
                build_resources(temp_dir_path, theme_file_path=path, stylesheet=stylesheet, urls=parse_url(stylesheet))
        # Refresh dist dir
        changed_files = compare_all_files(DIST_DIR_PATH, temp_dir_path)
        if changed_files:
            shutil.rmtree(DIST_DIR_PATH, ignore_errors=True)
            shutil.copytree(temp_dir, DIST_DIR_PATH)

    click.secho("Build finished!", fg="green")
    if changed_files:
        click.echo("Changed contents: " + click.style("[", fg="yellow"))
        click.secho(pprint.pformat(changed_files).replace("[", " ").replace("]", ""), bold=True)
        click.secho("]", fg="yellow")
    else:
        click.echo("There is no change")


if __name__ == "__main__":
    main()
