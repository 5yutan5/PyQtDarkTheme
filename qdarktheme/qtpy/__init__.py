from .qt_compat import QtImportError  # noqa: F401
from .qt_version import __version__  # noqa: F401

try:
    from . import QtCore, QtGui, QtSvg, QtWidgets  # noqa: F401
except ImportError:
    pass
