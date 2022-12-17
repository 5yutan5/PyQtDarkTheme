"""Main module for building style resources for qdarktheme."""
from __future__ import annotations

import json
import logging
import re
import shutil
from collections import defaultdict
from filecmp import cmpfiles
from pathlib import Path
from pprint import pformat
from tempfile import TemporaryDirectory

from tools import material_icons
from tools._util import get_style_path

logging.basicConfig(level=logging.INFO)

_ROOT_INIT_DOC = '''"""Package including resources.

**Warning**

This package created programmatically. All changes made in this file will be lost!
Created by the `PyQtDarkTheme/tools/build_styles`.

"""
'''


def _get_dist_path() -> Path:
    return Path(__file__).parent.parent.parent / "qdarktheme" / "_resources"


def _remove_qss_comment(stylesheet: str) -> str:
    """Remove qss comment from the stylesheet string."""
    stylesheet = re.sub(r" */\*[\s\S]*?\*/", "", stylesheet)
    # Change multi blank lines to one blank line.
    return re.sub(r"\n\s*\n", "\n", stylesheet)


def _mk_root_init_file(output: Path, themes: list[str], doc_string: str) -> None:
    themes.append("auto")

    code = f"{doc_string}\n"
    code += "from qdarktheme._resources._color_values import COLOR_VALUES\n"
    code += "from qdarktheme._resources._palette import mk_q_palette\n"
    code += "from qdarktheme._resources._svg import SVG_RESOURCES\n"
    code += "from qdarktheme._resources._template_stylesheet import (\n"
    code += "    TEMPLATE_STANDARD_ICONS_STYLESHEET,\n"
    code += "    TEMPLATE_STYLESHEET,\n"
    code += ")\n\n"
    code += f"""THEMES = {str(tuple(themes)).replace("'", '"')}\n"""
    (output / "__init__.py").write_text(code)


def _mk_svg_resource(svg_dir: Path, output: Path):
    material_icons.reflect_icon_conf_changes()

    svg_resources = {svg_file.stem: svg_file.read_text() for svg_file in svg_dir.glob("*/*.svg")}
    for name, svg_resource in svg_resources.items():
        svg_resources[name] = re.compile(r'xmlns="[\s\S]*?" ').sub("", svg_resource)

    code = '"""SVG resource."""\n\n'
    code += 'SVG_RESOURCES = """\n'
    code += json.dumps(svg_resources, sort_keys=True).replace('\\"', '\\\\"')
    code += '\n"""  # noqa: E501\n'
    output.write_text(code)


def _mk_standard_icon_map(icon_map_file: Path, output: Path):
    standard_icons: dict[str, dict] = json.loads(icon_map_file.read_text())

    for standard_icon in standard_icons.values():
        if "qss" in standard_icon:
            del standard_icon["qss"]

    incompatible_names = (
        "SP_LineEditClearButton",
        "SP_DialogYesToAllButton",
        "SP_DialogNoToAllButton",
        "SP_DialogSaveAllButton",
        "SP_DialogAbortButton",
        "SP_DialogRetryButton",
        "SP_DialogIgnoreButton",
        "SP_RestoreDefaultsButton",
        "SP_TabCloseButton",
    )
    incompatible_standard_icons = {
        name: standard_icons.pop(name) for name in list(standard_icons) if name in incompatible_names
    }

    icon_map_code = pformat(standard_icons, sort_dicts=True, indent=4)
    for icon_name in standard_icons.keys():
        icon_map_code = icon_map_code.replace(f"'{icon_name}'", f"QStyle.StandardPixmap.{icon_name}")
    icon_map_code = icon_map_code[0] + "\n " + icon_map_code[1:-1] + ",\n" + icon_map_code[-1]

    add_icon_to_map_code = ""
    for icon_name in sorted(incompatible_standard_icons.keys()):
        add_icon_to_map_code += f'\nif hasattr(QStyle.StandardPixmap, "{icon_name}"):\n'
        add_icon_to_map_code += f"    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.{icon_name}]"
        add_icon_to_map_code += (
            f" = {incompatible_standard_icons[icon_name]}  # type: ignore  # noqa: E501\n"
        )

    code = '"""Icon map that overrides standard icons."""\n'
    code += "from qdarktheme.qtpy.QtWidgets import QStyle\n\n"
    code += "NEW_STANDARD_ICON_MAP = "
    code += icon_map_code.replace("'", '"') + "\n"
    code += add_icon_to_map_code.replace("'", '"')
    output.write_text(code)


def _create_icon_definition(icon_id: str, rotate: int | None, qss_property: str) -> str:
    url_placeholder = f'foreground|color(state="icon")|url(id="{icon_id}"'
    if rotate is not None:
        url_placeholder += f", rotate={rotate}"
    url_placeholder += ")"
    if qss_property == "lineedit-clear-button-icon":
        return f'    {{{{ {url_placeholder})|env(value="{qss_property}:${{}};",version=">=6.0.0") }}}}'
    return f"    {qss_property}: {{{{ {url_placeholder} }}}}"


def _mk_template_standard_icon_stylesheet(icon_map_file: Path) -> str:
    standard_icons: dict[str, dict] = json.loads(icon_map_file.read_text())
    definitions_by_selector: defaultdict[tuple[str], set[str]] = defaultdict(set)

    for value in standard_icons.values():
        if "qss" not in value:
            continue
        qss_widgets: tuple[str, ...] = tuple(sorted(value["qss"]["widgets"]))
        definition = _create_icon_definition(
            icon_id=value["id"],
            rotate=value.get("rotate"),
            qss_property=value["qss"]["property"],
        )
        definitions_by_selector[qss_widgets].add(definition)

    qss = ""
    for selector, definitions in sorted(definitions_by_selector.items()):
        qss += ",\n".join(selector) + " {\n"
        qss += ";\n".join(sorted(definitions)) + ";\n"
        qss += "}\n"
    return qss


def _mk_template_stylesheet(base_stylesheet_file: Path, icon_map_file: Path, output: Path):
    base_qss = base_stylesheet_file.read_text()
    base_qss = _remove_qss_comment(base_qss)

    code = '"""Template stylesheet."""\n\n'
    code += 'TEMPLATE_STYLESHEET = """\n'
    code += base_qss
    code += '\n"""  # noqa: E501\n'
    code += 'TEMPLATE_STANDARD_ICONS_STYLESHEET = """\n'
    code += _mk_template_standard_icon_stylesheet(icon_map_file)
    code += '"""  # noqa: E501\n'
    output.write_text(code)


def _mk_palette_file(template_palette_path: Path, output: Path):
    template_palette = template_palette_path.read_text()
    output.write_text(template_palette)


def _mk_color_resource(color_values: dict[str, dict], output: Path):
    code = '"""Default color values."""\n\n'
    code += "COLOR_VALUES = {\n"
    for theme, color_value in sorted(color_values.items()):
        code += f"""    "{theme}": '{json.dumps(color_value, sort_keys=True)}',  # noqa: E501\n"""
    code += "}\n"
    output.write_text(code)


def _build_styles(build_path: Path) -> None:
    style_path = get_style_path()
    theme_paths = [path for path in style_path.glob("colors/*.json") if path.name != "validate.json"]
    themes = sorted(path.stem for path in theme_paths)
    color_values = {path.stem: json.loads(path.read_bytes()) for path in theme_paths}

    _mk_color_resource(color_values, output=build_path / "_color_values.py")
    _mk_palette_file(style_path / "palette.template.py", output=build_path / "_palette.py")
    _mk_svg_resource(style_path / "svg", output=build_path / "_svg.py")
    _mk_standard_icon_map(
        style_path / "svg/new_standard_icons.json", output=build_path / "standard_icons.py"
    )
    _mk_template_stylesheet(
        style_path / "base.qss",
        style_path / "svg/new_standard_icons.json",
        output=build_path / "_template_stylesheet.py",
    )
    _mk_root_init_file(build_path, themes, _ROOT_INIT_DOC)


def _compare_all_files(dir1: Path, dir2: Path) -> list[str]:
    """Check if the contents of the files with the same name in the two directories are the same.

    Args:
        dir1: The directory containing files.
        dir2: The directory containing files.

    Returns:
        A list of file names with different contents.
    """
    target_files = {str(path.relative_to(dir2)) for path in dir2.glob("**/*") if path.is_file()}
    _, mismatch_path, err_path = cmpfiles(dir1, dir2, target_files)
    return mismatch_path + err_path


def main() -> None:
    """Build style resources for qdarktheme."""
    dist_dir_path = _get_dist_path()

    with TemporaryDirectory() as temp_dir:
        _build_styles(Path(temp_dir))
        # Refresh dist dir
        changed_files = _compare_all_files(dist_dir_path, Path(temp_dir))
        if len(changed_files) == 0:
            logging.info("There is no change of qdarktheme module")
            return

        shutil.rmtree(dist_dir_path, ignore_errors=True)
        shutil.copytree(temp_dir, dist_dir_path)

    logging.info("Build finished!")
    logging.info("Changed some contents in qdarktheme module: %s", changed_files)
