import sys

import qdarktheme
from qdarktheme.designer_supporter.mainwindow import MainDialog
from qdarktheme.qtpy.QtWidgets import QApplication

app = QApplication(sys.argv)
main_win = MainDialog()
main_win.show()
app.setStyleSheet(qdarktheme.load_stylesheet())
app.exec()
