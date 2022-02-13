"""Tests for the main program."""
import sys
from importlib import import_module

import pytest

import qdarktheme


@pytest.mark.available_qt()
def test_load_palette() -> None:
    """Ensure `load_palette()` load QPalette without error."""
    from qdarktheme.qtpy.QtCore import Qt
    from qdarktheme.qtpy.QtWidgets import QApplication

    app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore

    for theme in qdarktheme.get_themes():
        app.setPalette(qdarktheme.load_palette(theme))


def test_wrong_theme() -> None:
    """Verify we raise TypeError when inputting wrong theme name."""
    with pytest.raises(TypeError) as e_stylesheet:
        qdarktheme.load_stylesheet("wrong_value")

    with pytest.raises(TypeError) as e_palette:
        qdarktheme.load_palette("wrong_value")

    for e in [e_stylesheet, e_palette]:
        assert e.type == TypeError


def test_wrong_border_style() -> None:
    """Verify we raise TypeError when inputting wrong border shape name."""
    with pytest.raises(TypeError) as e:
        qdarktheme.load_stylesheet(border="none")
    assert e.type == TypeError


@pytest.mark.available_qt()
def test_qrc() -> None:
    """Test the qt resource files."""
    from qdarktheme.qtpy import QtCore

    if not hasattr(QtCore, "qRegisterResourceData"):
        return

    for theme in qdarktheme.get_themes():
        rc_icons = import_module(f"qdarktheme.themes.{theme}.rc_icons")
        rc_icons.qCleanupResources()  # type: ignore


def test_parse_env_patch() -> None:
    """Test `parse_env_patch()`."""
    from qdarktheme.main import _parse_env_patch

    with pytest.raises(SyntaxError) as e:
        _parse_env_patch('$env_patch{"version": "^6.0.0", "value": "test"};')

    assert "invalid character in qualifier. Available qualifiers" in str(e.value)

    # If Qt module not found
    from qdarktheme import qtpy

    temp_qt_version = qtpy.__version__
    qtpy.__version__ = None
    _parse_env_patch('$env_patch{"version": "==6.0.0", "value": "test"};')
    qtpy.__version__ = temp_qt_version
