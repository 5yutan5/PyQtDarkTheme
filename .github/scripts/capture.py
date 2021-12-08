"""Script capturing the image of widget_gallery."""
import sys

import qdarktheme
from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtGui import QGuiApplication
from qdarktheme.qtpy.QtWidgets import QApplication
from qdarktheme.widget_gallery.mainwindow import WidgetGallery

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    for theme in qdarktheme.THEMES:
        app.setStyleSheet(qdarktheme.load_stylesheet(theme))
        save_file_name = f"{sys.argv[1]}-{theme}.png" if len(sys.argv) >= 2 else f"{theme}.png"

        gallery = WidgetGallery()
        gallery.setGeometry(QGuiApplication.primaryScreen().geometry())
        gallery.grab().save(save_file_name)
