import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
# Customize accent color.
qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})

main_win = QMainWindow()
main_win.setContentsMargins(10, 10, 10, 10)
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
