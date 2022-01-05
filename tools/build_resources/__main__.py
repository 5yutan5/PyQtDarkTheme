"""Module allowing for `python -m tools.build_resources`."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from rich.console import Console

from tools.build_resources.main import DIST_DIR_PATH, build_resources, compare_all_files

ROOT_INIT_DOC = '''"""Package including resources.

**Warning**

This package created programmatically. All changes made in this file will be lost!
Created by the `qdarktheme/tools/build_resources`.


License Information
===================

Material design icons
---------------------

All svg files in PyQtDarkTheme is from Material design icons(which uses an Apache 2.0 license).

- Author: Google
- Site: https://fonts.google.com/icons
- Source: https://github.com/google/material-design-icons
- License: Apache License Version 2.0 | https://www.apache.org/licenses/LICENSE-2.0.txt

Modifications made to each files to change the icon color and angle.

The current Material design icons license summary can be viewed at:
https://github.com/google/material-design-icons/blob/master/LICENSE


QDarkStyleSheet(Source code)
----------------------------

Qt stylesheets are originally fork of QDarkStyleSheet(MIT License).

- Author: Colin Duquesnoy
- Site: https://github.com/ColinDuquesnoy/QDarkStyleSheet
- Source: https://github.com/ColinDuquesnoy/QDarkStyleSheet
- License: MIT License | https://opensource.org/licenses/MIT

Modifications made to a file to change the style.

The current QDarkStyleSheet license summary can be viewed at:
https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/LICENSE.rst

"""
'''
_console = Console(force_terminal=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program generates resources for Qt Applications.")
    parser.add_argument(
        "-c",
        "--check",
        help="If set this arg, no result will be output.",
        action="store_true",
    )
    return parser.parse_args()


def _main() -> None:
    args = _parse_args()
    only_check = args.check
    if only_check:
        _console.log("Checking if this commit need to change qdarktheme/themes...")
    color_schemes = [path for path in Path(__file__).parent.glob("themes/*.json") if path.name != "validate.json"]

    with TemporaryDirectory() as temp_dir:
        build_resources(Path(temp_dir), color_schemes, ROOT_INIT_DOC)
        # Refresh dist dir
        changed_files = compare_all_files(DIST_DIR_PATH, Path(temp_dir))
        if not changed_files:
            _console.log("There is no change")
            return
        for file in changed_files:
            _console.print(str(DIST_DIR_PATH))
            _console.print((DIST_DIR_PATH.parent.parent / file).read_text())
            _console.print(str(temp_dir))
            _console.print((Path(temp_dir).parent.parent / file).read_text())
        if only_check:
            _console.log("You can change following files: ", changed_files)
            raise Exception(
                """You need to change 'qdarktheme/themes' directory. You can use pre-commit command or run
                'tools/build_resources/__main__.py' file
            pre-commit    : Run 'pre-commit install' and commit the changes
            python script : Run 'poetry run python -m tools.build_resources'"""
            ) from None
        shutil.rmtree(DIST_DIR_PATH, ignore_errors=True)
        shutil.copytree(temp_dir, DIST_DIR_PATH)

    _console.log("Build finished!", style="green")
    _console.log("Changed contents: ", changed_files)


if __name__ == "__main__":
    _main()
