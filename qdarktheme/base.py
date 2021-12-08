"""Main file of qdarktheme."""
from __future__ import annotations

import json
import operator as ope
import re
import sys
from pathlib import Path

from qdarktheme.util import get_logger, get_qdarktheme_root_path, multireplace

_logger = get_logger(__name__)

# greater_equal and less_equal must be evaluated before greater and less.
_OPERATORS = {"==": ope.eq, "!=": ope.ne, ">=": ope.ge, "<=": ope.le, ">": ope.gt, "<": ope.lt}

THEMES = ("dark", "light")


def _compare_v(v1: str, operator: str, v2) -> bool:
    """Comparing two versions."""
    v1_list, v2_list = (v.split(".") for v in (v1, v2))
    return _OPERATORS[operator](v1_list, v2_list)


def _parse_env_patch(stylesheet: str) -> dict[str, str]:
    """Parse `$env_patch{...}` symbol in template stylesheet.

    Template stylesheet has `$env_patch{...}` symbol.
    This symbol has json string and resolve the differences of the style between qt versions.
    The json keys:
        * version - the qt version and qualifier. Available qualifiers: [==, !=, >=, <=, >, <].
        * value - the qt stylesheet string

    Args:
        stylesheet: The qt stylesheet string.

    Raises:
        SyntaxError: If the version operator in version key of `$env_patch{...}` is wrong.

    Returns:
        The dictionary. Key is the text of $env_patch{...} symbol.
        Value is the value of the `value` key in $env_patch.
    """
    from qdarktheme.qtpy import __version__ as qt_version

    if qt_version is None:
        _logger.warning(
            "Failed to detect Qt version. -> Load stylesheet as the latest version."
            + "\nMaybe you need to install qt-binding. Available Qt-binding packages: PySide6, PyQt6, PyQt5, PySide2."
        )
        qt_version = "10.0.0"  # Fairly future version for always setting latest version.

    replacements = {}
    for match in re.finditer(r"\$env_patch\{[\s\S]*?\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$env_patch", "")
        env_property: dict[str, str] = json.loads(json_text)

        for operator in _OPERATORS.keys():
            if operator in env_property["version"]:
                version = env_property["version"].replace(operator, "")
                replacements[match_text] = env_property["value"] if _compare_v(qt_version, operator, version) else ""
                break
        else:
            raise SyntaxError(
                f"invalid character in qualifier. Available qualifiers {list(_OPERATORS.keys())}"
            ) from None
    return replacements


def load_stylesheet(theme: str = "dark") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme.

    Args:
        theme: The name of the theme. Available theme are "dark" and "light". Defaults to "dark".

    Raises:
        TypeError: If the arg of theme name is wrong.

    Returns:
        The stylesheet string for the given theme.
    """
    if theme not in ("dark", "light"):
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    if theme == "dark":
        from qdarktheme.dist.dark.stylesheet import STYLE_SHEET
    else:
        from qdarktheme.dist.light.stylesheet import STYLE_SHEET

    # Append Qt version patches
    replacements = _parse_env_patch(STYLE_SHEET)
    stylesheet = multireplace(STYLE_SHEET, replacements)

    from qdarktheme.qtpy import QtImportError

    try:
        if theme == "dark":
            from qdarktheme.dist.dark import rc_icons as _
        elif theme == "light":
            from qdarktheme.dist.light import rc_icons as _  # noqa: F401
        icon_path = ":qdarktheme"
    except (AttributeError, QtImportError):
        # Qt resource system has been removed in PyQt6. So in PyQt6, load the icon from a physical file.
        # PyInstaller's onefile uses temp dir(_MEIPASS).
        if hasattr(sys, "_MEIPASS"):
            module_path = Path(sys._MEIPASS) / "qdarktheme"  # type: ignore
            icon_path = module_path.as_posix()
        else:
            icon_path = get_qdarktheme_root_path().as_posix()
    # Replace the ${path} variable by real path value
    return stylesheet.replace("${path}", icon_path)


def load_palette(theme: str = "dark"):
    """Load the QPalette for the dark or light theme.

    Args:
        theme: The name of the theme. Available theme are "dark" and "light". Defaults to "dark".

    Raises:
        TypeError: If the arg name of theme is wrong.

    Returns:
        QPalette: The QPalette for the given theme.
    """
    if theme not in ("dark", "light"):
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    if theme == "dark":
        from qdarktheme.dist.dark.palette import PALETTE
    else:
        from qdarktheme.dist.light.palette import PALETTE
    return PALETTE
