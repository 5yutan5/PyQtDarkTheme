"""Tests for PyInstaller."""
import sys
from importlib import import_module

import qdarktheme


def test_meipass() -> None:
    """Verify that we use `sys._MEIPASS` correctly when `sys._MEIPASS` is exist."""
    sys._MEIPASS = "testpath"  # type: ignore
    for theme in qdarktheme.THEMES:
        qdarktheme.load_stylesheet(theme)
    del sys._MEIPASS  # type: ignore


def test_hook() -> None:
    """Test qdarktheme hook for PyInstaller."""
    from qdarktheme.__pyinstaller import get_hook_dirs

    get_hook_dirs()
    import_module("qdarktheme.__pyinstaller.hook-qdarktheme")
