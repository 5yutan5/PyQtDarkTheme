from ..qt_compat import QT_API

if QT_API == "PySide6":
    from PySide6.QtGui import *
elif QT_API == "PyQt6":
    from PyQt6.QtGui import *
elif QT_API == "PyQt5":
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import QAction, QActionGroup
elif QT_API == "PySide2":
    from PySide2.QtGui import *