"""PyQtDarkTheme - A flat dark theme for PySide and PyQt.

- Repository: https://github.com/5yutan5/PyQtDarkTheme
- Documentation: https://pyqtdarktheme.readthedocs.io


License Information
===================

Material design icons
---------------------

All svg files in PyQtDarkTheme is from Material design icons(which uses an Apache 2.0 license).

- Author: Google
- Site: https://fonts.google.com/icons
- Source: https://github.com/google/material-design-icons
- License: Apache License Version 2.0 | https://www.apache.org/licenses/LICENSE-2.0.txt

Modifications made to each files to change the icon color and angle and remove svg namespace.

The current Material design icons license summary can be viewed at:
https://github.com/google/material-design-icons/blob/master/LICENSE


QDarkStyleSheet(Source code)
----------------------------

Qt stylesheets are originally fork of QDarkStyleSheet(MIT License).

- Author: Colin Duquesnoy
- Site: https://github.com/ColinDuquesnoy/QDarkStyleSheet
- Source: https://github.com/ColinDuquesnoy/QDarkStyleSheet
- License: MIT License | https://opensource.org/licenses/MIT

Modifications made to a file to change the style.

The current QDarkStyleSheet license summary can be viewed at:
https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/LICENSE.rst

"""
# Version of PyQtDarkTheme
__version__ = "2.1.0"

from qdarktheme._main import enable_hi_dpi, setup_theme, stop_sync
from qdarktheme._style_loader import clear_cache, get_themes, load_palette, load_stylesheet
