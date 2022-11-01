"""This example demonstrates to sync system theme."""
import sys

import darkdetect
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
theme_label = QLabel()

main_win.setCentralWidget(theme_label)


@Slot()
def sync_theme_with_system() -> None:
    theme = darkdetect.theme().lower()
    # Return None if darkdetect fails to detect a theme.
    if theme is None:
        theme = "dark"
    theme_label.setText(f"Theme: {theme}")
    stylesheet = qdarktheme.load_stylesheet(theme)
    QApplication.instance().setStyleSheet(stylesheet)


app.paletteChanged.connect(sync_theme_with_system)
sync_theme_with_system()

main_win.show()

app.exec()
