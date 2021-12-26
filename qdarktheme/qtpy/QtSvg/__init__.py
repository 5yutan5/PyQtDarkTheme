from ..qt_compat import QT_API, qt_import_error

if QT_API is None:
    raise qt_import_error
if QT_API == "PySide6":
    from PySide6.QtSvg import *  # noqa: F401, F403
elif QT_API == "PyQt6":
    from PyQt6.QtSvg import *  # noqa: F401, F403
elif QT_API == "PyQt5":
    from PyQt5.QtSvg import *  # noqa: F401, F403
elif QT_API == "PySide2":
    from PySide2.QtSvg import *  # noqa: F401, F403
