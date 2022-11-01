"""This example demonstrates applying dark theme to PyQtGraph."""
import pyqtgraph as pg
from pyqtgraph.Qt.QtGui import QMainWindow, QPushButton

import qdarktheme

app = pg.mkQApp()
main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

# Apply dark theme
app.setStyleSheet(qdarktheme.load_stylesheet())

main_win.show()

pg.exec()
