import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

qdarktheme.enable_hi_dpi()

app = QApplication(sys.argv)
qdarktheme.setup_theme()

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
