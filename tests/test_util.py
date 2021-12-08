"""Test utility methods in qdarktheme/util.py."""
from qdarktheme.util import multireplace


def test_multireplace() -> None:
    """Test `multireplace()`."""
    TARGET = "Dark theme for PySide and PyQt."
    EMPTY = {}
    multireplace(TARGET, EMPTY)

    REPLACEMENTS = {"Dark": "Light", "PySide": "PyQt", "PyQt": "PySide"}
    multireplace(TARGET, REPLACEMENTS)
