import sys

import qdarktheme
from qdarktheme.qtpy.QtCore import Qt, QTimer
from qdarktheme.qtpy.QtWidgets import QApplication

THEMES = ["dark", "light"]


def test_app() -> None:
    app = QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    for theme in THEMES:
        app.setStyleSheet(qdarktheme.load_stylesheet(theme))
        app.setPalette(qdarktheme.load_palette(theme))
    QTimer.singleShot(6000, app.exit)
    app.exec()


def test_load_stylesheet() -> None:
    for theme in THEMES:
        qdarktheme.load_stylesheet(theme)


def test_load_palette() -> None:
    for theme in THEMES:
        qdarktheme.load_palette(theme)
