"""The main module of build resources program."""
from __future__ import annotations

import json
import re
import shutil
from filecmp import cmpfiles
from pathlib import Path
from tempfile import TemporaryDirectory

from qdarktheme._util import get_logger, get_qdarktheme_root_path
from tools.util import get_style_path

_logger = get_logger(__name__)

_ROOT_INIT_DOC = '''"""Package including resources.

**Warning**

This package created programmatically. All changes made in this file will be lost!
Created by the `qdarktheme/tools/build_resources`.

"""
'''


def _remove_qss_comment(stylesheet: str) -> str:
    """Remove qss comment from the stylesheet string."""
    stylesheet = re.sub(r" */\*[\s\S]*?\*/", "", stylesheet)
    # Change multi blank lines to one blank line.
    return re.sub(r"\n\s*\n", "\n", stylesheet)


def _mk_root_init_file(output_path: Path, themes: list[str], doc_string: str = "") -> None:
    code = f"{doc_string}\n"
    code += "from qdarktheme._resources._color_values import COLOR_VALUES\n"
    code += "from qdarktheme._resources._palette import mk_q_palette\n"
    code += "from qdarktheme._resources._svg import SVG_RESOURCES\n"
    code += "from qdarktheme._resources._template_stylesheet import TEMPLATE_STYLESHEET\n\n"
    code += f"""THEMES = {str(tuple(themes)).replace("'", '"')}\n"""
    (output_path / "__init__.py").write_text(code)


def _mk_svg_resource(svg_dir_path: Path, output: Path):
    svg_resources = {svg_path.stem: svg_path.read_text() for svg_path in svg_dir_path.glob("*.svg")}
    svg_resources = {
        name: re.compile(r'xmlns="[\s\S]*?" ').sub("", svg) for name, svg in svg_resources.items()
    }

    code = '"""SVG resource."""\n\n'
    code += 'SVG_RESOURCES = """\n'
    code += json.dumps(svg_resources, sort_keys=True).replace('\\"', '\\\\"')
    code += '\n"""  # noqa: E501\n'
    output.write_text(code)


def _mk_template_stylesheet(stylesheet_path: Path, output: Path):
    stylesheet = stylesheet_path.read_text()
    stylesheet = _remove_qss_comment(stylesheet)

    code = '"""Template stylesheet."""\n\n'
    code += 'TEMPLATE_STYLESHEET = """\n'
    code += stylesheet
    code += '\n"""  # noqa: E501\n'
    output.write_text(code)


def _mk_palette_file(palette_path: Path, output: Path):
    palette = palette_path.read_text()
    output.write_text(palette)


def _mk_color_resource(color_values: dict[str, dict], output: Path):
    code = '"""Default color values."""\n\n'
    code += "COLOR_VALUES = {\n"
    for theme, color_value in sorted(color_values.items()):
        code += f"""    "{theme}": '{json.dumps(color_value, sort_keys=True)}',  # noqa: E501\n"""
    code += "}\n"
    output.write_text(code)


def _build_resources(build_path: Path) -> None:
    style_path = get_style_path()
    theme_paths = [path for path in style_path.glob("colors/*.json") if path.name != "validate.json"]
    themes = sorted(path.stem for path in theme_paths)
    color_values = {path.stem: json.loads(path.read_bytes()) for path in theme_paths}

    _mk_color_resource(color_values, output=build_path / "_color_values.py")
    _mk_palette_file(style_path / "palette.template.py", output=build_path / "_palette.py")
    _mk_svg_resource(style_path / "svg", output=build_path / "_svg.py")
    _mk_template_stylesheet(style_path / "base.qss", output=build_path / "_template_stylesheet.py")
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
    """Build resources for qdarktheme."""
    dist_dir_path = get_qdarktheme_root_path() / "_resources"

    with TemporaryDirectory() as temp_dir:
        _build_resources(Path(temp_dir))
        # Refresh dist dir
        changed_files = _compare_all_files(dist_dir_path, Path(temp_dir))
        if len(changed_files) == 0:
            _logger.info("There is no change")
            return

        shutil.rmtree(dist_dir_path, ignore_errors=True)
        shutil.copytree(temp_dir, dist_dir_path)

    _logger.info("Build finished!")
    _logger.info("Changed contents: %s", changed_files)
