# PyQtDarkTheme

PyQtDarkTheme 能够对 QtWidgets 应用程序应用平板暗色主题。也有一个亮色主题。拥有从暗色主题中获得的色彩平衡，方便在日光下查看。

请查阅[完整文档](https://pyqtdarktheme.readthedocs.io)获取更多信息。

**项目状态**

[![PyPI 最新发布版本](https://img.shields.io/pypi/v/pyqtdarktheme.svg?color=orange)](https://pypi.org/project/pyqtdarktheme/)
[![Python 版本](https://img.shields.io/pypi/pyversions/pyqtdarktheme.svg?color=blue)](https://www.python.org/downloads/)
[![Qt 版本](https://img.shields.io/badge/Qt-5%20|%206-blue.svg?&logo=Qt&logoWidth=18&logoColor=white)](https://www.qt.io/qt-for-python)
[![许可证](https://img.shields.io/github/license/5yutan5/PyQtDarkTheme.svg?color=green)](https://github.com/5yutan5/PyQtDarkTheme/blob/main/LICENSE.txt/)

**测试**

[![pre-commit.ci 状态](https://results.pre-commit.ci/badge/github/5yutan5/PyQtDarkTheme/main.svg)](https://results.pre-commit.ci/latest/github/5yutan5/PyQtDarkTheme/main)
[![codecov](https://codecov.io/gh/5yutan5/PyQtDarkTheme/branch/main/graph/badge.svg?token=RTS8O0V6SF)](https://codecov.io/gh/5yutan5/PyQtDarkTheme)
[![文档状态](https://readthedocs.org/projects/pyqtdarktheme/badge/?version=latest)](https://pyqtdarktheme.readthedocs.io/en/latest/?badge=latest)

## 特性

- 简约的暗色和亮色主题
- 支持 PySide 和 PyQt
- 与操作系统的主题和强调色同步 (Mac、Windows、Linux)
- 解决不同 Qt 版本之间的风格差异
- 提供暗色/亮色主题的 QPalette
- 覆盖 Qt 旧的标准图标

## 主题

### 暗色主题

![暗色主题的部件展示](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_dark.png)

### 亮色主题

![亮色主题的部件展示](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/widget_gallery_light.png)

## 需求

- [Python 3.7+](https://www.python.org/downloads/)
- Qt 5.15+
- PySide6, PyQt6, PyQt5 或者 PySide2

## 安装方法

- 最新发布版本

   ```plaintext
   pip install pyqtdarktheme
   ```

- 最新开发版本

   ```plaintext
   pip install git+https://github.com/5yutan5/PyQtDarkTheme.git@main
   ```

## 使用方式 

```Python
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication(sys.argv)
# 在你的 Qt 应用上应用完整的暗色主题。
qdarktheme.setup_theme()

main_win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme！")
main_win.setCentralWidget(push_button)

main_win.show()

app.exec()
```
更多信息可以在我们的文档中找到：

- [使用指南](https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html)

### 启用 HiDPI

```Python
# enable_hi_dpi() 必须在 QApplication 的实例化之前调用。
qdarktheme.enable_hi_dpi()
app = QApplication(sys.argv)
qdarktheme.setup_theme()
```

对于 Qt6 绑定，HiDPI “能够自动工作”而不需要使用此函数。

### 亮色主题

```Python
qdarktheme.setup_theme("light")
```

### 与操作系统的主题和强调色同步

```Python
qdarktheme.setup_theme("auto")
```

![与操作系统主题同步](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/sync_with_os_theme.gif)

在macOS上，qdarktheme还可以与强调色同步。 
![与操作系统强调色同步](https://raw.githubusercontent.com/5yutan5/PyQtDarkTheme/main/images/sync_with_os_accent.gif)

### 定制颜色

你可以定制主题颜色。

```python
# 定制强调色。
qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})
```

所有可定制颜色的列表，请见主题颜色参考：

- [主题颜色](https://pyqtdarktheme.readthedocs.io/en/latest/reference/theme_color.html)

### 锐利的框边

你可以更改角落的样式。

```python
# 默认是 "rounded".
stylesheet = qdarktheme.setup_theme(corner_shape="sharp")
```

### QPalette 和样式表

你也可以只加载 QPalette 和样式表。`qdarktheme.setup_theme` 内部使用以下函数。

```Python
palette = qdarktheme.load_palette(theme="dark")
stylesheet = qdarktheme.load_stylesheet(theme="dark")
```
## 示例 

要查看所有 Qt 部件，请运行：

```plaintext
python -m qdarktheme.widget_gallery
```
## 许可证

PyQtDarkTheme 为的 svg 文件源自 [Material design icons](https://fonts.google.com/icons)(Apache License Version 2.0)。Qt 样式表原为 [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet)的分支(MIT License)。其他文件都受到 PyQtDarkTheme 的 MIT 许可证保护。强调色检测器(qdarktheme/_os_appearance/_accent/_mac_detect) 的设计灵感源自[darkdetect](https://github.com/albertosottile/darkdetect)(3-clause BSD License)。

## 贡献方式

所有的贡献，包括错误报告，错误修复，文档改进，增强、创意等均受到欢迎。你可以从阅读这个开始：

- [贡献指南](https://pyqtdarktheme.readthedocs.io/en/latest/contributing.html)

## 变更记录

请见[发布记录](https://github.com/5yutan5/PyQtDarkTheme/releases)。