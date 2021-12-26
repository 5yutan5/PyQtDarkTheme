from ..qt_compat import QT_API, qt_import_error

if QT_API is None:
    raise qt_import_error
if QT_API == "PySide6":
    from PySide6.QtGui import *  # noqa: F401, F403
elif QT_API == "PyQt6":
    from PyQt6.QtGui import *  # noqa: F401, F403
elif QT_API == "PyQt5":
    from PyQt5.QtGui import *  # noqa: F401, F403
    from PyQt5.QtWidgets import QAction, QActionGroup, QShortcut
elif QT_API == "PySide2":
    from PySide2.QtGui import *  # noqa: F401, F403
    from PySide2.QtWidgets import QAction, QActionGroup, QShortcut  # noqa: F401, F403

if QT_API in ["PyQt5", "PySide2"]:
    QAction = QAction
    QActionGroup = QActionGroup
    QShortcut = QShortcut
