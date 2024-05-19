贡献指南
==================

所有的贡献、错误报告、错误修复、文档改进、增强和想法都是受欢迎的。

本地开发
-----------------

以下是开始在 PyQtDarkTheme 上开发所需的基本步骤。

1. 克隆 PyQtDarkTheme
    首先，你需要使用 git 克隆仓库并进入其目录：

    .. code-block:: bash

        $ git@github.com:5yutan5/PyQtDarkTheme.git
        $ cd PyQtDarkTheme
2. 安装 Poetry
    你需要 Poetry 来开始在 PyQtDarkTheme 代码库上贡献。参考 `Poetry 文档 <https://python-poetry.org/docs/#installation>`__ 来开始使用 Poetry。
3. 创建虚拟环境
    现在，你需要用 Poetry 安装 PyQtDarkTheme 所需的依赖，并用 pip 安装 Qt 绑定（PySide 或 PyQt）。

    .. code-block:: bash

        $ poetry install
        $ poetry run pip install PySide6

4. 运行 Pytest
    你需要确保当前的测试在你的机器上通过：

    .. code-block:: bash

        $ poetry run pytest tests
5. 设置 pre-commit
    为了确保你不会意外地提交不符合编码风格的代码，你可以安装一个 pre-commit 钩子，它会检查一切是否正常：

    .. code-block:: bash

        $ poetry run pre-commit install
6. 检查 Qt 主题
    你可以使用内置应用检查深色/浅色主题。

    .. code-block:: bash

        $ poetry run python -m qdarktheme.widget_gallery