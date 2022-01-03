"""Package containing Qt compat."""
from qdarktheme.qtpy.qt_compat import QtImportError
from qdarktheme.qtpy.qt_version import __version__

try:
    from qdarktheme.qtpy import QtCore, QtGui, QtSvg, QtWidgets
except ImportError:
    from qdarktheme.util import get_logger as __get_logger

    __logger = __get_logger(__name__)
    __logger.warning("Failed to import QtCore, QtGui, QtSvg and QtWidgets.")
