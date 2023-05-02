import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
# Change border corner shape to sharp.
qdarktheme.setup_theme(corner_shape="sharp")

main_win = QMainWindow()
main_win.setContentsMargins(10, 10, 10, 10)
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
