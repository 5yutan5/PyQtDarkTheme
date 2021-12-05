"""Script capturing the image of widget_gallery."""
import sys
from importlib import resources

import qdarktheme
from qdarktheme.qtpy.QtCore import QDir, Qt
from qdarktheme.qtpy.QtGui import QGuiApplication
from qdarktheme.qtpy.QtWidgets import QApplication
from qdarktheme.util import get_project_root_path
from qdarktheme.widget_gallery.__main__ import WidgetGallery

app = QApplication(sys.argv)
if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
QDir.addSearchPath("icons", f"{get_project_root_path().as_posix()}/widget_gallery/ui/svg")

for contents in resources.contents("builder.theme"):
    if ".json" not in contents or "validate.json" in contents:
        continue
    theme = contents.replace(".json", "")
    app.setStyleSheet(qdarktheme.load_stylesheet(theme))

    save_file_name = f"{sys.argv[1]}-{theme}.jpg" if len(sys.argv) >= 2 else f"{theme}.jpg"

    gallery = WidgetGallery()
    gallery.setGeometry(QGuiApplication.primaryScreen().geometry())
    gallery.grab().save(save_file_name)
