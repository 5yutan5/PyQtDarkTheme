# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from typing import Any

from qdarktheme.qtpy.QtCore import QAbstractTableModel, QModelIndex, Qt
from qdarktheme.qtpy.QtGui import QIcon, QTextOption
from qdarktheme.qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QDockWidget,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSlider,
    QSpinBox,
    QSplitter,
    QTableView,
    QTabWidget,
    QTextEdit,
    QToolBox,
    QToolButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class _Group1(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 1")

        # Widgets
        group_push = QGroupBox("Push Button")
        group_tool = QGroupBox("Tool Button")
        group_radio = QGroupBox("Radio Button")
        group_checkbox = QGroupBox("Check Box")

        push_btn, push_btn_toggled = QPushButton("NORMAL"), QPushButton("TOGGLED")
        push_btn_flat, push_btn_flat_toggled = QPushButton("NORMAL"), QPushButton("TOGGLED")
        tool_btn, tool_btn_toggled, tool_btn_text = QToolButton(), QToolButton(), QToolButton()
        radio_btn_1, radio_btn_2 = QRadioButton("Normal 1"), QRadioButton("Normal 2")
        checkbox, checkbox_tristate = QCheckBox("Normal"), QCheckBox("Tristate")

        # Setup widgets
        self.setCheckable(True)
        push_btn_toggled.setCheckable(True)
        push_btn_toggled.setChecked(True)
        push_btn_flat_toggled.setCheckable(True)
        push_btn_flat_toggled.setChecked(True)
        push_btn_flat.setFlat(True)
        push_btn_flat_toggled.setFlat(True)

        tool_btn.setIcon(QIcon("icons:favorite_border_24dp.svg"))
        tool_btn_toggled.setIcon(QIcon("icons:favorite_border_24dp.svg"))
        tool_btn_text.setIcon(QIcon("icons:favorite_border_24dp.svg"))
        tool_btn_text.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        tool_btn_text.setText("Text")
        tool_btn_toggled.setCheckable(True)
        tool_btn_toggled.setChecked(True)

        radio_btn_1.setChecked(True)
        checkbox.setChecked(True)
        checkbox_tristate.setTristate(True)
        checkbox_tristate.setCheckState(Qt.CheckState.PartiallyChecked)

        # Layout
        g_layout_push = QGridLayout()
        g_layout_push.addWidget(QLabel("Normal"), 0, 0)
        g_layout_push.addWidget(push_btn, 1, 0)
        g_layout_push.addWidget(push_btn_toggled, 2, 0)
        g_layout_push.addWidget(QLabel("Flat"), 0, 1)
        g_layout_push.addWidget(push_btn_flat, 1, 1)
        g_layout_push.addWidget(push_btn_flat_toggled, 2, 1)
        group_push.setLayout(g_layout_push)

        v_layout_tool = QVBoxLayout()
        v_layout_tool.addWidget(tool_btn)
        v_layout_tool.addWidget(tool_btn_toggled)
        v_layout_tool.addWidget(tool_btn_text)
        group_tool.setLayout(v_layout_tool)

        v_layout_radio = QVBoxLayout()
        v_layout_radio.addWidget(radio_btn_1)
        v_layout_radio.addWidget(radio_btn_2)
        group_radio.setLayout(v_layout_radio)

        v_layout_checkbox = QVBoxLayout()
        v_layout_checkbox.addWidget(checkbox)
        v_layout_checkbox.addWidget(checkbox_tristate)
        group_checkbox.setLayout(v_layout_checkbox)

        g_layout_main = QGridLayout(self)
        g_layout_main.addWidget(group_push, 0, 0)
        g_layout_main.addWidget(group_tool, 0, 1)
        g_layout_main.addWidget(group_radio, 1, 0)
        g_layout_main.addWidget(group_checkbox, 1, 1)


class _Group2(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 2")
        # Widgets
        group_spinbox = QGroupBox("Spinbox")
        group_combobox = QGroupBox("Combobox")
        group_editable = QGroupBox("Line edit")
        group_date = QGroupBox("Date time edit")

        spinbox, spinbox_suffix = QSpinBox(), QSpinBox()
        combobox, combobox_line_edit = QComboBox(), QComboBox()
        lineedit = QLineEdit()
        date_time_edit, date_time_edit_calendar = QDateTimeEdit(), QDateTimeEdit()

        # Setup ui
        self.setCheckable(True)
        spinbox_suffix.setSuffix(" m")

        combobox.addItems(("Item 1", "Item 2", "Item 3"))
        combobox_line_edit.addItems(("Item 1", "Item 2", "Item 3"))
        combobox_line_edit.setEditable(True)

        lineedit.setPlaceholderText("Placeholder text")

        date_time_edit_calendar.setCalendarPopup(True)

        # Layout
        v_layout_spin = QVBoxLayout()
        v_layout_spin.addWidget(spinbox)
        v_layout_spin.addWidget(spinbox_suffix)
        group_spinbox.setLayout(v_layout_spin)

        v_layout_combo = QVBoxLayout()
        v_layout_combo.addWidget(combobox)
        v_layout_combo.addWidget(combobox_line_edit)
        group_combobox.setLayout(v_layout_combo)

        v_layout_lineedit = QVBoxLayout()
        v_layout_lineedit.addWidget(lineedit)
        group_editable.setLayout(v_layout_lineedit)

        v_layout_date = QVBoxLayout()
        v_layout_date.addWidget(date_time_edit)
        v_layout_date.addWidget(date_time_edit_calendar)
        group_date.setLayout(v_layout_date)

        g_layout_main = QGridLayout(self)
        g_layout_main.addWidget(group_spinbox, 0, 0)
        g_layout_main.addWidget(group_combobox, 0, 1)
        g_layout_main.addWidget(group_editable, 1, 0)
        g_layout_main.addWidget(group_date, 1, 1)


class _TableModel(QAbstractTableModel):
    def __init__(self) -> None:
        super().__init__()
        self._data = [[i * 10 + j for j in range(4)] for i in range(5)]

    def data(self, index: QModelIndex, role: int) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 1:
            return Qt.CheckState.Checked if index.row() % 2 == 0 else Qt.CheckState.Unchecked
        if role == Qt.ItemDataRole.EditRole and index.column() == 2:
            return self._data[index.row()][index.column()]  # pragma: no cover
        return None

    def rowCount(self, index) -> int:
        return len(self._data)

    def columnCount(self, index) -> int:
        return len(self._data[0])

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flag = super().flags(index)
        if index.column() == 1:
            flag |= Qt.ItemFlag.ItemIsUserCheckable
        elif index.column() in (2, 3):
            flag |= Qt.ItemFlag.ItemIsEditable
        return flag  # type: ignore

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return
        if orientation == Qt.Orientation.Horizontal:
            return ["Normal", "Checkbox", "Spinbox", "LineEdit"][section]
        return super().headerData(section, orientation, role)


class _Group3(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 3")

        # Widgets
        tab_widget = QTabWidget()
        tab_text_edit = QTextEdit()
        tab_table = QTableView()
        tab_list = QListWidget()
        tab_tree = QTreeWidget()

        # Setup ui
        self.setCheckable(True)
        tab_widget.setTabsClosable(True)
        tab_widget.setMovable(True)
        tab_text_edit.append("<b>PyQtDarkTheme</b>")
        tab_text_edit.append("Dark theme for PySide and PyQt.")
        tab_text_edit.append("This project is licensed under the MIT license.")
        tab_text_edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)

        tab_table.setModel(_TableModel())
        tab_table.setSortingEnabled(True)

        tab_list.addItems([f"Item {i+1}" for i in range(30)])
        tab_list.setAlternatingRowColors(True)

        tab_tree.setColumnCount(2)
        for i in range(5):
            item = QTreeWidgetItem([f"Item {i+1}" for _ in range(2)])
            for j in range(2):
                item.addChild(QTreeWidgetItem([f"Child Item {i+1}_{j+1}" for _ in range(2)]))
            tab_tree.insertTopLevelItem(i, item)

        # layout
        tab_widget.addTab(tab_table, "Table")
        tab_widget.addTab(tab_text_edit, "Text Edit")
        tab_widget.addTab(tab_list, "List")
        tab_widget.addTab(tab_tree, "Tree")

        v_layout_main = QVBoxLayout(self)
        v_layout_main.addWidget(tab_widget)


class _Group4(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 4")
        # Widgets
        toolbox = QToolBox()
        slider = QSlider(Qt.Orientation.Horizontal)
        dial_ticks = QDial()
        progressbar = QProgressBar()
        lcd_number = QLCDNumber()

        # Setup ui
        self.setCheckable(True)
        toolbox.addItem(slider, "Slider")
        toolbox.addItem(dial_ticks, "Dial")
        toolbox.addItem(progressbar, "Progress Bar")
        toolbox.addItem(lcd_number, "LCD Number")
        slider.setValue(50)
        dial_ticks.setNotchesVisible(True)
        progressbar.setValue(50)
        lcd_number.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        lcd_number.display(123)

        # Layout
        v_layout = QVBoxLayout(self)
        v_layout.addWidget(toolbox)


class HomeUI:
    def setup_ui(self, win: QWidget) -> None:
        # Widgets
        h_splitter_1, h_splitter_2 = QSplitter(Qt.Orientation.Horizontal), QSplitter(Qt.Orientation.Horizontal)

        # Setup ui
        h_splitter_1.setMinimumHeight(350)  # Fix bug layout crush

        # Layout
        h_splitter_1.addWidget(_Group1())
        h_splitter_1.addWidget(_Group2())
        h_splitter_2.addWidget(_Group3())
        h_splitter_2.addWidget(_Group4())

        v_layout = QVBoxLayout()
        v_layout.addWidget(h_splitter_1)
        v_layout.addWidget(h_splitter_2)

        widget = QWidget()
        widget.setLayout(v_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)

        v_main_layout = QVBoxLayout(win)
        v_main_layout.addWidget(scroll_area)


class DockUI:
    def setup_ui(self, main_win: QMainWindow) -> None:
        # Attribute
        left_dock = QDockWidget("Left dock")
        right_dock = QDockWidget("Right dock")
        top_dock = QDockWidget("Top dock")
        bottom_dock = QDockWidget("Bottom dock")

        # Setup ui
        left_dock.setWidget(QTextEdit("This is the left widget."))
        right_dock.setWidget(QTextEdit("This is the right widget."))
        top_dock.setWidget(QTextEdit("This is the top widget."))
        bottom_dock.setWidget(QTextEdit("This is the bottom widget."))
        for dock in (left_dock, right_dock, top_dock, bottom_dock):
            dock.setAllowedAreas(
                Qt.DockWidgetArea.LeftDockWidgetArea
                | Qt.DockWidgetArea.RightDockWidgetArea
                | Qt.DockWidgetArea.BottomDockWidgetArea
                | Qt.DockWidgetArea.TopDockWidgetArea
            )

        # Layout
        main_win.setCentralWidget(QTextEdit("This is the central widget."))
        main_win.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, left_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, right_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, top_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, bottom_dock)
