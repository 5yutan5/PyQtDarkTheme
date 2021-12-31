"""Module for QtWidgets."""
from __future__ import annotations

from typing import Sequence

from ..qt_compat import QT_API
from ..QtCore import Qt
from ..QtGui import QPalette

if QT_API == "PySide6":
    from PySide6.QtWidgets import *  # noqa: F403
elif QT_API == "PyQt6":
    from PyQt6.QtWidgets import *  # noqa: F403
elif QT_API == "PyQt5":
    from PyQt5.QtWidgets import *  # noqa: F403
elif QT_API == "PySide2":
    from PySide2.QtWidgets import *  # noqa: F403


class Application(QApplication):  # noqa: F405
    """Override QApplication."""

    def __init__(self, args: Sequence[str] = None) -> None:
        """Override QApplication method."""
        super().__init__(args)

    def exec(self) -> int:
        """Override QApplication method."""
        if hasattr(super(), "exec_"):
            return super().exec_()
        return super().exec()

    def exit(self, returnCode: int = 0) -> None:
        """Override QApplication method."""
        return super().exit(returnCode)

    def setStyleSheet(self, sheet: str) -> None:
        """Override QApplication method."""
        return super().setStyleSheet(sheet)

    def setAttribute(self, attribute: Qt.ApplicationAttribute, on: bool = True) -> None:
        """Override QApplication method."""
        super().setAttribute(attribute, on)

    def setPalette(self, palette: QPalette, className: str = None) -> None:
        """Override QApplication method."""
        super().setPalette(palette, className)


QApplication = Application
