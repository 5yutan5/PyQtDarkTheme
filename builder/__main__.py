"""Module allowing for `python -m builder`."""
from __future__ import annotations

import argparse
import pprint
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


import click
from builder.main import DIST_DIR_PATH, build_resources, compare_all_files


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
    package_root_path = Path(__file__).parent
    color_schemes = [path for path in package_root_path.glob("theme/*.json") if path.name != "validate.json"]
    svg_dir_path = package_root_path / "svg"

    with TemporaryDirectory() as temp_dir:
        build_resources(Path(temp_dir), color_schemes, svg_dir_path)
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
