"""Test utility methods in qdarktheme/util.py."""
from qdarktheme.util import analyze_version_str, multi_replace


def test_multi_replace() -> None:
    """Test `multi_replace()`."""
    target = "Dark theme for PySide and PyQt."
    empty = {}
    multi_replace(target, empty)

    replacements = {"Dark": "Light", "PySide": "PyQt", "PyQt": "PySide"}
    multi_replace(target, replacements)


def test_analyze_version_str() -> None:
    """Test `analyze_version_str()`."""
    # Test "=="
    assert analyze_version_str(target_version="5.0.0", version_text="==5.0.0")
    assert not analyze_version_str(target_version="5.1.2", version_text="==5.0.0")
    # Test "!="
    assert analyze_version_str(target_version="5.0.0", version_text="!=6.0.1")
    assert not analyze_version_str(target_version="6.0.1", version_text="!=6.0.1")
    # Test ">="
    assert analyze_version_str(target_version="5.12.0", version_text=">=5.10.5")
    assert analyze_version_str(target_version="5.10.5", version_text=">=5.10.5")
    assert not analyze_version_str(target_version="5.9.1", version_text=">=5.10.5")
    # Test ">"
    assert analyze_version_str(target_version="5.12.0", version_text=">5.10.5")
    assert not analyze_version_str(target_version="5.10.5", version_text=">5.10.5")
    assert not analyze_version_str(target_version="5.9.1", version_text=">5.10.5")
    # Test "<="
    assert analyze_version_str(target_version="6.2.2", version_text="<=6.3.1")
    assert analyze_version_str(target_version="6.3.1", version_text="<=6.3.1")
    assert not analyze_version_str(target_version="6.4.0", version_text="<=6.3.1")
    # Test "<"
    assert analyze_version_str(target_version="6.2.2", version_text="<6.3.1")
    assert not analyze_version_str(target_version="6.3.1", version_text="<6.3.1")
    assert not analyze_version_str(target_version="6.4.0", version_text="<6.3.1")
