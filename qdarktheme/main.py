"""Main file of qdarktheme."""
from __future__ import annotations

import json
import platform
import re
import shutil
from pathlib import Path

from qdarktheme.qtpy import __version__ as qt_version
from qdarktheme.qtpy.qt_compat import QT_API
from qdarktheme.util import OPERATORS, compare_v, get_logger, multi_replace

# Version of PyQtDarkTheme
__version__ = "1.1.1"

_logger = get_logger(__name__)

if qt_version is None:
    _logger.warning("Failed to detect Qt version. Load Qt version as the latest version.")
    _qt_version = "10.0.0"  # Fairly future version for always setting latest version.
else:
    _qt_version = qt_version

if QT_API is None:
    _qt_api = "PySide6"
    _logger.warning(f"Failed to detect Qt binding. Load Qt API as '{_qt_api}'.")
else:
    _qt_api = QT_API

if None in [qt_version, QT_API]:
    _logger.warning(
        "Maybe you need to install qt-binding. Available Qt-binding packages: PySide6, PyQt6, PyQt5, PySide2."
    )

_RESOURCE_HOME_DIR = Path.home() / ".qdarktheme"
_RESOURCES_BASE_DIR = _RESOURCE_HOME_DIR / f"v{__version__}"

# Pattern
_PATTERN_RADIUS = re.compile(r"\$radius\{[\s\S]*?\}")
_PATTERN_ENV_PATCH = re.compile(r"\$env_patch\{[\s\S]*?\}")


def _build_svg_files(theme: str, theme_resources_dir: Path) -> None:
    svg_resources_dir = theme_resources_dir / "svg"
    if not svg_resources_dir.exists():
        svg_resources_dir.mkdir()
    else:
        return

    if theme == "dark":
        from qdarktheme.themes.dark.svg import SVG_RESOURCES
    else:
        from qdarktheme.themes.light.svg import SVG_RESOURCES

    for file_name, code in json.loads(SVG_RESOURCES).items():
        (svg_resources_dir / f"{file_name}.svg").write_text(code)


def get_themes() -> tuple[str, ...]:
    """Return available theme list.

    Returns:
        Available themes.
    """
    from qdarktheme.themes import THEMES

    return THEMES


def _replace_rounded(match: re.Match) -> str:
    return match.group().replace("$radius{", "").replace("}", "")


def _replace_sharp(match: re.Match) -> str:
    return _PATTERN_RADIUS.sub("0", match.group())


def _parse_radius(stylesheet: str, border: str = "rounded") -> dict[str, str]:
    """Parse `$radius{...}` placeholder in template stylesheet."""
    matches = _PATTERN_RADIUS.finditer(stylesheet)
    replace = _replace_rounded if border == "rounded" else _replace_sharp
    return {match.group(): replace(match) for match in matches}


def _parse_env_patch(stylesheet: str) -> dict[str, str]:
    """Parse `$env_patch{...}` placeholder in template stylesheet.

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
    for match in re.finditer(_PATTERN_ENV_PATCH, stylesheet):
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


def load_stylesheet(theme: str = "dark", border: str = "rounded") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme.

    Args:
        theme: The name of the theme. Available themes are "dark" and "light".
        border: The border style. Available styles are "rounded" and "sharp".

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

        Change sharp frame.

        Sharp Frame::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet(border="sharp"))
    """
    if theme not in get_themes():
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    if border not in ("rounded", "sharp"):
        raise TypeError("The argument [border] can only be specified as 'rounded' or 'sharp'.")

    theme_resources_dir = _RESOURCES_BASE_DIR / theme
    theme_resources_dir.mkdir(parents=True, exist_ok=True)
    _build_svg_files(theme, theme_resources_dir)

    if theme == "dark":
        from qdarktheme.themes.dark.stylesheet import STYLE_SHEET
    else:
        from qdarktheme.themes.light.stylesheet import STYLE_SHEET

    # Build stylesheet
    # Radius
    replacements_radius = _parse_radius(STYLE_SHEET, border)
    stylesheet = multi_replace(STYLE_SHEET, replacements_radius)
    # Env
    replacements_env = _parse_env_patch(stylesheet)
    # Path
    replacements_env["${path}"] = _RESOURCES_BASE_DIR.as_posix()
    return multi_replace(stylesheet, replacements_env)


def clear_cache():
    """Clear the caches in system home path.

    PyQtDarkTheme build the caches of resources in the system home path.You can clear the caches by running this
    method.
    """
    try:
        shutil.rmtree(_RESOURCE_HOME_DIR)
        _logger.info(f"The caches({_RESOURCE_HOME_DIR}) has been deleted")
    except FileNotFoundError:
        _logger.info("There is no caches")


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
