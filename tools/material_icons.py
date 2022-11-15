"""Module for downloading material design icons."""
import json
import logging
from urllib import request

from tools._util import get_style_path

logging.basicConfig(level=logging.INFO)


def _get_available_icons() -> dict[str, str]:
    material_icons_info_file = get_style_path() / "svg/material_design_icons.json"
    return json.loads(material_icons_info_file.read_text())


def _download_icon(name: str, style: str) -> None:
    """Download Google material deign icon.

    Use assets of https://github.com/marella/material-design-icons.
    """
    url = f"https://raw.githubusercontent.com/marella/material-design-icons/main/svg/{style}/{name}.svg"
    material_icons_dir = get_style_path() / "svg" / "material"
    material_icons_dir.mkdir(parents=True, exist_ok=True)
    output_path = material_icons_dir / f"{name}.svg"
    logging.info("Downloading: %s", url)
    with request.urlopen(url) as response:
        svg: str = response.read().decode()
        output_path.write_text(svg)


def _download_missing_icons() -> None:
    """Download missing material design icons."""
    for name, style in _get_available_icons().items():
        if not (get_style_path() / f"svg/material/{name}.svg").exists():
            _download_icon(name, style)


def _remove_unused_icons() -> None:
    """Remove unused material design icons."""
    available_icons = _get_available_icons()
    for svg_path in (get_style_path() / "svg/material").glob("*.svg"):
        if svg_path.stem not in available_icons:
            logging.info("Removing: %s", svg_path)
            svg_path.unlink()


def reflect_icon_conf_changes() -> None:
    """Reflect changes of ``style/svg/material_design_icons.json``."""
    _download_missing_icons()
    _remove_unused_icons()


def _download_all() -> None:
    """Download all icon files to use in PyQtDarkTheme styles."""
    for name, style in _get_available_icons().items():
        _download_icon(name, style)


def update_icons() -> None:
    """Update all material design icons."""
    _download_all()
    reflect_icon_conf_changes()
