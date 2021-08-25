from qdarktheme.Qt.qt_compat import QT_API

if QT_API == "PySide6":
    from PySide6.QtSvg import *
elif QT_API == "PyQt6":
    from PyQt6.QtSvg import *
elif QT_API == "PyQt5":
    from PyQt5.QtSvg import *
elif QT_API == "PySide2":
    from PySide2.QtSvg import *
