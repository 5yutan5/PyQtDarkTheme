import sys

from PyQt6.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QWidget

import qdarktheme

app = QApplication(sys.argv)
qdarktheme.setup_theme("dark")

main_win = QMainWindow()

combo_box = QComboBox()
combo_box.addItems(qdarktheme.get_themes())
combo_box.currentTextChanged.connect(qdarktheme.setup_theme)

layout = QHBoxLayout()
layout.addWidget(combo_box)

central_widget = QWidget()
central_widget.setLayout(layout)
main_win.setCentralWidget(central_widget)

main_win.show()

app.exec()
