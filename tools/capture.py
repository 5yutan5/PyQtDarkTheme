"""Script capturing the image of widget_gallery."""
from __future__ import annotations

import argparse
import os
import platform
import sys

import qdarktheme
from qdarktheme.qtpy.QtCore import QTimer, Slot
from qdarktheme.qtpy.QtGui import QGuiApplication
from qdarktheme.qtpy.QtWidgets import QApplication
from qdarktheme.widget_gallery.main_window import WidgetGallery


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program capture images of WidgetGallery.")
    parser.add_argument("--name", help="Image name")
    return parser.parse_args()


class _Application(QApplication):
    def __init__(self, img_name: str) -> None:
        super().__init__(sys.argv)
        self._img_name = img_name.replace("~=", "-")
        self._gallery = WidgetGallery()
        self._gallery.show()

    @Slot()
    def _capture_window_img(self) -> None:
        for theme in qdarktheme.get_themes():
            qdarktheme.setup_style(theme)
            self._gallery.setGeometry(QGuiApplication.primaryScreen().geometry())
            self._gallery.grab().save(f"{self._img_name}-{theme}.png")
        self.exit()


if __name__ == "__main__":
    if platform.system() == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = _Application(_parse_args().name)
    QTimer.singleShot(10, app._capture_window_img)
    app.exec()
