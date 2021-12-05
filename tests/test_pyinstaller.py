import sys
from importlib import import_module

import qdarktheme

THEMES = ["dark", "light"]


def test_meipass() -> None:
    sys._MEIPASS = "testpath"  # type: ignore
    for theme in THEMES:
        qdarktheme.load_stylesheet(theme)
    del sys._MEIPASS  # type: ignore


def test_hook() -> None:
    import_module("qdarktheme.__pyinstaller.hook-qdarktheme")


def test_get_hook_dirs() -> None:
    from qdarktheme.__pyinstaller import get_hook_dirs

    get_hook_dirs()
