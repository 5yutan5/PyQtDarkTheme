from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtGui import QTextOption
from qdarktheme.qtpy.QtWidgets import (
    QCheckBox,
    QComboBox,
    QCommandLinkButton,
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
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QToolBox,
    QToolButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
from qdarktheme.icon_manager import get_icon


class HomeUI:
    def setup_ui(self, win: QWidget) -> None:
        h_splitter_1, h_splitter_2 = QSplitter(Qt.Orientation.Horizontal), QSplitter(Qt.Orientation.Horizontal)

        # layout
        h_splitter_1.addWidget(_Group1())
        h_splitter_1.addWidget(_Group2())
        h_splitter_2.addWidget(_Group3())
        h_splitter_2.addWidget(_Group4())

        # Fix bug layout crush
        h_splitter_1.setMinimumHeight(370)

        v_layout = QVBoxLayout()
        v_layout.addWidget(h_splitter_1)
        v_layout.addWidget(h_splitter_2)

        widget = QWidget()
        widget.setLayout(v_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)

        v_main_layout = QVBoxLayout(win)
        v_main_layout.addWidget(scroll_area)


class _Group1(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 1")
        # Attribute
        group_push = QGroupBox("Push Button")
        group_tool = QGroupBox("Tool Button")
        group_radio = QGroupBox("Radio Button")
        group_command_link = QGroupBox("Command Link Button")
        group_checkbox = QGroupBox("Check Box")

        push_button_normal = QPushButton(text="NORMAL")
        push_button_toggled = QPushButton(text="TOGGLED")
        push_button_icon = QPushButton(icon=get_icon("favorite_border"), text="ICON")

        push_button_contained_normal = QPushButton(text="NORMAL")
        push_button_contained_toggled = QPushButton(text="TOGGLED")
        push_button_contained_icon = QPushButton(icon=get_icon("favorite_border"), text="ICON")

        push_button_text_normal = QPushButton(text="NORMAL")
        push_button_text_toggled = QPushButton(text="TOGGLED")
        push_button_text_icon = QPushButton(icon=get_icon("favorite_border"), text="ICON")

        tool_button_normal, tool_button_toggled, tool_button_text = QToolButton(), QToolButton(), QToolButton()

        radio_button_normal_1, radio_button_normal_2 = QRadioButton("Normal 1"), QRadioButton("Normal 2")

        command_link_button = QCommandLinkButton("NORMAL")

        checkbox_normal, checkbox_tristate = QCheckBox("Normal"), QCheckBox("Tristate")

        # setup widgets
        self.setCheckable(True)
        push_button_toggled.setCheckable(True)
        push_button_toggled.setChecked(True)
        push_button_contained_toggled.setCheckable(True)
        push_button_contained_toggled.setChecked(True)
        push_button_text_toggled.setCheckable(True)
        push_button_text_toggled.setChecked(True)

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

        # setup qss property
        push_button_contained_normal.setProperty("type", "contained")
        push_button_contained_toggled.setProperty("type", "contained")
        push_button_contained_icon.setProperty("type", "contained")
        push_button_text_normal.setProperty("type", "text")
        push_button_text_toggled.setProperty("type", "text")
        push_button_text_icon.setProperty("type", "text")

        # layout
        g_layout_push = QGridLayout()
        g_layout_push.addWidget(QLabel("Outlined"), 0, 0)
        g_layout_push.addWidget(push_button_normal, 1, 0)
        g_layout_push.addWidget(push_button_toggled, 2, 0)
        g_layout_push.addWidget(push_button_icon, 3, 0)
        g_layout_push.addWidget(QLabel("Contained"), 0, 1)
        g_layout_push.addWidget(push_button_contained_normal, 1, 1)
        g_layout_push.addWidget(push_button_contained_toggled, 2, 1)
        g_layout_push.addWidget(push_button_contained_icon, 3, 1)
        g_layout_push.addWidget(QLabel("Text"), 0, 2)
        g_layout_push.addWidget(push_button_text_normal, 1, 2)
        g_layout_push.addWidget(push_button_text_toggled, 2, 2)
        g_layout_push.addWidget(push_button_text_icon, 3, 2)
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

        v_layout_command = QVBoxLayout()
        v_layout_command.addWidget(command_link_button)
        group_command_link.setLayout(v_layout_command)

        v_layout_checkbox = QVBoxLayout()
        v_layout_checkbox.addWidget(checkbox_normal)
        v_layout_checkbox.addWidget(checkbox_tristate)
        group_checkbox.setLayout(v_layout_checkbox)

        g_layout_main = QGridLayout(self)
        g_layout_main.addWidget(group_push, 0, 0, 2, 1)
        g_layout_main.addWidget(group_tool, 0, 1)
        g_layout_main.addWidget(group_command_link, 1, 1, 2, 1)
        g_layout_main.addWidget(group_radio, 2, 0, 2, 1)
        g_layout_main.addWidget(group_checkbox, 3, 1)


class _Group2(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 2")
        # Attribute
        group_spinbox = QGroupBox("Spinbox")
        group_combobox = QGroupBox("Combobox")
        group_editable = QGroupBox("Line edit")
        group_date = QGroupBox("Date time edit")

        spinbox_normal, spinbox_suffix = QSpinBox(), QSpinBox()

        combobox_normal, combobox_line_edit = QComboBox(), QComboBox()

        lineedit_normal, lineedit_warning, lineedit_error = QLineEdit(), QLineEdit(), QLineEdit()

        date_time_edit_normal, date_time_edit_calendar = QDateTimeEdit(), QDateTimeEdit()

        # setup widget
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

        # setup qss property
        lineedit_warning.setProperty("state", "warning")
        lineedit_error.setProperty("state", "error")

        # layout
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


class _Group3(QGroupBox):
    def __init__(self) -> None:
        super().__init__("Group 3")

        # Attribute
        tab_widget = QTabWidget()
        tab_text_edit = QTextEdit()
        tab_table = QTableWidget(5, 5)
        tab_list = QListWidget()
        tab_tree = QTreeWidget()

        # ui
        self.setCheckable(True)
        tab_widget.setTabsClosable(True)
        tab_text_edit.append("<b>QMaterialStyleSheet</b>")
        tab_text_edit.append("A material style sheet for QtWidgets application(Qt for python).")
        tab_text_edit.append("This project is licensed under the MIT license.")
        tab_text_edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)

        count = 0
        for row in range(5):
            for column in range(5):
                count += 1
                tab_table.setItem(row, column, QTableWidgetItem(str(count)))
        tab_table.setSortingEnabled(True)

        tab_list.addItems([f"Item {i+1}" for i in range(30)])
        tab_list.setAlternatingRowColors(True)

        tab_tree.setColumnCount(2)
        tree_widget_items = []
        for i in range(10):
            tree_widget_item = QTreeWidgetItem([f"Item {i+1}" for _ in range(2)])
            for j in range(2):
                tree_widget_child_item = QTreeWidgetItem([f"Child Item {i+1}_{j+1}" for _ in range(2)])
                for k in range(3):
                    tree_widget_grandchild_item = QTreeWidgetItem(
                        [f"Grand Child Item {i+1}_{j+1}_{k+1}" for _ in range(2)]
                    )
                    tree_widget_child_item.addChild(tree_widget_grandchild_item)
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
        # Attribute
        toolbox = QToolBox()
        slider = QSlider(Qt.Orientation.Horizontal)
        dial_ticks = QDial()
        progressbar = QProgressBar()
        lcd_number = QLCDNumber()

        # ui
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

        # layout
        v_layout = QVBoxLayout(self)
        v_layout.addWidget(toolbox)
