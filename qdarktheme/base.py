# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import json
import operator as ope
import re
import sys
from distutils.version import StrictVersion
from pathlib import Path

from qdarktheme.util import create_logger, get_project_root_path, multireplace

_logger = create_logger(__name__)


def _parse_env_patch(stylesheet: str) -> dict[str, str]:
    from qdarktheme.qtpy import __version__ as qt_version

    if qt_version is None:
        _logger.warning("Failed to detect Qt version. -> Load stylesheet as the latest version.")
        qt_version = "10.0.0"  # Fairly future version for always setting latest version.

    # greater_equal and less_equal must be evaluated before greater and less.
    operators = {"==": ope.eq, "!=": ope.ne, ">=": ope.ge, "<=": ope.le, ">": ope.gt, "<": ope.lt}
    replacements = {}

    for match in re.finditer(r"\$env_patch\{[\s\S]*?\}", stylesheet):
        match_text = match.group()
        json_text = match_text.replace("$env_patch", "")
        property: dict[str, str] = json.loads(json_text)

        for qualifier in operators.keys():
            if qualifier in property["version"]:
                version = property["version"].replace(qualifier, "")
                break
        else:
            raise SyntaxError(
                f"invalid character in qualifier. Available qualifiers {list(operators.keys())}"
            ) from None

        is_true = operators[qualifier](StrictVersion(qt_version), StrictVersion(version))
        replacements[match_text] = property["value"] if is_true else ""
    return replacements


def load_stylesheet(theme: str = "dark") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme."""

    if theme == "dark":
        from qdarktheme.dist.dark.stylesheet import STYLE_SHEET
    elif theme == "light":
        from qdarktheme.dist.light.stylesheet import STYLE_SHEET
    else:
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    # Append Qt version patches
    replacements = _parse_env_patch(STYLE_SHEET)
    stylesheet = multireplace(STYLE_SHEET, replacements)

    # Qt resource system has been removed in PyQt6.
    # So in PyQt6, load the icon from a physical file.
    try:
        if theme == "dark":
            from qdarktheme.dist.dark import rc_icons
        elif theme == "light":
            from qdarktheme.dist.light import rc_icons  # noqa: F401
        icon_path = ":qdarktheme"
    except AttributeError:
        if hasattr(sys, "_MEIPASS"):  # For PyInstaller --onefile
            icon_path = Path(sys._MEIPASS / "qdarktheme").as_posix()  # type: ignore
        else:
            icon_path = get_project_root_path().as_posix()
    # Replace the ${path} variable by real path value
    return stylesheet.replace("${path}", icon_path)
