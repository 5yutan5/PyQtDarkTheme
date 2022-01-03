"""Main file of qdarktheme."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from qdarktheme.util import OPERATORS, compare_v, get_logger, get_qdarktheme_root_path, multi_replace

_logger = get_logger(__name__)


class _SvgFileNotFoundError(FileNotFoundError):

    pass


def get_themes() -> tuple[str, ...]:
    """Return available theme list.

    Returns:
        Available themes.
    """
    from qdarktheme.themes import THEMES

    return THEMES


def _get_qt_version() -> str:
    from qdarktheme.qtpy import __version__ as qt_version

    if qt_version is None:
        _logger.warning(
            "Failed to detect Qt version. -> Load stylesheet as the latest version."
            + "\nMaybe you need to install qt-binding. Available Qt-binding packages: PySide6, PyQt6, PyQt5, PySide2."
        )
        return "10.0.0"  # Fairly future version for always setting latest version.
    return qt_version


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
    replacements = {}
    for match in re.finditer(r"\$env_patch\{[\s\S]*?\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$env_patch", "")
        env_property: dict[str, str] = json.loads(json_text)

        for operator in OPERATORS.keys():
            if operator in env_property["version"]:
                version = env_property["version"].replace(operator, "")
                qt_version = _get_qt_version()
                replacements[match_text] = env_property["value"] if compare_v(qt_version, operator, version) else ""
                break
        else:
            raise SyntaxError(
                f"invalid character in qualifier. Available qualifiers {list(OPERATORS.keys())}"
            ) from None
    return replacements


def load_stylesheet(theme: str = "dark") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme.

    Args:
        theme: The name of the theme. Available theme are "dark" and "light".

    Raises:
        TypeError: If the arg of theme name is wrong.

    Returns:
        The stylesheet string for the given theme.

    Examples:
        Set stylesheet to your Qt application.

        1. Dark Theme::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet())
            # or
            app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

        2. Light Theme::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet("light"))
    """
    if theme not in get_themes():
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    if theme == "dark":
        from qdarktheme.themes.dark.stylesheet import STYLE_SHEET
    else:
        from qdarktheme.themes.light.stylesheet import STYLE_SHEET

    # Append Qt version patches
    replacements = _parse_env_patch(STYLE_SHEET)
    stylesheet = multi_replace(STYLE_SHEET, replacements)

    from qdarktheme.qtpy import QtImportError

    qt_version = _get_qt_version()

    try:
        # In mac os, if the qt version is 5.13 or lower, the svg icon of Qt resource file cannot be read correctly.
        if compare_v(qt_version, "<", "5.13.0"):
            raise _SvgFileNotFoundError()

        if theme == "dark":
            from qdarktheme.themes.dark import rc_icons as _
        elif theme == "light":
            from qdarktheme.themes.light import rc_icons as _  # noqa: F401
        icon_path = ":qdarktheme"
    except (AttributeError, QtImportError, _SvgFileNotFoundError):
        # Qt resource system has been removed in PyQt6. So in PyQt6, load the icon from a physical file.
        # PyInstaller's one file option uses temp dir(_MEIPASS).
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
        theme: The name of the theme. Available theme are "dark" and "light".

    Raises:
        TypeError: If the arg name of theme is wrong.

    Returns:
        QPalette: The QPalette for the given theme.

    Examples:
        Set QPalette to your Qt application.

        1. Dark Theme::

            app = QApplication([])
            app.setPalette(qdarktheme.load_palette())
            # or
            app.setPalette(qdarktheme.load_palette("dark"))

        2. Light Theme::

            app = QApplication([])
            app.setPalette(qdarktheme.load_palette("light"))
    """
    if theme not in get_themes():
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    if theme == "dark":
        from qdarktheme.themes.dark.palette import PALETTE
    else:
        from qdarktheme.themes.light.palette import PALETTE
    return PALETTE
