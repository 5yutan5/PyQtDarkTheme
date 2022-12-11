from __future__ import annotations

import json

from qdarktheme._icon.icon_engine import SvgIconEngine
from qdarktheme._icon.svg import Svg
from qdarktheme._resources import NEW_STANDARD_ICON_MAP
from qdarktheme.qtpy.QtGui import QIcon
from qdarktheme.qtpy.QtWidgets import QProxyStyle, QStyle, QStyleOption


class QDarkThemeStyle(QProxyStyle):
    """Style proxy to improve theme."""

    def __init__(self):
        """Initialize style proxy."""
        super().__init__()
        self._new_standard_icon_map: dict[str, dict] = json.loads(NEW_STANDARD_ICON_MAP)

    def standardIcon(  # noqa: N802
        self, standard_icon: QStyle.StandardPixmap, option: QStyleOption | None, widget
    ) -> QIcon:
        """Implement QProxyStyle.standardIcon."""
        standard_icon_name = str(standard_icon).split(".")[-1]
        icon_info = self._new_standard_icon_map.get(standard_icon_name)
        if icon_info is None:
            return super().standardIcon(standard_icon, option, widget)

        rotate = icon_info.get("rotate", 0)
        svg = Svg(icon_info["id"]).rotate(rotate)
        icon_engine = SvgIconEngine(svg)
        return QIcon(icon_engine)
