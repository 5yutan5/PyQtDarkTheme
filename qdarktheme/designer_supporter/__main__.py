import sys

import qdarktheme
from qdarktheme.designer_supporter.mainwindow import MainDialog
from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtWidgets import QApplication

app = QApplication(sys.argv)
# Fix the svg icon display becoming low quality in Qt5.
# PyQt6 doesn't have this attribute.
if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
main_win = MainDialog()
main_win.show()
app.setStyleSheet(qdarktheme.load_stylesheet())
app.exec()
