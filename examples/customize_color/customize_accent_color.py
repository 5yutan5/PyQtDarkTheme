"""This example demonstrates customizing accent color."""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
main_win.setContentsMargins(10, 10, 10, 10)
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

# Customize accent color.
app.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

main_win.show()

app.exec()
