import sys

import qdarktheme
from qdarktheme.examples.widget_gallery.mainwindow import WidgetGallery
from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtWidgets import QApplication

app = QApplication(sys.argv)
# Fix the svg icon display becoming low quality in Qt5.
# PyQt6 doesn't have this attribute.
if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
win = WidgetGallery()
win.menuBar().setNativeMenuBar(False)
app.setStyleSheet(qdarktheme.load_stylesheet())
win.show()
app.exec()
