"""Module for checking tag validation in GitHub auto release action."""
import argparse
import sys
from importlib.metadata import version

import qdarktheme
from qdarktheme._util import get_logger

_logger = get_logger(__name__)


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
    git_tag_v: str = args.tag_version.replace("v", "")
    package_v = version("pyqtdarktheme")
    if git_tag_v == package_v == qdarktheme.__version__:
        _logger.info("The package version, module version and tag version are the same.")
    else:
        _logger.info("The version names of package and tag are different.")
        _logger.info("tag version(GitHub tags)         : ", git_tag_v)
        _logger.info("package version(pyproject.toml)  : ", package_v)
        _logger.info("module version(__version__)      : ", qdarktheme.__version__)
        sys.exit(1)

    _test_qdarktheme()
    _logger.info("Test finished successfully!")


if __name__ == "__main__":
    _main()
