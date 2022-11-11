"""This example demonstrates to sync system theme."""
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
theme_label = QLabel()

main_win.setCentralWidget(theme_label)


@Slot()
def sync_theme_with_system() -> None:
    stylesheet = qdarktheme.load_stylesheet("auto")
    QApplication.instance().setStyleSheet(stylesheet)


app.paletteChanged.connect(sync_theme_with_system)
sync_theme_with_system()

main_win.show()

app.exec()
