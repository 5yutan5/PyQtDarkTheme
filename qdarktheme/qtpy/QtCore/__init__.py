from ..qt_compat import QT_API, qt_import_error

if QT_API is None:
    raise qt_import_error
if QT_API == "PySide6":
    from PySide6.QtCore import *
elif QT_API == "PyQt6":
    from PyQt6.QtCore import *

    Slot = pyqtSlot  # noqa: F405
    Signal = pyqtSignal  # noqa: F405
elif QT_API == "PyQt5":
    from PyQt5.QtCore import *

    Slot = pyqtSlot  # noqa: F405
    Signal = pyqtSignal  # noqa: F405
elif QT_API == "PySide2":
    from PySide2.QtCore import *
