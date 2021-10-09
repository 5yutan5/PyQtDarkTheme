# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

from builder.color import RGBA
from qdarktheme.util import multireplace


# A class that handle the properties of the $url{...} variable in the stylesheet template.
@dataclass(unsafe_hash=True, frozen=True)
class Url:
    icon: str
    id: str
    rotate: str
    match_text: str
    file_name: str


def parse_url(stylesheet: str) -> set[Url]:
    """Parse $type_patch{...} and $env_patch{...} in template stylesheet."""
    urls = set()
    for match in re.finditer(r"\$url\{.+\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$url", "")

        icon, id, rotate = json.loads(json_text).values()
        file_name = f"{icon.replace('.svg', '')}_{id}_{rotate}.svg"
        urls.add(Url(icon, id, rotate, match_text, file_name))
    return urls


def build_svg_file(urls: set[Url], colors: dict[str, str], output_folder_path: Path) -> None:
    svg_codes: dict[str, str] = {}  # {file name: svg code}
    for content in resources.contents("builder.svg"):
        if ".svg" not in content:  # Only svg file
            continue
        svg_codes[content] = resources.read_text("builder.svg", content)

    # QSvg does not support #RRGGBBAA. Therefore, we need to set the alpha value to `fill-opacity` instead.
    def to_svg_color_format(hex_code: str) -> str:
        if color is None:
            return 'fill=""'
        r, g, b, a = RGBA.from_hex(hex_code)
        return f'fill="rgb({r}, {g}, {b})" fill-opacity="{a}"'

    for url in urls:
        color = colors[url.id]
        # Change color and rotate. See https://stackoverflow.com/a/15139069/13452582
        new_contents = f'{to_svg_color_format(color)} transform="rotate({url.rotate}, 12, 12)"'
        svg_code_converted = svg_codes[url.icon].replace('fill="#FFFFFF"', new_contents)

        with (output_folder_path / url.file_name).open("w") as f:
            f.write(svg_code_converted)


if __name__ == "__main__":
    stylesheet = resources.read_text("builder", "base.qss")
    urls = parse_url(stylesheet)
    dist_folder_path = Path.cwd() / "qdarktheme" / "dist"

    # Reflesh dist folder
    shutil.rmtree(str(dist_folder_path), ignore_errors=True)
    dist_folder_path.mkdir()
    (dist_folder_path / "__init__.py").touch()

    for contents in resources.contents("builder.theme"):
        if ".json" not in contents or "validate.json" in contents:
            continue
        with resources.open_binary("builder.theme", contents) as f:
            colors: dict[str, str] = json.load(f)
            theme_name = contents.replace(".json", "")

        # Setup output folder
        output_folder_path = dist_folder_path / theme_name
        output_folder_path.mkdir()
        (output_folder_path / "__init__.py").touch()

        # Build svg
        svg_folder_path = output_folder_path / "svg"
        svg_folder_path.mkdir()
        build_svg_file(urls, colors, svg_folder_path)

        # Build template stylesheet
        url_replacements = {url.match_text: f"url(${{path}}/dist/{theme_name}/svg/{url.file_name})" for url in urls}
        colors = {f"${key}": str(RGBA.from_hex(value)) for key, value in colors.items()}
        template_stylesheet = multireplace(stylesheet, {**url_replacements, **colors})

        with (output_folder_path / "stylesheet.qss").open("w") as f:
            f.write(template_stylesheet)
