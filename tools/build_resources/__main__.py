"""Module allowing for `python -m tools.build_resources`."""
from __future__ import annotations

import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from qdarktheme.util import get_logger, get_qdarktheme_root_path
from tools.build_resources.main import build_resources, compare_all_files
from tools.util import get_style_path

logger = get_logger(__name__)

ROOT_INIT_DOC = '''"""Package including resources.

**Warning**

This package created programmatically. All changes made in this file will be lost!
Created by the `qdarktheme/tools/build_resources`.

"""
'''


def _main() -> None:
    color_schemes = [
        path for path in get_style_path().glob("colors/*.json") if path.name != "validate.json"
    ]
    dist_dir_path = get_qdarktheme_root_path() / "resources"

    with TemporaryDirectory() as temp_dir:
        build_resources(Path(temp_dir), color_schemes, ROOT_INIT_DOC)
        # Refresh dist dir
        files_changed = compare_all_files(dist_dir_path, Path(temp_dir))

        if not files_changed:
            logger.info("There is no change")
            return

        shutil.rmtree(dist_dir_path, ignore_errors=True)
        shutil.copytree(temp_dir, dist_dir_path)

    logger.info("Build finished!")
    logger.info("Changed contents: %s", files_changed)


if __name__ == "__main__":
    _main()
