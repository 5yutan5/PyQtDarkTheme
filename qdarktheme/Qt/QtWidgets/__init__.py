from qdarktheme.Qt.qt_compat import QT_API

if QT_API == "PySide6":
    from PySide6.QtWidgets import *
elif QT_API == "PyQt6":
    from PyQt6.QtWidgets import *
elif QT_API == "PyQt5":
    from PyQt5.QtWidgets import *
elif QT_API == "PySide2":
    from PySide2.QtWidgets import *

    class Application(QApplication):
        def __init__(self, arg__1) -> None:
            super().__init__(arg__1)

        def exec(self) -> int:
            return super().exec_()

    QApplication = Application
