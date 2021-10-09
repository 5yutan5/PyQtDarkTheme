# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

import inspect
import json
from pathlib import Path

import qdarktheme


def _replace_variable_to_value(contents: str, value_map: dict) -> str:
    for variable_name, color_code in value_map.items():
        # Replace the variable ${main_theme} contained in the svg file name bg the main-theme name.
        if variable_name == "main_theme":
            contents = contents.replace("${main_theme}", color_code)

        # Replace the variable by color code
        contents = contents.replace(f"${variable_name};", f"{color_code};")
    # Replace the variable by prefix or absolute path
    path = Path(inspect.getfile(qdarktheme)).parent
    contents = contents.replace("${path}", str(path))
    return contents


def compile_stylesheet(stylesheet_file: Path, theme_file: Path) -> str:
    try:
        with stylesheet_file.open() as stylesheet_f, theme_file.open() as theme_f:
            stylesheet = stylesheet_f.read()
            value_map = json.load(theme_f)

            stylesheet_compiled = _replace_variable_to_value(stylesheet, value_map)
            return stylesheet_compiled
    except FileNotFoundError:
        raise FileNotFoundError(
            "Unable to load the QSS file."
            f"\nQSS file path: {stylesheet_file}"
            "\nThe qss file may be crushed or not installed properly."
            "\nTry reinstalling the module again.[pip install qdarktheme]"
            "\nAlso, this module has only been tested on mac and windows."
            "\nOperation on other operating systems, such as Linux, is not guaranteed."
        ) from None
