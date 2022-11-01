"""The main module of build resources program."""
from __future__ import annotations

import json
import re
from filecmp import cmpfiles
from importlib import resources
from pathlib import Path

from tools.util import get_style_path


def _remove_qss_comment(stylesheet: str) -> str:
    """Remove qss comment from the stylesheet string."""
    stylesheet = re.sub(r" */\*[\s\S]*?\*/", "", stylesheet)
    # Change multi blank lines to one blank line.
    return re.sub(r"\n\s*\n", "\n", stylesheet)


def _mk_root_init_file(output_path: Path, themes: list[str], doc_string: str = "") -> None:
    code = f"{doc_string}\n"
    code += "from qdarktheme.resources.color_schema import COLOR_SCHEMAS\n"
    code += "from qdarktheme.resources.palette import mk_q_palette\n"
    code += "from qdarktheme.resources.svg import SVG_RESOURCES\n"
    code += "from qdarktheme.resources.template_stylesheet import TEMPLATE_STYLESHEET\n\n"
    code += f"""THEMES = {str(tuple(themes)).replace("'", '"')}\n"""
    (output_path / "__init__.py").write_text(code)


def _mk_svg_resource(output: Path):
    svg_dir_path = get_style_path() / "svg"
    svg_resources = {svg_path.stem: svg_path.read_text() for svg_path in svg_dir_path.glob("*.svg")}
    svg_resources = {
        name: re.compile(r'xmlns="[\s\S]*?" ').sub("", svg) for name, svg in svg_resources.items()
    }

    code = '"""SVG resource."""\n\n'
    code += 'SVG_RESOURCES = """\n'
    code += json.dumps(svg_resources, sort_keys=True).replace('\\"', '\\\\"')
    code += '\n"""  # noqa: E501\n'
    output.write_text(code)


def _mk_template_stylesheet(output: Path):
    stylesheet = (get_style_path() / "base.qss").read_text()
    stylesheet = _remove_qss_comment(stylesheet)

    code = '"""Template stylesheet."""\n\n'
    code += 'TEMPLATE_STYLESHEET = """\n'
    code += stylesheet
    code += '\n"""  # noqa: E501\n'
    output.write_text(code)


def _mk_palette_file(output: Path):
    palette = resources.read_text("tools.build_resources", "palette.template.py")
    output.write_text(palette)


def _mk_color_schema_resource(color_schemas: dict[str, dict], output: Path):
    code = '"""Color schemas."""\n\n'
    code += "COLOR_SCHEMAS = {\n"
    for theme, color_schema in sorted(color_schemas.items()):
        code += f"""    "{theme}": '{json.dumps(color_schema, sort_keys=True)}',  # noqa: E501\n"""
    code += "}\n"
    output.write_text(code)


def build_resources(build_path: Path, theme_file_paths: list[Path], root_init_file_doc: str) -> None:
    """Build resources for qdarktheme module."""
    themes = tuple(path.stem for path in theme_file_paths)
    color_schemas = {path.stem: json.loads(path.read_bytes()) for path in theme_file_paths}
    _mk_color_schema_resource(color_schemas, output=build_path / "color_schema.py")
    _mk_palette_file(output=build_path / "palette.py")
    _mk_svg_resource(output=build_path / "svg.py")
    _mk_template_stylesheet(output=build_path / "template_stylesheet.py")

    _mk_root_init_file(build_path, sorted(themes), root_init_file_doc)


def compare_all_files(dir_path1: Path, dir_path2: Path) -> list[str]:
    """Check if the contents of the files with the same name in the two directories are the same.

    Args:
        dir1: The directory containing files.
        dir2: The directory containing files.

    Returns:
        list[str]: A list of file names with different contents.
    """
    target_files = set()
    for file in dir_path2.glob("**/*"):
        if not file.is_file():
            continue
        target_files.add(str(file).replace(str(dir_path2), "")[1:])
    _, mismatch, err = cmpfiles(dir_path1, dir_path2, target_files)
    return [str(file) for file in mismatch + err]
