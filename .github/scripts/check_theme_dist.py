"""Script checking if the commit need to change qdarktheme/dist."""
import sys
from importlib import resources
from pathlib import Path
from tempfile import TemporaryDirectory

import click

sys.path.append(str(Path(__file__).parent.parent.parent))
click.echo(sys.path)

from builder.main import DIST_DIR_PATH, build_resources, compare_all_files  # noqa


def _main():
    click.echo("Checking if this commit need to change qdarktheme/dist..")
    stylesheet = resources.read_text("builder", "base.qss")
    color_schemes = [path for path in Path("builder").glob("theme/*.json") if path.name != "validate.json"]
    svg_dir_path = Path("builder") / "svg"

    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)

        build_resources(temp_dir_path, color_schemes, stylesheet, svg_dir_path)
        # Refresh dist dir
        changed_files = compare_all_files(DIST_DIR_PATH, temp_dir_path)

    if changed_files:
        raise Exception(
            """You need to change 'qdarktheme/dist' directory. You can use pre-commit command or run 'builder/__main__.py' file
        pre-commit    : Run 'pre-commit install' and commit the changes
        python script : Run 'poetry run python builder''"""
        ) from None

    click.secho("There is no change in 'qdarktheme/dist' directory", fg="green")


if __name__ == "__main__":
    _main()
