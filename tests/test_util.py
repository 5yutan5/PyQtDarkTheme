"""Test utility methods in qdarktheme/util.py."""
from qdarktheme.util import multi_replace


def test_multi_replace() -> None:
    """Test `multi_replace()`."""
    TARGET = "Dark theme for PySide and PyQt."
    EMPTY = {}
    multi_replace(TARGET, EMPTY)

    REPLACEMENTS = {"Dark": "Light", "PySide": "PyQt", "PyQt": "PySide"}
    multi_replace(TARGET, REPLACEMENTS)
