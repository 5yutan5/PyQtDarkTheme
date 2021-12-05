# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import pprint
import shutil
from importlib import resources
from pathlib import Path
from tempfile import TemporaryDirectory

import click

from builder.main import DIST_DIR_PATH, build_resources, compare_all_files


def _main() -> None:
    stylesheet = resources.read_text("builder", "base.qss")
    color_schemes = [path for path in Path(__file__).parent.glob("theme/*.json") if path.name != "validate.json"]
    svg_dir_path = Path(__file__).parent / "svg"

    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)

        build_resources(temp_dir_path, color_schemes, stylesheet, svg_dir_path)
        # Refresh dist dir
        changed_files = compare_all_files(DIST_DIR_PATH, temp_dir_path)
        if changed_files:
            shutil.rmtree(DIST_DIR_PATH, ignore_errors=True)
            shutil.copytree(temp_dir, DIST_DIR_PATH)

    click.secho("Build finished!", fg="green")
    if changed_files:
        click.echo("Changed contents: " + click.style("[", fg="yellow"))
        click.secho(pprint.pformat(changed_files).replace("[", " ").replace("]", ""), bold=True)
        click.secho("]", fg="yellow")
    else:
        click.echo("There is no change")


if __name__ == "__main__":
    _main()
