How to use PyQtDarkTheme
========================


Apply dark theme to your Qt Application
---------------------------------------
PyQtDarkTheme applies a flat theme to your Qt applications.

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

Enable HiDPI
------------

If you want to enable HiDPI, you can use ``qdarktheme.enable_hi_dpi()``. For Qt6 bindings, HiDPI “just works” without using this function.

.. code-block:: python

    # enable_hi_dpi() must be called before instantiation of QApplication.
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)

Toggle dark/light Theme
-----------------------

If you add ``theme`` argument as "auto", your Qt Application sync with OS's theme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            qdarktheme.setup_theme("auto")

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/sync_with_os_theme.py

You can also switch between light and dark theme manually.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            combo_box = QComboBox()
            combo_box.addItems(qdarktheme.get_themes())
            combo_box.currentTextChanged.connect(qdarktheme.setup_theme)

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/toggle_dark_light.py

Toggle dark/light Theme with pyqtgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also switch between light and dark theme with pyqtgraph.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            def toggle_theme(theme) -> None:
                qdarktheme.setup_theme(theme)
                plot_widget.setBackground("k" if theme == "dark" else "w")


            signal.connect(toggle_theme)

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/toggle_with_pyqtgraph.py

Theme customization
-------------------

You can customize theme color.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/customize_color/customize_accent_color.py

    .. tab-item:: Result

        .. image:: ../../examples/customize_color/customize_accent_color.png
            :class: dark-light


You can also change border corner shape.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qdarktheme.setup_theme(corner_shape="sharp")

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/customize_style/change_corner_to_sharp.py

    .. tab-item:: Result

        .. image:: ../../examples/customize_style/change_corner_to_sharp.png
            :class: dark-light

Append your own stylesheets
---------------------------

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qss = """
            QPushButton {
                border-width: 2px;
                border-style: dashed;
            }
            """
            qdarktheme.setup_theme(additional_qss=qss)

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/customize_style/append_stylesheet.py

    .. tab-item:: Result

        .. image:: ../../examples/customize_style/append_stylesheet.png
            :class: dark-light

Use overridden Qt default icons
-------------------------------

If you setup theme with ``qdarktheme.setup_theme``, qdarktheme override ``QStyle.standardIcon()``. So you can easily use some `Google Material Design Icons <https://fonts.google.com/icons>`_. And these icons change color that adjust to theme when theme is changed.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            save_pixmap = QStyle.StandardPixmap.SP_DialogSaveButton
            save_icon = win.style().standardIcon(save_pixmap)

            push_button = QPushButton("Save")
            push_button.setIcon(save_icon)

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/icons/use_standard_icons.py

    .. tab-item:: Result

        .. image:: ../../examples/icons/use_standard_icons.png

    .. tab-item:: Gallery

        .. image:: ../../images/standard_icons.png


Use QPalette to your Qt Application
-----------------------------------

You can apply dark and light color to your Qt Application using QPalette of PyQtDarkTheme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qdarktheme.load_palette()

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/qpalette/apply_dark_palette.py

    .. tab-item:: Gallery

        .. image:: ../../images/widget_gallery_dark_qpalette.png
            :class: dark-light

And you can get theme color from QPalette of PyQtDarkTheme.

.. code-block:: Python

    import qdarktheme

    dark_palette = qdarktheme.load_palette()
    link_color = dark_palette.link().color()
    link_rgb = link_color.getRgb()

Use stylesheet
--------------

If you want to use Qt stylesheet of PyQtDarkTheme, use following function.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qdarktheme.load_stylesheet()

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/use_stylesheet/apply_stylesheet.py
