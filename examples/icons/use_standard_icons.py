import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle

import qdarktheme

app = QApplication(sys.argv)
qdarktheme.setup_theme()

main_win = QMainWindow()
save_pixmap = QStyle.StandardPixmap.SP_DialogSaveButton
save_icon = main_win.style().standardIcon(save_pixmap)

push_button = QPushButton("Save")
push_button.setIcon(save_icon)
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
