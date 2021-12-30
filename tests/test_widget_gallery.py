"""Test WidgetGallery."""
import sys

import pytest

from qdarktheme.widget_gallery.__main__ import WidgetGallery


@pytest.fixture
def widget_gallery(qtbot) -> WidgetGallery:
    """Create test instance of WidgetGallery."""
    widget_gallery = WidgetGallery()
    qtbot.add_widget(widget_gallery)
    widget_gallery.show()
    return widget_gallery


def test_widget_gallery() -> None:
    """Test WidgetGallery."""
    from qdarktheme.qtpy.QtCore import Qt, QTimer
    from qdarktheme.qtpy.QtWidgets import QApplication

    app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):  # Enable High DPI display with Qt5
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    win = WidgetGallery()
    win.show()
    QTimer.singleShot(10, app.exit)
    app.exec()


def test_widget_gallery_init(widget_gallery: WidgetGallery) -> None:
    """Ensure the widget gallery opens without error."""
    from qdarktheme.qtpy.QtCore import QTimer

    QTimer.singleShot(2000, widget_gallery.close)


def test_change_page(widget_gallery: WidgetGallery) -> None:
    """Ensure the change page UX works."""
    for action in [widget_gallery._ui.action_change_dock, widget_gallery._ui.action_change_home]:
        action.triggered.emit()


def test_toggle_state(widget_gallery: WidgetGallery) -> None:
    """Ensure the toggle state UX works."""
    for action in [widget_gallery._ui.action_enable, widget_gallery._ui.action_disable]:
        action.triggered.emit()


def test_change_theme(widget_gallery: WidgetGallery) -> None:
    """Ensure the change theme UX works."""
    for action in widget_gallery._ui.actions_theme:
        action.triggered.emit()
