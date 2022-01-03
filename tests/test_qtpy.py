"""Test for qt-compat package."""
import os
import sys

import pytest


def _clear_importing_qdarktheme() -> None:
    sys.modules.pop("qdarktheme", None)
    sys.modules.pop("qdarktheme.qtpy", None)
    sys.modules.pop("qdarktheme.qtpy.qt_compat", None)


def test_environment_variable() -> None:
    """Test QT_API of environment variable."""
    from qdarktheme.qtpy.qt_compat import _get_installed_api

    installed_qt_api = _get_installed_api()
    os.environ["QT_API"] = "PySide2" if installed_qt_api == "PySide6" else "PySide6"

    sys.modules.pop(f"{installed_qt_api}.QtCore", None)
    _clear_importing_qdarktheme()
    from qdarktheme.qtpy.qt_compat import QT_API

    assert QT_API == os.environ["QT_API"]

    del os.environ["QT_API"]
    _clear_importing_qdarktheme()


def test_wrong_QT_API() -> None:
    """Ensure if raise correct error when setting wrong qt-binding to QT_API."""
    from qdarktheme.qtpy.qt_compat import _get_installed_api

    if _get_installed_api() is not None:
        return
    os.environ["QT_API"] = "wrong_qt_api"

    _clear_importing_qdarktheme()
    with pytest.raises(KeyError) as e:
        import qdarktheme.qtpy as _  # noqa: F401

    assert e.type is KeyError

    del os.environ["QT_API"]


def test_qt_import_error() -> None:
    """Test QtImportError."""
    _clear_importing_qdarktheme()
    from qdarktheme.qtpy.qt_compat import QT_API

    if QT_API is not None:
        return
    from qdarktheme import qtpy

    with pytest.raises(qtpy.QtImportError) as e_core:
        import qdarktheme.qtpy.QtCore
    with pytest.raises(qtpy.QtImportError) as e_gui:
        import qdarktheme.qtpy.QtGui
    with pytest.raises(qtpy.QtImportError) as e_svg:
        import qdarktheme.qtpy.QtSvg
    with pytest.raises(qtpy.QtImportError) as e_widgets:
        import qdarktheme.qtpy.QtWidgets  # noqa: F401

    for e in [e_core, e_gui, e_svg, e_widgets]:
        assert e.type is qtpy.QtImportError
    _clear_importing_qdarktheme()
