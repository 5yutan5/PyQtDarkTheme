# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import json
import operator
import re
from distutils.version import StrictVersion
from importlib import resources

from qdarktheme.util import create_logger, multireplace

_logger = create_logger(__name__)


def _parse_env_patch(stylesheet: str) -> dict[str, str]:
    from qdarktheme.qtpy import __version__ as qt_version

    if qt_version is None:
        _logger.warning("Failed to detect Qt version. -> Load stylesheet as the latest version.")
        qt_version = "10.0.0"  # Fairly future version for always setting latest version.

    # greater_equal and less_equal must be evaluated before greater and less.
    operators = {
        "==": operator.eq,  # equal
        "!=": operator.ne,  # unequal
        ">=": operator.ge,  # greater_equal
        "<=": operator.le,  # less_equal
        ">": operator.gt,  # greater
        "<": operator.lt,  # less
    }
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
            raise SyntaxError(f"invalid character in qualifier. Available qualifiers {list(operators.keys())}")

        is_true = operators[qualifier](StrictVersion(qt_version), StrictVersion(version))
        replacements[match_text] = property["value"] if is_true else ""
    return replacements


def load_stylesheet(theme: str = "dark") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme."""

    if theme not in ["dark", "light"]:
        raise TypeError("The argument [theme] can only be specified as 'dark' or 'light'.") from None

    stylesheet = resources.read_text(f"qdarktheme.dist.{theme}", "stylesheet.qss")
    replacements = _parse_env_patch(stylesheet)
    stylesheet = multireplace(stylesheet, replacements)

    # Replace the variable by prefix or absolute path
    with resources.path("qdarktheme", "__init__.py") as path:
        stylesheet = stylesheet.replace("${path}", str(path.parent.as_posix()))

    return stylesheet
