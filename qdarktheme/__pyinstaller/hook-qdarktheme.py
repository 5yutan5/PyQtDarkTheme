from pathlib import Path

import qdarktheme
from qdarktheme.qtpy.qt_compat import QT_API

if QT_API == "PyQt6":
    qdarktheme_path = Path(qdarktheme.__file__).parent

    datas = []
    for theme in ["dark", "light"]:
        datas += [(str(qdarktheme_path / "dist" / theme / "svg"), f"qdarktheme/dist/{theme}/svg")]
