"""Module for checking tag validation in GitHub auto release action."""
import argparse
import sys
from importlib.metadata import version

from rich.console import Console

import qdarktheme

_console = Console(force_terminal=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program check package built by poetry.")
    parser.add_argument(
        "--tag-version",
        help="Version name of the pushed tag",
        required=True,
    )
    return parser.parse_args()


def _test_qdarktheme() -> None:
    for theme in qdarktheme.get_themes():
        qdarktheme.load_stylesheet(theme)
        qdarktheme.load_palette(theme)


def _main() -> None:
    args = _parse_args()
    tag_v: str = args.tag_version.replace("v", "")
    package_v = version("pyqtdarktheme")
    if tag_v == package_v == qdarktheme.__version__:
        _console.log("The package version, module version and tag version are the same.", style="green")
    else:
        _console.log("The version names of package and tag are different.", style="red")
        _console.log(f"tag version(GitHub tags)         : {tag_v}")
        _console.log(f"package version(pyproject.toml)  : {package_v}")
        _console.log(f"module version(__version__)      : {qdarktheme.__version__}")
        sys.exit(1)

    _test_qdarktheme()
    _console.log("Test finished successfully!", style="green")


if __name__ == "__main__":
    _main()
