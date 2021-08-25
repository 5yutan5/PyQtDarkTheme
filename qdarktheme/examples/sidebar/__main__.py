import sys

import qdarktheme
from qdarktheme.Qt.QtCore import Qt
from qdarktheme.Qt.QtGui import QAction, QActionGroup
from qdarktheme.Qt.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget, QToolBar
from qdarktheme.resource_manager import get_icon

app = QApplication(sys.argv)
main_win = QMainWindow()

# Create action
action_move_page_1 = QAction(get_icon("home"), "Move Page 1")
action_move_page_2 = QAction(get_icon("favorite_border"), "Move Page2")
action_move_page_1.setCheckable(True)
action_move_page_2.setCheckable(True)
action_move_page_1.setChecked(True)
action_group = QActionGroup(main_win)
action_group.addAction(action_move_page_1)
action_group.addAction(action_move_page_2)
action_group.setExclusive(True)

# Create pages
page_1 = QLabel("Page 1")
page_2 = QLabel("Page 2")

# Create stack widget
stack_widget = QStackedWidget()
stack_widget.addWidget(page_1)
stack_widget.addWidget(page_2)
stack_widget.setMinimumSize(300, 300)

# Create sidebar============================================
sidebar = QToolBar()
sidebar.addActions([action_move_page_1, action_move_page_2])
sidebar.setMovable(False)
sidebar.setProperty("type", "sidebar")
# ==========================================================

# Setup Singal
action_move_page_1.triggered.connect(lambda: stack_widget.setCurrentIndex(0))
action_move_page_2.triggered.connect(lambda: stack_widget.setCurrentIndex(1))

main_win.addToolBar(Qt.ToolBarArea.LeftToolBarArea, sidebar)
main_win.setCentralWidget(stack_widget)

app.setStyleSheet(qdarktheme.load_stylesheet())
main_win.show()
app.exec()
