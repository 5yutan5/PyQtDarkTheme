"""Package containing Qt compat."""
from .qt_compat import QtImportError
from .qt_version import __version__

try:
    from . import QtCore, QtGui, QtSvg, QtWidgets
except ImportError:
    from qdarktheme.util import get_logger as __get_logger

    __logger = __get_logger(__name__)
    __logger.warn("Cannot load QtCore, QtGui, QtSvg and QtWidgets.")
