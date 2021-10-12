# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from importlib import resources

from qdarktheme.qtpy.QtGui import QIcon


def get_icon(icon_name: str) -> QIcon:
    """Creates an icon from svg file in `qdarktheme/svg/app`. See below folder(`qdarktheme/widget_gallery/svg`)
    for details on available icons.
    """
    with resources.path("qdarktheme.widget_gallery.svg", f"{icon_name}_24dp.svg") as icon_path:
        return QIcon(str(icon_path))
