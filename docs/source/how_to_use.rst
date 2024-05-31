如何使用 PyQtDarkTheme
========================


将深色主题应用于您的 Qt 应用程序
---------------------------------------
PyQtDarkTheme 为您的 Qt 应用程序提供了一个扁平主题。

.. tab-set::

    .. tab-item:: PySide6

        .. literalinclude:: ../../examples/apply_theme/pyside6.py

    .. tab-item:: PyQt6

        .. literalinclude:: ../../examples/apply_theme/pyqt6.py

    .. tab-item:: PySide2

        .. literalinclude:: ../../examples/apply_theme/pyside2.py

    .. tab-item:: PyQt5

        .. literalinclude:: ../../examples/apply_theme/pyqt5.py

    .. tab-item:: pyqtgraph

        .. literalinclude:: ../../examples/apply_theme/pyqtgraph.py

启用 HiDPI
------------

如果您想启用 HiDPI，可以使用 ``qdarktheme.enable_hi_dpi()``。对于 Qt6 绑定，无需使用此函数，HiDPI 就可以正常工作。

.. code-block:: python

    # 必须在 QApplication 实例化之前调用 enable_hi_dpi()。
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)

切换深/浅主题
-----------------------

如果您将 ``theme`` 参数设置为 "auto"，您的 Qt 应用程序将与操作系统的主题同步。在 macOS 上，qdarktheme 也会与突出颜色同步。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: python

            qdarktheme.setup_theme("auto")

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/toggle_theme/sync_with_os_theme.py

您还可以手动切换深色和浅色主题。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: python

            combo_box = QComboBox()
            combo_box.addItems(qdarktheme.get_themes())
            combo_box.currentTextChanged.connect(qdarktheme.setup_theme)

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/toggle_theme/toggle_dark_light.py

使用 pyqtgraph 切换深/浅主题
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

您也可以使用 pyqtgraph 切换深色和浅色主题。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: python

            def toggle_theme(theme) -> None:
                qdarktheme.setup_theme(theme)
                plot_widget.setBackground("k" if theme == "dark" else "w")


            signal.connect(toggle_theme)

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/toggle_theme/toggle_with_pyqtgraph.py

主题定制
-------------------

您可以定制主题颜色。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: python

            qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/customize_color/customize_accent_color.py

    .. tab-item:: 结果

        .. image:: ../../examples/customize_color/customize_accent_color.png
            :class: dark-light


您还可以更改边框圆角形状。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: Python

            qdarktheme.setup_theme(corner_shape="sharp")

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/customize_style/change_corner_to_sharp.py

    .. tab-item:: 结果

        .. image:: ../../examples/customize_style/change_corner_to_sharp.png
            :class: dark-light

附加您自己的样式表
---------------------------

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: Python

            qss = """
            QPushButton {
                border-width: 2px;
                border-style: dashed;
            }
            """
            qdarktheme.setup_theme(additional_qss=qss)

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/customize_style/append_stylesheet.py

    .. tab-item:: 结果

        .. image:: ../../examples/customize_style/append_stylesheet.png
            :class: dark-light

使用覆盖的 Qt 默认图标
-------------------------------

如果您使用 ``qdarktheme.setup_theme`` 设置主题，qdarktheme 将覆盖 ``QStyle.standardIcon()``。因此，您可以轻松使用一些 `Google Material Design Icons <https://fonts.google.com/icons>`_。当主题更改时，这些图标颜色会自动调整以适应主题。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: Python

            save_pixmap = QStyle.StandardPixmap.SP_DialogSaveButton
            save_icon = win.style().standardIcon(save_pixmap)

            push_button = QPushButton("Save")
            push_button.setIcon(save_icon)

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/icons/use_standard_icons.py

    .. tab-item:: 结果

        .. image:: ../../examples/icons/use_standard_icons.png

    .. tab-item:: 图库

        .. image:: ../../images/standard_icons.png


将 QPalette 应用于您的 Qt 应用程序
-----------------------------------

您可以使用 PyQtDarkTheme 的 QPalette 为您的 Qt 应用程序应用深色和浅色的颜色。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: Python

            qdarktheme.load_palette()

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/qpalette/apply_dark_palette.py

    .. tab-item:: 图库

        .. image:: ../../images/widget_gallery_dark_qpalette.png
            :class: dark-light

您还可以从 PyQtDarkTheme 的 QPalette 中获取主题颜色。

.. code-block:: Python

    import qdarktheme

    dark_palette = qdarktheme.load_palette()
    link_color = dark_palette.link().color()
    link_rgb = link_color.getRgb()

使用样式表
--------------

如果您想使用 PyQtDarkTheme 的 Qt 样式表，请使用以下函数。

.. tab-set::

    .. tab-item:: 源码

        .. code-block:: Python

            qdarktheme.load_stylesheet()

    .. tab-item:: 完整源码

        .. literalinclude:: ../../examples/use_stylesheet/apply_stylesheet.py
