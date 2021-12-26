# qtpy_qt6

Provides an uniform layer to support some features of PyQt6 PySide6, PyQt5 and PySide2 with a single codebase.

This module provides a workaround of the problem that Qt6 cannot be used with [qtpy](https://github.com/spyder-ide/qtpy).

## Available modules

- QtWidgets
- QtCore
- QtGui
- QtSvg

## Usage

This module is intended to be included in the repository as a submodule.
It can be easily added to an existing git repository with the following command.

```plaintext
git submodule add https://github.com/5yutan5/qtpy_qt6.git qtpy
```

[Example](https://github.com/5yutan5/PyQtDarkTheme/tree/main/qdarktheme)