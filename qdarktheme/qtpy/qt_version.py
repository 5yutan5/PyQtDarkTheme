"""Module for detecting Qt version."""
from __future__ import annotations

from qdarktheme.qtpy.qt_compat import QT_API

__version__: str | None = None
if QT_API == "PySide6":
    from PySide6 import __version__  # type: ignore
elif QT_API == "PyQt6":
    from PyQt6.QtCore import PYQT_VERSION_STR  # type: ignore

    __version__ = PYQT_VERSION_STR
elif QT_API == "PyQt5":
    from PyQt5.QtCore import PYQT_VERSION_STR  # type: ignore

    __version__ = PYQT_VERSION_STR
elif QT_API == "PySide2":
    from PySide2 import __version__  # type: ignore  # noqa: F401
