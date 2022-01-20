"""Main file of qdarktheme."""
from __future__ import annotations

import json
import platform
import re
import sys
from pathlib import Path

from qdarktheme.qtpy import QtImportError, __version__
from qdarktheme.qtpy.qt_compat import QT_API
from qdarktheme.util import OPERATORS, compare_v, get_logger, get_qdarktheme_root_path, multi_replace

_logger = get_logger(__name__)

if __version__ is None:
    _logger.warning("Failed to detect Qt version. Load Qt version as the latest version.")
    _qt_version = "10.0.0"  # Fairly future version for always setting latest version.
else:
    _qt_version = __version__

if QT_API is None:
    _qt_api = "PySide6"
    _logger.warning(f"Failed to detect Qt binding. Load Qt API as '{_qt_api}'.")
else:
    _qt_api = QT_API

if None in [__version__, QT_API]:
    _logger.warning(
        "Maybe you need to install qt-binding. Available Qt-binding packages: PySide6, PyQt6, PyQt5, PySide2."
    )


class _SvgFileNotFoundError(FileNotFoundError):

    pass


def get_themes() -> tuple[str, ...]:
    """Return available theme list.

    Returns:
        Available themes.
    """
    from qdarktheme.themes import THEMES

    return THEMES


def _parse_env_patch(stylesheet: str) -> dict[str, str]:
    """Parse `$env_patch{...}` symbol in template stylesheet.

    Template stylesheet has `$env_patch{...}` symbol.
    This symbol has json string and resolve the differences of the style between qt versions.
    The json keys:
        * version - the qt version and qualifier. Available qualifiers: [==, !=, >=, <=, >, <].
        * qt - the name of qt binding.
        * value - the qt stylesheet string

    Args:
        stylesheet: The qt stylesheet string.

    Raises:
        SyntaxError: If the version operator in version key of `$env_patch{...}` is wrong.

    Returns:
        The dictionary. Key is the text of $env_patch{...} symbol.
        Value is the value of the `value` key in $env_patch.
    """
    replacements: dict[str, str] = {}
    for match in re.finditer(r"\$env_patch\{[\s\S]*?\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$env_patch", "")
        env_property: dict[str, str] = json.loads(json_text)

        patch_version = env_property.get("version")
        patch_qt = env_property.get("qt")
        patch_os = env_property.get("os")
        patch_value = env_property["value"]

        results: list[bool] = []
        # Parse version
        if patch_version is not None:
            for operator in OPERATORS:
                if operator not in patch_version:
                    continue
                version = patch_version.replace(operator, "")
                results.append(compare_v(_qt_version, operator, version))
                break
            else:
                raise SyntaxError(
                    f"invalid character in qualifier. Available qualifiers {list(OPERATORS.keys())}"
                ) from None
        # Parse qt binding
        if patch_qt is not None:
            if QT_API is None:
                results.append(False)
            results.append(patch_qt.lower() == _qt_api.lower())
        # Parse os
        if patch_os is not None:
            results.append(platform.system().lower() in patch_os.lower())

        replacements[match_text] = patch_value if all(results) else ""
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

    try:
        # In mac os, if the qt version is 5.13 or lower, the svg icon of Qt resource file cannot be read correctly.
        if compare_v(_qt_version, "<", "5.13.0"):
            raise _SvgFileNotFoundError()

        if theme == "dark":
            from qdarktheme.themes.dark import rc_icons as _
        else:
            from qdarktheme.themes.light import rc_icons as _  # noqa: F401
        icon_path = ":qdarktheme"
    except (AttributeError, QtImportError, _SvgFileNotFoundError):
        # Qt resource system has been removed in PyQt6. So in PyQt6, load the icon from a physical file.
        # PyInstaller's one file option uses temp dir(_MEIPASS).
        if hasattr(sys, "_MEIPASS"):
            icon_path = (Path(sys._MEIPASS) / "qdarktheme").as_posix()  # type: ignore
        else:
            icon_path = get_qdarktheme_root_path().as_posix()

    if theme == "dark":
        from qdarktheme.themes.dark.stylesheet import STYLE_SHEET
    else:
        from qdarktheme.themes.light.stylesheet import STYLE_SHEET

    # Create Qt version patches
    replacements = _parse_env_patch(STYLE_SHEET)
    # Replace the ${path} variable by real path value
    replacements["${path}"] = icon_path
    # Build stylesheet
    return multi_replace(STYLE_SHEET, replacements)


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
