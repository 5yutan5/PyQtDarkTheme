"""Tests for the main program with Qt."""
import sys

import pytest

import qdarktheme


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


def test_apply_stylesheet_to_qt_app() -> None:
    """Verify that the function `load_stylesheet()` runs without error."""
    from qdarktheme.qtpy.QtCore import Qt
    from qdarktheme.qtpy.QtWidgets import QApplication

    app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore

    app.setStyleSheet(qdarktheme.load_stylesheet())


def test_apply_palette_to_qt_app() -> None:
    """Verify that the function `load_palette()` runs without error."""
    from qdarktheme.qtpy.QtCore import Qt
    from qdarktheme.qtpy.QtWidgets import QApplication

    app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore

    app.setPalette(qdarktheme.load_palette())
