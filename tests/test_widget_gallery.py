"""Test WidgetGallery."""
import pytest

from qdarktheme.widget_gallery.__main__ import WidgetGallery


@pytest.fixture()
def widget_gallery(qtbot) -> WidgetGallery:
    """Create test instance of WidgetGallery."""
    widget_gallery = WidgetGallery()
    qtbot.add_widget(widget_gallery)
    widget_gallery.show()
    return widget_gallery


def test_actions(widget_gallery: WidgetGallery, monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure the actions work correctly."""
    from qdarktheme.qtpy.QtWidgets import QMessageBox

    monkeypatch.setattr(QMessageBox, "question", lambda a, b, c: (a, b, c))
    monkeypatch.setattr(QMessageBox, "information", lambda a, b, c: (a, b, c))
    monkeypatch.setattr(QMessageBox, "warning", lambda a, b, c: (a, b, c))
    monkeypatch.setattr(QMessageBox, "critical", lambda a, b, c: (a, b, c))

    actions = [widget_gallery._ui.action_enable, widget_gallery._ui.action_disable]
    actions += widget_gallery._ui.actions_page
    actions += widget_gallery._ui.actions_theme
    actions += widget_gallery._ui.actions_message_box
    actions += widget_gallery._ui.actions_message_box
    for action in actions:
        action.triggered.emit()
