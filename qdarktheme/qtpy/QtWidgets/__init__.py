"""Module for QtWidgets."""
from __future__ import annotations

from collections.abc import Sequence

from qdarktheme.qtpy.qt_compat import QT_API
from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtGui import QPalette

if QT_API == "PySide6":
    from PySide6.QtWidgets import *  # type: ignore  # noqa: F403
elif QT_API == "PyQt6":
    from PyQt6.QtWidgets import *  # type: ignore  # noqa: F403
elif QT_API == "PyQt5":
    from PyQt5.QtWidgets import *  # type: ignore # noqa: F403
elif QT_API == "PySide2":
    from PySide2.QtWidgets import *  # type: ignore  # noqa: F403


class Application(QApplication):  # type: ignore  # noqa: F405
    """Override QApplication."""

    def __init__(self, args: Sequence[str] | None = None) -> None:
        """Override QApplication method."""
        super().__init__(args)

    def exec(self) -> int:
        """Override QApplication method."""
        if hasattr(super(), "exec"):
            return super().exec()
        return super().exec_()

    def exit(self, returnCode: int = 0) -> None:  # noqa: N803
        """Override QApplication method."""
        return super().exit(returnCode)

    def setStyleSheet(self, sheet: str) -> None:  # noqa: N802
        """Override QApplication method."""
        return super().setStyleSheet(sheet)

    def setAttribute(self, attribute: Qt.ApplicationAttribute, on: bool = True) -> None:  # noqa: N802
        """Override QApplication method."""
        super().setAttribute(attribute, on)

    def setPalette(self, palette: QPalette, className: str | None = None) -> None:  # noqa: N802, N803
        """Override QApplication method."""
        super().setPalette(palette, className)


QApplication = Application
