import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
# Additional stylesheet
qss = """
QPushButton {
    border-width: 2px;
    border-style: dashed;
}
"""
qdarktheme.setup_theme(additional_qss=qss)

main_win = QMainWindow()
main_win.setContentsMargins(10, 10, 10, 10)
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
