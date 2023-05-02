import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

# Enable HiDPI.
qdarktheme.enable_hi_dpi()

app = QApplication(sys.argv)
# Apply dark theme.
qdarktheme.setup_theme()

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec_()
