import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
qdarktheme.setup_theme("auto")

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
