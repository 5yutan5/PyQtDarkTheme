PyQtDarkTheme
=============
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyqtdarktheme.svg?color=orange)](https://pypi.org/project/pyqtdarktheme/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyqtdarktheme.svg?color=blue)](https://www.python.org/downloads/)
[![Qt Versions](https://img.shields.io/badge/Qt-5%20|%206-blue.svg?&logo=Qt&logoWidth=18&logoColor=white)](https://www.qt.io/qt-for-python)
[![License](https://img.shields.io/github/license/5yutan5/PyQtDarkTheme.svg?color=green)](https://github.com/5yutan5/PyQtDarkTheme/blob/main/LICENSE.txt/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)

[![Build Status](https://github.com/5yutan5/PyQtDarkTheme/workflows/os-test/badge.svg)](https://github.com/5yutan5/PyQtDarkTheme/actions/workflows/os-test.yml)
[![CodeQL Status](https://github.com/5yutan5/PyQtDarkTheme/workflows/codeql/badge.svg)](https://github.com/5yutan5/PyQtDarkTheme/actions/workflows/code-quality.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/5yutan5/PyQtDarkTheme.svg?logo=lgtm&logoWidth=18&color=success)](https://lgtm.com/projects/g/5yutan5/PyQtDarkTheme/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/5yutan5/PyQtDarkTheme.svg?logo=lgtm&logoWidth=18&color=success)](https://lgtm.com/projects/g/5yutan5/PyQtDarkTheme/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/5yutan5/pyqtdarktheme/badge)](https://www.codefactor.io/repository/github/5yutan5/pyqtdarktheme)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/5yutan5/PyQtDarkTheme/main.svg)](https://results.pre-commit.ci/latest/github/5yutan5/PyQtDarkTheme/main)

Dark theme for PySide and PyQt.

PyQtDarkTheme applies a flat dark theme to Qt applications(PySide6, PyQt6, PyQt5 and PySide2) using the qt stylesheets system.
There's a Light Theme too. Color and style balanced from the Dark theme for easy viewing in daylight.

PyQtDarkTheme is easy to freeze with freezing library(PyInstaller, py2app, cx_freeze or etc..).


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

app.setStyleSheet(qdarktheme.load_stylesheet())

main_win.show()

app.exec()

```

> ⚠ The image quality may be lower on Qt5(PyQt5, PySide2) due to the use of svg. You can add the following attribute to improve the quality of images.
> ```Python
> app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
> ```

### Light theme

```Python
app.setStyleSheet(qdarktheme.load_stylesheet("light"))
```

### Check common widgets

To check common widgets, run:

```plaintext
python -m qdarktheme.widget_gallery
```

## License

PyQtDarkTheme incorporates image assets from external sources. The icons for the PyQtDarkTheme are derived [Material design icons](https://fonts.google.com/icons)(Apache License Version 2.0).
Any file not listed in the [NOTICE.md](https://github.com/5yutan5/PyQtDarkTheme/blob/main/NOTICE.md) file is covered by PyQtDarkTheme's MIT license.
