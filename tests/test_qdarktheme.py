"""Tests for the main program."""
import sys
from importlib import import_module

import pytest

import qdarktheme
from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtWidgets import QApplication


def test_load_palette() -> None:
    """Ensure `load_palette()` load QPalette without error."""
    app = QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore

    for theme in qdarktheme.THEMES:
        app.setPalette(qdarktheme.load_palette(theme))


def test_wrong_theme() -> None:
    """Verify we raise TypeError when inputting wrong theme name."""
    with pytest.raises(TypeError) as e_stylesheet:
        qdarktheme.load_stylesheet("wrong_value")

    with pytest.raises(TypeError) as e_palette:
        qdarktheme.load_palette("wrong_value")

    for e in [e_stylesheet, e_palette]:
        assert str(e.value) == "The argument [theme] can only be specified as 'dark' or 'light'."


def test_qrc() -> None:
    """Test the qt resource files."""
    from qdarktheme.qtpy import QtCore

    if not hasattr(QtCore, "qRegisterResourceData"):
        return

    for theme in qdarktheme.THEMES:
        rc_icons = import_module(f"qdarktheme.dist.{theme}.rc_icons")
        rc_icons.qCleanupResources()  # type: ignore


def test_parse_env_patch() -> None:
    """Test `parse_env_patch()`."""
    from qdarktheme.base import _parse_env_patch

    with pytest.raises(SyntaxError) as e:
        _parse_env_patch('$env_patch{"version": "^6.0.0", "value": "test"};')

    assert "invalid character in qualifier. Available qualifiers" in str(e.value)

    # If Qt module not found
    from qdarktheme import qtpy

    temp_qt_version = qtpy.__version__
    qtpy.__version__ = None
    _parse_env_patch('$env_patch{"version": "==6.0.0", "value": "test"};')
    qtpy.__version__ = temp_qt_version
