import re
import shutil
from pathlib import Path
from typing import Union
from xml.etree import ElementTree as ET

from qdarktheme import load_stylesheet
from qdarktheme.util import get_qdarktheme_root_path


class TemplateGenerator:
    def __init__(self, save_folder: Union[Path, str], theme: str) -> None:
        self._qdarktheme_root_folder = get_qdarktheme_root_path()
        self._save_folder = Path(save_folder)
        self._theme = theme

    def generate(self) -> None:
        try:
            self._save_folder.mkdir()
        except FileExistsError:
            pass
        self._copy_svg_folder()
        self._generate_stylesheet_file()
        self._generate_resource_file()

    def _copy_svg_folder(self) -> None:
        svg_original_folder = self._qdarktheme_root_folder / "svg"
        svg_copy_folder = self._save_folder / "svg"
        try:
            svg_copy_folder.mkdir()
        except FileExistsError:
            pass
        try:
            shutil.copytree(str(svg_original_folder / self._theme), str(svg_copy_folder / self._theme))
        except FileExistsError:
            pass

    def _generate_stylesheet_file(self) -> None:
        stylesheet_file = self._save_folder / "stylesheet.qss"
        with stylesheet_file.open(mode="w", encoding="utf-8") as f:
            stylesheet = load_stylesheet("dark")
            stylesheet_for_designer = convert_stylesheet_for_designer(stylesheet)
            f.write(stylesheet_for_designer)

    def _generate_resource_file(self) -> None:
        rcc_tag = ET.Element("RCC", {"version": "1.0"})
        qresource_tab = ET.SubElement(rcc_tag, "qresource", {"prefix": "qdarktheme"})

        svg_original_folder = self._qdarktheme_root_folder / "svg" / self._theme
        for file in svg_original_folder.iterdir():
            file_tag = ET.SubElement(qresource_tab, "file")
            file_tag.text = str(file.relative_to(self._qdarktheme_root_folder))

        resource_file = self._save_folder / "resource.qrc"
        ET.ElementTree(rcc_tag).write(str(resource_file), "utf-8")


def convert_stylesheet_for_designer(stylesheet: str) -> str:
    # Convert to path for resource system
    stylesheet_designer = stylesheet.replace("qdarktheme:", ":/qdarktheme/")
    # Deleate comment
    stylesheet_designer = re.sub("[\s\t]*/\*/?(\n|[^/]|[^*]/)*\*/", "", stylesheet_designer)
    return stylesheet_designer
