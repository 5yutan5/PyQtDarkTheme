from typing import Any

from qdarktheme.qtpy.QtCore import QAbstractTableModel, QModelIndex, Qt
from qdarktheme.qtpy.QtGui import QTextOption
from qdarktheme.qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
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
from qdarktheme.widget_gallery.icon_manager import get_icon


class _Group1(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 1")

        # Widgets
        group_push = QGroupBox("Push Button")
        group_tool = QGroupBox("Tool Button")
        group_radio = QGroupBox("Radio Button")
        group_checkbox = QGroupBox("Check Box")

        push_button_normal = QPushButton(text="NORMAL")
        push_button_toggled = QPushButton(text="TOGGLED")
        push_button_flat_normal = QPushButton(text="NORMAL")
        push_button_flat_toggled = QPushButton(text="TOGGLED")
        tool_button_normal, tool_button_toggled, tool_button_text = QToolButton(), QToolButton(), QToolButton()
        radio_button_normal_1, radio_button_normal_2 = QRadioButton("Normal 1"), QRadioButton("Normal 2")
        checkbox_normal, checkbox_tristate = QCheckBox("Normal"), QCheckBox("Tristate")

        # Setup widgets
        self.setCheckable(True)
        push_button_toggled.setCheckable(True)
        push_button_toggled.setChecked(True)
        push_button_flat_toggled.setCheckable(True)
        push_button_flat_toggled.setChecked(True)
        push_button_flat_normal.setFlat(True)
        push_button_flat_toggled.setFlat(True)

        tool_button_normal.setIcon(get_icon("favorite_border"))
        tool_button_toggled.setIcon(get_icon("favorite_border"))
        tool_button_text.setIcon(get_icon("favorite_border"))
        tool_button_text.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        tool_button_text.setText("Text")
        tool_button_toggled.setCheckable(True)
        tool_button_toggled.setChecked(True)

        radio_button_normal_1.setChecked(True)
        checkbox_normal.setChecked(True)
        checkbox_tristate.setTristate(True)
        checkbox_tristate.setCheckState(Qt.CheckState.PartiallyChecked)

        # Layout
        g_layout_push = QGridLayout()
        g_layout_push.addWidget(QLabel("Normal"), 0, 0)
        g_layout_push.addWidget(push_button_normal, 1, 0)
        g_layout_push.addWidget(push_button_toggled, 2, 0)
        g_layout_push.addWidget(QLabel("Flat"), 0, 1)
        g_layout_push.addWidget(push_button_flat_normal, 1, 1)
        g_layout_push.addWidget(push_button_flat_toggled, 2, 1)
        group_push.setLayout(g_layout_push)

        v_layout_tool = QVBoxLayout()
        v_layout_tool.addWidget(tool_button_normal)
        v_layout_tool.addWidget(tool_button_toggled)
        v_layout_tool.addWidget(tool_button_text)
        group_tool.setLayout(v_layout_tool)

        v_layout_radio = QVBoxLayout()
        v_layout_radio.addWidget(radio_button_normal_1)
        v_layout_radio.addWidget(radio_button_normal_2)
        group_radio.setLayout(v_layout_radio)

        v_layout_checkbox = QVBoxLayout()
        v_layout_checkbox.addWidget(checkbox_normal)
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

        spinbox_normal, spinbox_suffix = QSpinBox(), QSpinBox()
        combobox_normal, combobox_line_edit = QComboBox(), QComboBox()
        lineedit_normal, lineedit_warning, lineedit_error = QLineEdit(), QLineEdit(), QLineEdit()
        date_time_edit_normal, date_time_edit_calendar = QDateTimeEdit(), QDateTimeEdit()

        # Setup ui
        self.setCheckable(True)
        spinbox_suffix.setSuffix(" m")

        texts = ["Item 1", "Item 2", "Item 3"]
        combobox_normal.addItems(texts)
        combobox_line_edit.addItems(texts)
        combobox_line_edit.setEditable(True)

        lineedit_normal.setPlaceholderText("Normal")
        lineedit_warning.setPlaceholderText("Warning")
        lineedit_error.setPlaceholderText("Error")

        date_time_edit_calendar.setCalendarPopup(True)

        # Setup qss property
        lineedit_warning.setProperty("state", "warning")
        lineedit_error.setProperty("state", "error")

        # Layout
        v_layout_spin = QVBoxLayout()
        v_layout_spin.addWidget(spinbox_normal)
        v_layout_spin.addWidget(spinbox_suffix)
        group_spinbox.setLayout(v_layout_spin)

        v_layout_combo = QVBoxLayout()
        v_layout_combo.addWidget(combobox_normal)
        v_layout_combo.addWidget(combobox_line_edit)
        group_combobox.setLayout(v_layout_combo)

        v_layout_lineedit = QVBoxLayout()
        v_layout_lineedit.addWidget(lineedit_normal)
        v_layout_lineedit.addWidget(lineedit_warning)
        v_layout_lineedit.addWidget(lineedit_error)
        group_editable.setLayout(v_layout_lineedit)

        v_layout_date = QVBoxLayout()
        v_layout_date.addWidget(date_time_edit_normal)
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
        self._checks = [True if i % 2 == 0 else False for i in range(5)]

    def data(self, index: QModelIndex, role: int) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.ItemDataRole.CheckStateRole and index.column() == 1:
            return Qt.CheckState.Checked if self._checks[index.row()] else Qt.CheckState.Unchecked
        elif role == Qt.ItemDataRole.EditRole and index.column() == 2:
            return self._data[index.row()][index.column()]

    def rowCount(self, index: QModelIndex) -> int:
        return len(self._data)

    def columnCount(self, index: QModelIndex) -> int:
        return len(self._data[0])

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flag = super().flags(index)
        if index.column() == 1:
            flag |= Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsUserCheckable
            return flag
        elif index.column() == 2:
            flag |= Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable
            return flag
        elif index.column() == 3:
            flag |= Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable
        return flag

    def setData(self, index: QModelIndex, value: Any, role: int) -> bool:
        if role == Qt.ItemDataRole.CheckStateRole:
            self._checks[index.row()] = True if value == Qt.CheckState.Checked else False
            return True
        return False

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
        tab_text_edit.append("<b>QtVSCodeStyle</b>")
        tab_text_edit.append("VS Code style for QtWidgets application(Qt for python).")
        tab_text_edit.append("This project is licensed under the MIT license.")
        tab_text_edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)

        tab_table.setModel(_TableModel())
        tab_table.setSortingEnabled(True)

        tab_list.addItems([f"Item {i+1}" for i in range(30)])
        tab_list.setAlternatingRowColors(True)

        tab_tree.setColumnCount(2)
        tree_widget_items = []
        for i in range(5):
            tree_widget_item = QTreeWidgetItem([f"Item {i+1}" for _ in range(2)])
            for j in range(2):
                tree_widget_child_item = QTreeWidgetItem([f"Child Item {i+1}_{j+1}" for _ in range(2)])
                tree_widget_item.addChild(tree_widget_child_item)
            tree_widget_items.append(tree_widget_item)
        tab_tree.addTopLevelItems(tree_widget_items)

        # layout
        tab_widget.addTab(tab_text_edit, "Text Edit")
        tab_widget.addTab(tab_table, "Table")
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
