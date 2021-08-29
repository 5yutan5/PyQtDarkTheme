import sys

import qdarktheme
from qdarktheme.examples.widget_gallery.mainwindow import WidgetGallery
from qdarktheme.Qt.qt_compat import QT_API
from qdarktheme.Qt.QtCore import Qt
from qdarktheme.Qt.QtWidgets import QApplication

app = QApplication(sys.argv)
# Fix the svg icon display becoming low quality in Qt5.
# Exclude PyQt6 because it doesn't have this attribute.
if QT_API != "PyQt6":
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
win = WidgetGallery()
win.menuBar().setNativeMenuBar(False)
app.setStyleSheet(qdarktheme.load_stylesheet())
win.show()
app.exec()
