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

Modifications made to each files to change the icon color and angle and remove svg namespace.

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
        files_changed = compare_all_files(DIST_DIR_PATH, Path(temp_dir))

        if not files_changed:
            _console.log("There is no change")
            return
        if only_check:
            _console.log("You should change following files: ", files_changed)
            raise Exception(
                """You can change './qdarktheme/themes' directory, by running pre-commit command or tools.build_resources
            pre-commit    : Run 'pre-commit install' and commit the changes
            python script : Run 'poetry run python -m tools.build_resources'"""
            ) from None

        shutil.rmtree(DIST_DIR_PATH, ignore_errors=True)
        shutil.copytree(temp_dir, DIST_DIR_PATH)

    _console.log("Build finished!", style="green")
    _console.log("Changed contents: ", files_changed)


if __name__ == "__main__":
    _main()
