"""Tests for the main program with Qt."""
import platform
import re

import pytest

import qdarktheme
from qdarktheme.qtpy.QtGui import QPalette
from qdarktheme.qtpy.QtWidgets import QApplication


@pytest.mark.parametrize(
    ("theme", "custom_colors"),
    [
        # Test theme
        ("dark", None),
        ("light", None),
        # Test theme and custom_colors
        ("dark", {}),
        ("dark", {"foreground": "#112233"}),
        ("dark", {"foreground>icon": "#112233"}),
        # Test color code
        ("dark", {"foreground": "#112"}),
        ("dark", {"foreground": "#11223344"}),
        ("dark", {"foreground": "#1122"}),
        # Test automatic theme
        ("auto", None),
        ("auto", {"foreground": "#112233"}),
        ("auto", {"[dark]": {"foreground": "#112233"}}),
        ("auto", {"foreground": "#112233", "[dark]": {"foreground": "#112233"}}),
        ("auto", {"foreground": "#112233", "[light]": {"foreground": "#112233"}}),
        ("auto", {"[dark]": {"foreground": "#112233"}, "[light]": {"foreground": "#112233"}}),
    ],
)
def test_load_palette(theme, custom_colors) -> None:
    """Verify that the function `load_stylesheet()` runs successfully when using various arguments."""
    qdarktheme.load_palette(theme, custom_colors)


def test_apply_stylesheet_to_qt_app(qapp: QApplication) -> None:
    """Verify that the function `load_stylesheet()` runs without error."""
    qapp.setStyleSheet(qdarktheme.load_stylesheet())


def test_apply_palette_to_qt_app(qapp: QApplication) -> None:
    """Verify that the function `load_palette()` runs without error."""
    qapp.setPalette(qdarktheme.load_palette())


@pytest.mark.parametrize(
    ("theme", "additional_qss"),
    [
        ("dark", None),
        ("dark", "QWidget{color: red;}"),
    ],
)
def test_setup_style(qapp: QApplication, theme, additional_qss) -> None:
    """Verify that the function `setup_style()` runs without error."""
    qdarktheme.setup_style(theme, additional_qss=additional_qss)


def test_enable_high_dpi(qapp: QApplication) -> None:
    """Verify that the function `enable_high_dpi()` runs without error."""
    qdarktheme.enable_hi_dpi()


def test_stop_sync(qapp: QApplication) -> None:
    """Verify that the function `stop_sync()` runs without error."""
    qdarktheme.setup_style()
    qdarktheme.stop_sync()


def test_setup_style_without_qapp(mocker) -> None:
    """Verify we raise Exception when qapp is none."""
    mocker.patch("qdarktheme.qtpy.QtWidgets.QApplication.instance", return_value=None)
    with pytest.raises(
        Exception, match=re.escape("setup_style() must be called after instantiation of QApplication.")
    ):
        qdarktheme.setup_style()


if platform.system() == "Darwin":

    def test_theme_event_filter(qapp: QApplication) -> None:
        """Verify that the internal class `ThemeEventFilter` runs without error."""
        qdarktheme.setup_style()
        qapp.setPalette(QPalette())
        # Test whether to skip changes if theme is the same
        qapp.setPalette(QPalette())
