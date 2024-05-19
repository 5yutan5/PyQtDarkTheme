PyQtDarkTheme 文档
===========================

PyQtDarkTheme 提供了一个扁平化的深色主题给 QtWidgets 应用程序(PySide 和 PyQt)。也有一个浅色主题。颜色和样式是从深色主题中平衡选择的，以便在日光下易于查看。

.. tab-set::

    .. tab-item:: 深色

        .. image:: ../../images/widget_gallery_dark.png
            :class: dark-light

    .. tab-item:: 浅色

        .. image:: ../../images/widget_gallery_light.png
            :class: dark-light

    .. tab-item:: 与操作系统主题同步

        .. image:: ../../images/sync_with_os_theme.gif
            :class: dark-light


**特性:**

* 扁平化的深色/浅色主题
* 支持 PySide, PyQt 和 PyInstaller
* 与操作系统的主题和色调同步（Mac, Windows, Linux）
* 解决 Qt 版本之间的样式差异
* 提供深色/浅色主题的 QPalette
* :ref:`覆盖 Qt 旧版标准图标 <how_to_use:Use overridden Qt default icons>`。

++++

.. grid::
    :gutter: 2

    .. grid-item-card:: 安装指南
        :text-align: center
        :link: installation_guide
        :link-type: doc
        :class-item: sd-text-nowrap

        :material-regular:`install_desktop;5em;sd-text-primary`
        ^^^

    .. grid-item-card:: 如何使用
        :text-align: center
        :link: how_to_use
        :link-type: doc
        :class-item: sd-text-nowrap

        :material-regular:`menu_book;5em;sd-text-primary`
        ^^^

    .. grid-item-card:: API 参考
        :text-align: center
        :link: reference/index
        :link-type: doc
        :class-item: sd-text-nowrap

        :material-regular:`library_books;5em;sd-text-primary`
        ^^^

    .. grid-item-card:: 贡献
        :text-align: center
        :link: contributing
        :link-type: doc
        :class-item: sd-text-nowrap

        :material-regular:`person_add;5em;sd-text-primary`
        ^^^

.. toctree::
   :maxdepth: 2
   :hidden:

   安装指南<installation_guide.rst>
   如何使用<how_to_use.rst>
   API 参考<reference/index.rst>
   贡献<contributing.rst>