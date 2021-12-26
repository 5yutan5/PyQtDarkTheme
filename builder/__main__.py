"""Module allowing for `python -m builder`."""
from __future__ import annotations

import argparse
import pprint
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

import click

from builder.main import DIST_DIR_PATH, build_resources, compare_all_files

ROOT_INIT_DOC = '''"""License Information.

All svg files in PyQtDarkTheme is from Material design icons(which uses an Apache 2.0 license).


Material design icons

- Author: Google
- Site: https://fonts.google.com/icons
- Source: https://github.com/google/material-design-icons
- License: Apache License Version 2.0 | https://www.apache.org/licenses/LICENSE-2.0.txt

Modifications made to each files to change the icon color and angle.

The current Material design icons license summary can be viewed at:
https://github.com/google/material-design-icons/blob/master/LICENSE

"""
'''


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program generates resources for Qt Applications.")
    parser.add_argument(
        "-c",
        "--check",
        help="If set this arg, no result will be output.",
        action="store_true",
    )
    return parser.parse_args()


def _list_contents(contents: list) -> None:
    click.secho("[", fg="yellow")
    click.secho(pprint.pformat(contents).replace("[", " ").replace("]", ""), bold=True)
    click.secho("]", fg="yellow")


def _main(only_check: bool = False) -> None:
    if only_check:
        click.echo("Checking if this commit need to change qdarktheme/dist...")
    color_schemes = [path for path in Path(__file__).parent.glob("theme/*.json") if path.name != "validate.json"]

    with TemporaryDirectory() as temp_dir:
        build_resources(Path(temp_dir), color_schemes, ROOT_INIT_DOC)
        # Refresh dist dir
        changed_files = compare_all_files(DIST_DIR_PATH, Path(temp_dir))
        if not changed_files:
            click.echo("There is no change")
            return
        if only_check:
            click.echo("You can change following files: ", nl=False)
            _list_contents(changed_files)
            raise Exception(
                """You need to change 'qdarktheme/dist' directory. You can use pre-commit command or run 'builder/__main__.py' file
            pre-commit    : Run 'pre-commit install' and commit the changes
            python script : Run 'poetry run python builder''"""
            ) from None
        shutil.rmtree(DIST_DIR_PATH, ignore_errors=True)
        shutil.copytree(temp_dir, DIST_DIR_PATH)

    click.secho("Build finished!", fg="green")
    click.echo("Changed contents: ", nl=False)
    _list_contents(changed_files)


if __name__ == "__main__":
    args = _parse_args()
    only_check = args.check
    _main(only_check)
