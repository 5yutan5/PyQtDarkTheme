import pyqtgraph as pg
from pyqtgraph.Qt.QtGui import QMainWindow, QPushButton

import qdarktheme

app = pg.mkQApp()
qdarktheme.setup_theme()

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

pg.exec()
