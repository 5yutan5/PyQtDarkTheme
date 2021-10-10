import sys

import qdarktheme
from qdarktheme.qtpy.QtCore import Qt, QTimer
from qdarktheme.qtpy.QtWidgets import QApplication


def test_app() -> None:
    app = QApplication(sys.argv)
    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    app.setStyleSheet(qdarktheme.load_stylesheet())
    QTimer.singleShot(6000, app.exit)
    app.exec()
