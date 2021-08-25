import importlib
import os
import sys
from typing import Optional

try:
    from typing import Literal
except ImportError:  # Python 3.7 requires typing-extensions.
    from typing_extensions import Literal

# Qt6
_QT_API_PYSIDE6 = "PySide6"
_QT_API_PYQT6 = "PyQt6"
# Qt5
_QT_API_PYQT5 = "PyQt5"
_QT_API_PYSIDE2 = "PySide2"

_QT_API_ENV = os.environ.get("QT_API")
if _QT_API_ENV is not None:
    _QT_API_ENV = _QT_API_ENV.lower()

_API_TO_MODULE = {
    "pyqt6": _QT_API_PYQT6,
    "pyside6": _QT_API_PYSIDE6,
    "pyqt5": _QT_API_PYQT5,
    "pyside2": _QT_API_PYSIDE2,
    None: None,
}


def _get_loaded_api() -> Optional[Literal["PySide6", "PyQt6", "PySide2", "PyQt5"]]:
    """Return which API is loaded, if any
    If this returns anything besides None,
    importing any other Qt binding is unsafe.
    Returns
    -------
    None, 'pyside6', 'pyqt6', 'pyside2', 'pyqt5'
    """
    if sys.modules.get("PySide6.QtCore"):
        return _QT_API_PYSIDE6
    elif sys.modules.get("PyQt6.QtCore"):
        return _QT_API_PYQT6
    elif sys.modules.get("PyQt5.QtCore"):
        return _QT_API_PYQT5
    elif sys.modules.get("PySide2.QtCore"):
        return _QT_API_PYSIDE2
    elif _QT_API_ENV is None:
        return None
    elif _QT_API_ENV is not None:
        try:
            return _API_TO_MODULE[_QT_API_ENV]
        except KeyError:
            raise RuntimeError(
                "The environment variable QT_API has the unrecognized value "
                f"{_QT_API_ENV!r}; "
                f"valid values are {set(k for k in _API_TO_MODULE if k is not None)}"
            ) from None
    return None


def _get_installed_api() -> Optional[Literal["PySide6", "PyQt6", "PySide2", "PyQt5"]]:
    if importlib.util.find_spec(_QT_API_PYSIDE6) is not None:  # type: ignore
        return _QT_API_PYSIDE6
    elif importlib.util.find_spec(_QT_API_PYQT6) is not None:  # type: ignore
        return _QT_API_PYQT6
    elif importlib.util.find_spec(_QT_API_PYQT5) is not None:  # type: ignore
        return _QT_API_PYQT5
    elif importlib.util.find_spec(_QT_API_PYSIDE6) is not None:  # type: ignore
        return _QT_API_PYSIDE2
    return None


QT_API = _get_loaded_api()
if QT_API is None:
    QT_API = _get_installed_api()
if QT_API is None:
    raise ImportError(
        "\n================================================================"
        "\nFailed to import qt-binding."
        "\nCheck that the module is installed.(pip list)"
        "\nThe supported qt-binding modules: PySide6, PyQt6, PyQt5, PySide2"
        "\n================================================================"
    )
