"""Tests for the main program."""
import platform

import pytest

from qdarktheme import filter
from qdarktheme.color import Color
from qdarktheme.qtpy.qt_compat import QT_API
from qdarktheme.qtpy.qt_version import __version__

CURRENT_QT_VERSION = f'=={"10.0.0" if __version__ is None else __version__}'
ANOTHER_QT_VERSION = f'=={"6.0.0" if CURRENT_QT_VERSION == "5.15.0" else "5.15.0"}'
CURRENT_QT_API = "PySide6" if QT_API is None else QT_API
ANOTHER_QT_API = "PyQt5" if CURRENT_QT_API == "PySide6" else "PySide6"
CURRENT_OS = platform.system()
ANOTHER_OS = "Linux" if CURRENT_OS.lower() == "windows" else "windows"


@pytest.mark.parametrize(
    ("text", "output", "qt_version", "qt_api", "os_name", "expected_result"),
    [
        ("", "background: red;", None, None, None, "background: red;"),
        ("blue", "background: red;", None, None, None, "background: red;"),
        ("red", "background: ${};", None, None, None, "background: red;"),
        ("", "background: ${};", None, None, None, "background: ;"),
        ("red", "background: ${};", CURRENT_QT_VERSION, None, None, "background: red;"),
        ("red", "background: ${};", ANOTHER_QT_VERSION, None, None, ""),
        ("red", "background: ${};", None, CURRENT_QT_API, None, "background: red;"),
        ("red", "background: ${};", None, ANOTHER_QT_API, None, ""),
        ("red", "background: ${};", None, None, CURRENT_OS, "background: red;"),
        ("red", "background: ${};", None, None, ANOTHER_OS, ""),
        ("red", "background: ${};", CURRENT_QT_VERSION, CURRENT_QT_API, CURRENT_OS, "background: red;"),
        ("red", "background: ${};", ANOTHER_QT_VERSION, CURRENT_QT_API, CURRENT_OS, ""),
        ("red", "background: ${};", CURRENT_QT_VERSION, ANOTHER_QT_API, CURRENT_OS, ""),
        ("red", "background: ${};", CURRENT_QT_VERSION, CURRENT_QT_API, ANOTHER_OS, ""),
    ],
)
def test_env_filter(text, output, qt_version, qt_api, os_name, expected_result) -> None:
    """Verify that the function `_Filter.env()` runs successfully when inputting various arguments."""
    assert filter.env(text, output, qt_version, qt_api, os_name) == expected_result


@pytest.mark.parametrize(
    ("color_info", "color_state", "expected_result"),
    [
        ("#121212", None, Color.from_hex("#121212")._to_hex()),
        ({"base": "#121212"}, None, Color.from_hex("#121212")._to_hex()),
        (
            {"base": "#121212", "test state": {"transparent": 0.5}},
            "test state",
            Color.from_hex("#121212").transparent(0.5)._to_hex(),
        ),
        (
            {"base": "#121212", "test state": {"darken": 0.5}},
            "test state",
            Color.from_hex("#121212").darken(0.5)._to_hex(),
        ),
        (
            {"base": "#121212", "test state": {"lighten": 0.5}},
            "test state",
            Color.from_hex("#121212").lighten(0.5)._to_hex(),
        ),
        (
            {"base": "#121212", "test state": {"transparent": 0.5, "darken": 0.5, "lighten": 0.5}},
            "test state",
            Color.from_hex("#121212").transparent(0.5).darken(0.5).lighten(0.5)._to_hex(),
        ),
    ],
)
def test_color_filter(color_info, color_state, expected_result) -> None:
    """Verify that the function `_Filter.color()` runs successfully when inputting various arguments."""
    assert filter.color(color_info, color_state)._to_hex() == expected_result
