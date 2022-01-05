"""Test utility methods in qdarktheme/util.py."""
from qdarktheme.util import multi_replace


def test_multi_replace() -> None:
    """Test `multi_replace()`."""
    target = "Dark theme for PySide and PyQt."
    empty = {}
    multi_replace(target, empty)

    replacements = {"Dark": "Light", "PySide": "PyQt", "PyQt": "PySide"}
    multi_replace(target, replacements)
