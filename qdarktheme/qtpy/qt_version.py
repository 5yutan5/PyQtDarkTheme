from typing import Optional

from .qt_compat import QT_API

__version__: Optional[str] = None
try:
    if QT_API == "PySide6":
        from PySide6 import __version__
    elif QT_API == "PyQt6":
        from PyQt6.QtCore import PYQT_VERSION_STR

        __version__ = PYQT_VERSION_STR
    elif QT_API == "PyQt5":
        from PyQt5.QtCore import PYQT_VERSION_STR

        __version__ = PYQT_VERSION_STR
    elif QT_API == "PySide2":
        from PySide2 import __version__
except ImportError:
    __version__ = None
