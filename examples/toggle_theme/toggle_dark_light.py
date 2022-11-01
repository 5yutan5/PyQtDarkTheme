"""Demonstrate a toggle dark and light theme."""
import sys

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QWidget

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
combo_box = QComboBox()


@pyqtSlot(str)
def toggle_theme(theme) -> None:
    stylesheet = qdarktheme.load_stylesheet(theme)
    QApplication.instance().setStyleSheet(stylesheet)


combo_box.addItems(qdarktheme.get_themes())
combo_box.currentTextChanged.connect(toggle_theme)

layout = QHBoxLayout()
layout.addWidget(combo_box)

central_widget = QWidget()
central_widget.setLayout(layout)
main_win.setCentralWidget(central_widget)

# Apply dark theme
app.setStyleSheet(qdarktheme.load_stylesheet())

main_win.show()

app.exec()
