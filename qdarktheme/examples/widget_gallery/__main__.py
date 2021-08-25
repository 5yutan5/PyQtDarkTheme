import sys

import qdarktheme
from qdarktheme.examples.widget_gallery.mainwindow import WidgetGallery
from qdarktheme.Qt.QtWidgets import QApplication

app = QApplication(sys.argv)
win = WidgetGallery()
win.menuBar().setNativeMenuBar(False)
app.setStyleSheet(qdarktheme.load_stylesheet())
win.show()
app.exec()
