"""Module for downloading svg of material design icons."""
import json
import logging
from pathlib import Path
from urllib import request

from tools._util import get_style_path

logging.basicConfig(level=logging.INFO)


def _download_material_icons_svg(name: str, style: str, output_dir: Path) -> None:
    url = f"https://raw.githubusercontent.com/marella/material-design-icons/main/svg/{style}/{name}.svg"
    output_path = output_dir / f"{name}.svg"
    logging.info("Downloading: %s", url)
    with request.urlopen(url) as response:
        svg: str = response.read().decode()
        output_path.write_text(svg)


def _main() -> None:
    material_icons_dir = get_style_path() / "svg" / "material"
    material_icons_info_file = get_style_path() / "svg/material_design_icons.json"
    material_icons_dir.mkdir(parents=True, exist_ok=True)

    material_icons: dict[str, str] = json.loads(material_icons_info_file.read_text())
    for name, style in material_icons.items():
        _download_material_icons_svg(name, style, material_icons_dir)


if __name__ == "__main__":
    _main()
