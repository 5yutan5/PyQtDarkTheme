"""Script capturing the image of widget_gallery."""
from __future__ import annotations

import argparse
import os
import platform
import sys
from pathlib import Path

import qdarktheme
from qdarktheme.qtpy.QtCore import Qt, QTimer, Slot
from qdarktheme.qtpy.QtGui import QGuiApplication
from qdarktheme.qtpy.QtWidgets import QApplication
from qdarktheme.widget_gallery.mainwindow import WidgetGallery


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program capture images of WidgetGallery.")
    parser.add_argument(
        "-d",
        "--dir",
        help="Output dir path",
    )
    parser.add_argument(
        "-i",
        "--identifier",
        help="Image identifier",
    )
    return parser.parse_args()


class _Application(QApplication):
    def __init__(self, img_dir_path: str | None, img_identifier: str | None) -> None:
        super().__init__(sys.argv)
        self._img_dir_path = Path("dist" if img_dir_path is None else img_dir_path)
        self._img_dir_path.mkdir(exist_ok=True)
        self._img_identifier = img_identifier

        if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
            self.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

        self._gallery = WidgetGallery()
        self._gallery.show()

    @Slot()
    def _capture_window_img(self) -> None:
        for theme in qdarktheme.get_themes():
            self.setStyleSheet(qdarktheme.load_stylesheet(theme))
            save_file_name = f"{self._img_identifier}-{theme}.png" if self._img_identifier else f"{theme}.png"

            self._gallery.setGeometry(QGuiApplication.primaryScreen().geometry())
            img_path = self._img_dir_path / save_file_name
            self._gallery.grab().save(img_path.as_posix())
        self.exit()


if __name__ == "__main__":
    if platform.system() == "Linux":
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
    args = _parse_args()

    app = _Application(args.dir, args.identifier)
    QTimer.singleShot(10, app._capture_window_img)
    app.exec()
