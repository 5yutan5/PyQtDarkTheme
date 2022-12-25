# PyQtDarkTheme

PyQtDarkTheme applies a flat dark theme to QtWidgets application. There's a light theme too. Color balanced from the dark theme for easy viewing in daylight.

Check out the [complete documentation](https://pyqtdarktheme.readthedocs.io).

**Project status**
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyqtdarktheme.svg?color=orange)](https://pypi.org/project/pyqtdarktheme/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyqtdarktheme.svg?color=blue)](https://www.python.org/downloads/)
[![Qt Versions](https://img.shields.io/badge/Qt-5%20|%206-blue.svg?&logo=Qt&logoWidth=18&logoColor=white)](https://www.qt.io/qt-for-python)
[![License](https://img.shields.io/github/license/5yutan5/PyQtDarkTheme.svg?color=green)](https://github.com/5yutan5/PyQtDarkTheme/blob/main/LICENSE.txt/)

**Tests**
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/5yutan5/PyQtDarkTheme/main.svg)](https://results.pre-commit.ci/latest/github/5yutan5/PyQtDarkTheme/main)
[![codecov](https://codecov.io/gh/5yutan5/PyQtDarkTheme/branch/main/graph/badge.svg?token=RTS8O0V6SF)](https://codecov.io/gh/5yutan5/PyQtDarkTheme)
[![Documentation Status](https://readthedocs.org/projects/pyqtdarktheme/badge/?version=latest)](https://pyqtdarktheme.readthedocs.io/en/latest/?badge=latest)

## Features

- A flat dark and light theme
- Support PySide and PyQt
- Sync with OS's theme and accent (Mac, Windows, Linux)
- Resolve the style differences between Qt versions
- Provide dark/light theme QPalette
- Override Qt old standard icons

## Themes

### Dark Theme

![widget_gallery_dark_theme](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_dark.png)

### Light Theme

![widget_gallery_light_them](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_light.png)

## Requirements

- [Python 3.7+](https://www.python.org/downloads/)
- Qt 5.15+
- PySide6, PyQt6, PyQt5 or PySide2

## Installation Method

- Last released version

   ```plaintext
   pip install pyqtdarktheme
   ```

- Latest development version

   ```plaintext
   pip install git+https://github.com/5yutan5/PyQtDarkTheme.git@main
   ```

## Usage

```Python
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
# Apply the complete dark theme to your Qt App.
qdarktheme.setup_theme()

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
```

Further information can be found in our docs:

- [Usage Guide](https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html)

### Enable HiDPI

```Python
# enable_hi_dpi() must be called before the instantiation of QApplication.
qdarktheme.enable_hi_dpi()
app = QApplication(sys.argv)
qdarktheme.setup_theme()
```

For Qt6 bindings, HiDPI “just works” without using this function.

### Light theme

```Python
qdarktheme.setup_theme("light")
```

### Sync with OS's theme and accent

```Python
qdarktheme.setup_theme("auto")
```

![sync with os theme](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/sync_with_os_theme.gif)

On macOS, qdarktheme also syncs with accent colors.
![sync with os accent](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/sync_with_os_accent.gif)

### Customizing colors

You can customize the theme color.

```python
# Customize accent color.
qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})
```

For a list of all customizable colors, see the Theme Color Reference:

- [Theme Color](https://pyqtdarktheme.readthedocs.io/en/latest/reference/theme_color.html)

### Sharp frame

You can change the corner style.

```python
# Default is "rounded".
stylesheet = qdarktheme.setup_theme(corner_shape="sharp")
```

### QPalette and stylesheet

You can also only load QPalette and stylesheet. `qdarktheme.setup_theme` uses the following functions internally.

```Python
palette = qdarktheme.load_palette(theme="dark")
stylesheet = qdarktheme.load_stylesheet(theme="dark")
```

## Example

To check all Qt widgets, run:

```plaintext
python -m qdarktheme.widget_gallery
```

## License

The svg files for the PyQtDarkTheme are derived [Material design icons](https://fonts.google.com/icons)(Apache License Version 2.0). Qt stylesheets are originally fork of [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet)(MIT License). Other files are covered by PyQtDarkTheme's MIT license. The accent detector(qdarktheme/_os_appearance/_accent/_mac_detect) is inspired by [darkdetect](https://github.com/albertosottile/darkdetect)(3-clause BSD License).

## Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome. You can get started by reading this:

- [Contributing Guide](https://pyqtdarktheme.readthedocs.io/en/latest/contributing.html)

## Change log

See [Releases](https://github.com/5yutan5/PyQtDarkTheme/releases).
