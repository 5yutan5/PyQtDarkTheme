PyQtDarkTheme
=============
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyqtdarktheme.svg)](https://pypi.org/project/pyqtdarktheme/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyqtdarktheme.svg)](https://pypi.org/project/pyqtdarktheme/)
[![License](https://img.shields.io/github/license/5yutan5/PyQtDarkTheme)](/LICENSE)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/5yutan5/PyQtDarkTheme.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/5yutan5/PyQtDarkTheme/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/5yutan5/PyQtDarkTheme.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/5yutan5/PyQtDarkTheme/context:python)

Dark theme for PySide, PyQt and Qt Designer.

This python module applies a theme to a Qt applications(PySide6, PyQt6, PyQt5 and PySide2) using a qt stylesheets system.  
There's a Light Theme too. Color and style balanced from the Dark theme for easy viewing in daylight.

### Dark Theme
![widget_gallery_dark_theme](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_dark.png)

### Light Theme
![widget_gallery_light_them](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_light.png)

## Requirements

- [Python 3.7+](https://www.python.org/downloads/release/python-396/)
- PySide6, PyQt6, PyQt5 or PySide2

## Installation

```plaintext
pip install pyqtdarktheme
```

## Usage

```Python
import sys

import qdarktheme
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)
main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
main_win.setCentralWidget(push_button)

app.setStyleSheet(qdarktheme.load_stylesheet())

main_win.show()

app.exec()

```

### Light theme

```Python
app.setStyleSheet(qdarktheme.load_stylesheet("light"))
```

### Check common widgets

Input the following command in a terminal to check common widgets.

```plaintext
python -m qdarktheme.examples.widget_gallery
```

## Custom Properties

This module provides several custom properties.  
You can use `setProperty()` of the widget object to apply a modern style.

For example, if you set the QToolbar `type` property to `sidebar`, the style for the sidebar will be applied.

```Python
sidebar = QToolBar()
sidebar.setProperty("type", "sidebar")
```

| Widget      | Property | Property value            | Default  | Command for demo                                                                                                                            |
|-------------|----------|---------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| QToolBar    | type     | toolbar, sidebar          | toolbar  | [`python -m qdarktheme.examples.sidebar`](https://github.com/5yutan5/PyQtDarkTheme/blob/main/qdarktheme/examples/sidebar/__main__.py)       |
| QPushButton | type     | outlined, contained, text | outlined | [`python -m qdarktheme.examples.pushbutton`](https://github.com/5yutan5/PyQtDarkTheme/blob/main/qdarktheme/examples/pushbutton/__main__.py) |
| QLineEdit   | state    | normal, warning, error    | normal   | [`python -m qdarktheme.examples.lineedit`](https://github.com/5yutan5/PyQtDarkTheme/blob/main/qdarktheme/examples/lineedit/__main__.py)     |
| QFrame      | type     | normal, h_line, v_line    | normal   | [`python -m qdarktheme.examples.line`](https://github.com/5yutan5/PyQtDarkTheme/blob/main/qdarktheme/examples/line/__main__.py)             |

## Support Qt Designer

This module support Qt Designer.

How to use PyQtDarktheme with Qt Designer.
1. Run the following command in the terminal to launch the app that creates the template for the designer.  
   ```plaintext
   python -m qdarktheme.designer_supporter
   ```
1. Select a theme(dark or light) and press the Create button to create a template in any folder.
1. Copy the style sheet displayed in the text box.
1. Start Qt designer and save the ui file in the root of the template you created.
1. Paste the copied stylesheet into the top-level widget.
1. Register the resource file(.qrc) in the template to the resource browser.

> ⚠ Support for Qt’s resource system has been removed in PyQt6. Therefore, if you want to use Qt Designer in PyQt6, you need to delete the stylesheet in the ui file and load the stylesheet using `load_stylesheet()`.

## License

The icons used in the demo code are sourced from the [Material design icons](https://fonts.google.com/icons)(Apache License Version 2.0).  
Any file not listed the [NOTICE.md](https://github.com/5yutan5/PyQtDarkTheme/blob/main/NOTICE.md) file is covered by PyQtDarkTheme's MIT license.