"""Test module for freezing-package."""
import sys

import qdarktheme
from qdarktheme.qtpy.QtCore import QTimer
from qdarktheme.qtpy.QtWidgets import QApplication, QCheckBox, QMainWindow, QVBoxLayout, QWidget


def _main() -> None:
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    push_button = QCheckBox("Test")
    central_widget = QWidget()

    v_layout = QVBoxLayout(central_widget)
    v_layout.addWidget(push_button)
    main_win.setCentralWidget(central_widget)

    app.setStyleSheet(qdarktheme.load_stylesheet())

    main_win.show()
    QTimer.singleShot(10, app.exit)

    app.exec()


if __name__ == "__main__":
    _main()
