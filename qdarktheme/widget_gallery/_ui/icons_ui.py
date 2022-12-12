"""The ui to show Qt standard icons."""
from __future__ import annotations

from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtWidgets import (
    QGridLayout,
    QScrollArea,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class IconsUi:
    """The ui class to show Qt standard icons."""

    def setup_ui(self, win: QWidget) -> None:
        """Set up ui."""
        widget_container = QWidget()
        layout = QGridLayout(widget_container)
        standard_pixmap_names = sorted(
            attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")
        )
        if len(standard_pixmap_names) == 0:
            standard_pixmap_names = sorted(attr for attr in dir(QStyle) if attr.startswith("SP_"))

        for i, name in enumerate(standard_pixmap_names):
            button = QToolButton()
            button.setText(f":{name}:")
            button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

            pixmap = getattr(QStyle.StandardPixmap, name)
            icon = win.style().standardIcon(pixmap)
            button.setIcon(icon)
            layout.addWidget(button, int(i / 4), i % 4)

        scroll_area = QScrollArea()
        scroll_area.setWidget(widget_container)

        v_main_layout = QVBoxLayout(win)
        v_main_layout.addWidget(scroll_area)
