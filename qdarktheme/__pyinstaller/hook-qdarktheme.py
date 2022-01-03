from pathlib import Path

import qdarktheme
from qdarktheme.qtpy import __version__ as qt_version
from qdarktheme.qtpy.qt_compat import QT_API
from qdarktheme.util import compare_v

is_collect_svg = False
if qt_version is not None:
    is_collect_svg = compare_v(qt_version, "<", "5.13.0")
if QT_API == "PyQt6":
    is_collect_svg = True

if is_collect_svg:
    qdarktheme_path = Path(qdarktheme.__file__).parent

    datas = []
    for theme in ["dark", "light"]:
        datas += [(str(qdarktheme_path / "themes" / theme / "svg"), f"qdarktheme/themes/{theme}/svg")]
