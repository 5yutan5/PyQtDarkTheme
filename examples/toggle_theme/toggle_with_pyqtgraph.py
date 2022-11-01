"""Demonstrate a toggle dark and light theme with PyQtGraph."""
import sys

import pyqtgraph as pg
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow, QVBoxLayout, QWidget

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
combo_box = QComboBox()
plot_widget = pg.PlotWidget()


@Slot(str)
def toggle_theme(theme) -> None:
    stylesheet = qdarktheme.load_stylesheet(theme)
    QApplication.instance().setStyleSheet(stylesheet)
    plot_widget.setBackground("k" if theme == "dark" else "w")


combo_box.addItems(qdarktheme.get_themes())
combo_box.currentTextChanged.connect(toggle_theme)

layout = QVBoxLayout()
layout.addWidget(combo_box)
layout.addWidget(plot_widget)

central_widget = QWidget()
central_widget.setLayout(layout)
main_win.setCentralWidget(central_widget)

# Apply dark theme
app.setStyleSheet(qdarktheme.load_stylesheet())

main_win.show()

app.exec()
