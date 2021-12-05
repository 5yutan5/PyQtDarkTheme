# PyQtDarkTheme

PyQtDarkTheme applies a flat dark theme to QtWidgets application(PySide and PyQt). There's a light theme too. Color and style balanced from a dark theme for easy viewing in daylight.

**Project status**  
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyqtdarktheme.svg?color=orange)](https://pypi.org/project/pyqtdarktheme/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyqtdarktheme.svg?color=blue)](https://www.python.org/downloads/)
[![Qt Versions](https://img.shields.io/badge/Qt-5%20|%206-blue.svg?&logo=Qt&logoWidth=18&logoColor=white)](https://www.qt.io/qt-for-python)
[![License](https://img.shields.io/github/license/5yutan5/PyQtDarkTheme.svg?color=green)](https://github.com/5yutan5/PyQtDarkTheme/blob/main/LICENSE.txt/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)

**Tests**  
[![tests](https://github.com/5yutan5/PyQtDarkTheme/actions/workflows/test.yml/badge.svg)](https://github.com/5yutan5/PyQtDarkTheme/actions/workflows/test.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/5yutan5/PyQtDarkTheme/main.svg)](https://results.pre-commit.ci/latest/github/5yutan5/PyQtDarkTheme/main)
[![codecov](https://codecov.io/gh/5yutan5/PyQtDarkTheme/branch/main/graph/badge.svg?token=RTS8O0V6SF)](https://codecov.io/gh/5yutan5/PyQtDarkTheme)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/5yutan5/PyQtDarkTheme.svg?logo=lgtm&logoWidth=18&color=success)](https://lgtm.com/projects/g/5yutan5/PyQtDarkTheme/alerts/)

## Features

- A flat Dark and Light theme
- Support PySide and PyQt
- Support some freezing library(PyInstaller, cx_freeze, py2app and etc...)
- Resolve the differences of style between Qt versions
- QPalette of dark and light theme

## Themes

### Dark Theme

![widget_gallery_dark_theme](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_dark.png)

### Light Theme

![widget_gallery_light_them](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_light.png)

## Requirements

- [Python 3.7+](https://www.python.org/downloads/)
- PySide6, PyQt6, PyQt5 or PySide2

## Installation Method

- Last released version

   ```plaintext
   pip install pyqtdarktheme
   ```

- Latest development version

   ```plaintext
   pip install git+https://github.com/5yutan5/PyQtDarkTheme
   ```

## Usage

```Python
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

# Default is dark theme
app.setStyleSheet(qdarktheme.load_stylesheet())
# qdarktheme.load_stylesheet("dark")

main_win.show()

app.exec()

```

> ⚠ The image quality may be lower on Qt5(PyQt5, PySide2) due to the use of svg. You can add the following attribute to improve the quality of images.
>
> ```Python
> app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
> ```

### Light theme

```Python
app.setStyleSheet(qdarktheme.load_stylesheet("light"))
```

### Dark and Light palette

You can get color of dark and light theme by loading QPalette.
To load palette, run:

```Python
palette = qdarktheme.load_palette()
# qdarktheme.load_palette("dark")
# qdarktheme.load_palette("light")
```

For example, you can apply a link color to your application.

```Python
import sys

from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication

import qdarktheme

app = QApplication(sys.argv)
dark_palette = qdarktheme.load_palette()
palette = app.palette()
palette.setColor(QPalette.ColorRole.Link, dark_palette.link().color())
app.setPalette(palette)
```

## Example

To check example app, run:

```plaintext
python -m qdarktheme.widget_gallery
```

## License

The svg file for the PyQtDarkTheme are derived [Material design icons](https://fonts.google.com/icons)(Apache License Version 2.0). Qt stylesheets are originally fork of [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet)(MIT License). Other files are covered by PyQtDarkTheme's MIT license.
