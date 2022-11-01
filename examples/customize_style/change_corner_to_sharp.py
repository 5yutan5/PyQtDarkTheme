"""This example demonstrates to change corner shape to sharp."""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
main_win.setContentsMargins(10, 10, 10, 10)
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

# Change border corner shape to sharp.
app.setStyleSheet(qdarktheme.load_stylesheet(corner_shape="sharp"))

main_win.show()

app.exec()
