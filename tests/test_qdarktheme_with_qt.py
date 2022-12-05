"""Tests for the main program with Qt."""
import pytest

import qdarktheme
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
