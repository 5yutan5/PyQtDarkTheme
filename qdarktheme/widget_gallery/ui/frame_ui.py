"""Module setting up ui of frame window."""
from qdarktheme.qtpy.QtGui import QIcon
from qdarktheme.qtpy.QtWidgets import (
    QCalendarWidget,
    QCheckBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSpinBox,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class FrameUI:
    """The ui class of frame window."""

    def setup_ui(self, win: QWidget) -> None:
        """Set up ui."""
        # Widgets
        group_box = QGroupBox("frameShape = Box")
        group_panel = QGroupBox("frameShape = Panel")
        group_none = QGroupBox("frameShape = NoFrame")
        group_line = QGroupBox("frameShape = VLine HLine")
        frame_box, frame_panel, frame_none, frame_v_line, frame_h_line = (QFrame() for _ in range(5))

        # Setup widgets
        frame_box.setFrameShape(QFrame.Shape.Box)
        frame_panel.setFrameShape(QFrame.Shape.Panel)
        frame_none.setFrameShape(QFrame.Shape.NoFrame)
        frame_v_line.setFrameShape(QFrame.Shape.VLine)
        frame_h_line.setFrameShape(QFrame.Shape.HLine)

        # Layout
        for frame in (frame_box, frame_panel, frame_none):
            push_btn_flat = QPushButton("Push button(flat)")
            push_btn_flat.setFlat(True)
            tool_btn = QToolButton()
            tool_btn.setIcon(QIcon("icons:favorite_border_24dp.svg"))
            calender = QCalendarWidget()

            g_layout = QGridLayout(frame)
            g_layout.addWidget(QPushButton("Push button"), 0, 0)
            g_layout.addWidget(push_btn_flat, 0, 1)
            g_layout.addWidget(QSpinBox(), 1, 0)
            g_layout.addWidget(tool_btn, 1, 1)
            g_layout.addWidget(QRadioButton("Radio button"), 2, 0)
            g_layout.addWidget(QCheckBox("Check box"), 2, 1)
            g_layout.addWidget(calender, 3, 0, 1, 2)

        for group, frame in ((group_box, frame_box), (group_panel, frame_panel), (group_none, frame_none)):
            v_layout = QVBoxLayout(group)
            v_layout.addWidget(frame)

        h_layout = QHBoxLayout(group_line)
        h_layout.addWidget(frame_v_line)
        h_layout.addWidget(frame_h_line)

        widget_container = QWidget()
        g_layout = QGridLayout(widget_container)
        g_layout.addWidget(group_box, 0, 0)
        g_layout.addWidget(group_panel, 0, 1)
        g_layout.addWidget(group_none, 1, 0)
        g_layout.addWidget(group_line, 1, 1)

        scroll_area = QScrollArea()
        scroll_area.setWidget(widget_container)

        v_main_layout = QVBoxLayout(win)
        v_main_layout.addWidget(scroll_area)
