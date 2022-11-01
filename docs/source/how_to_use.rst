How to use PyQtDarkTheme
========================


Apply dark theme to your Qt Application
---------------------------------------
PyQtDarkTheme applies a flat theme to your Qt applications using Qt stylesheets system.

.. tab-set::

    .. tab-item:: PySide6

        .. literalinclude:: ../../examples/apply_dark_theme/pyside6.py
            :start-at: import sys

    .. tab-item:: PyQt6

        .. literalinclude:: ../../examples/apply_dark_theme/pyqt6.py
            :start-at: import sys

    .. tab-item:: PySide2

        .. literalinclude:: ../../examples/apply_dark_theme/pyside2.py
            :start-at: import sys

    .. tab-item:: PyQt5

        .. literalinclude:: ../../examples/apply_dark_theme/pyqt5.py
            :start-at: import sys

    .. tab-item:: pyqtgraph

        .. literalinclude:: ../../examples/apply_dark_theme/pyqtgraph.py
            :start-at: import pyqtgraph as pg

Toggle dark/light Theme
-----------------------

You can easily switch between light and dark theme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            def toggle_theme(theme) -> None:
                stylesheet = qdarktheme.load_stylesheet(theme)
                QApplication.instance().setStyleSheet(stylesheet)


            signal.connect(toggle_theme)


    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/toggle_dark_light.py
            :start-at: import sys

On some operating systems we can detect if a dark or light mode is selected system-wide.
By using `darkdetect <https://github.com/albertosottile/darkdetect>`_, You can easily sync your application theme with this operating system theme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            def sync_theme_with_system() -> None:
                theme = darkdetect.theme().lower()
                # Return None if darkdetect fails to detect a theme.
                if theme is None:
                    theme = "dark"
                stylesheet = qdarktheme.load_stylesheet(theme)
                QApplication.instance().setStyleSheet(stylesheet)


            app.paletteChanged.connect(sync_theme_with_system)


    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/sync_system_theme.py
            :start-at: import sys

Toggle dark/light Theme with pyqtgraph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also switch between light and dark theme with pyqtgraph.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            def toggle_theme(theme) -> None:
                stylesheet = qdarktheme.load_stylesheet(theme)
                QApplication.instance().setStyleSheet(stylesheet)
                plot_widget.setBackground("k" if theme == "dark" else "w")


            signal.connect(toggle_theme)


    .. tab-item:: Full source

        .. literalinclude:: ../../examples/toggle_theme/toggle_with_pyqtgraph.py
            :start-at: import sys

Theme customization
-------------------

You can customize theme color.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: python

            qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"})

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/customize_color/customize_accent_color.py
            :start-at: import sys

    .. tab-item:: Result

        .. image:: ../../examples/customize_color/customize_accent_color.png
            :class: dark-light


You can also change border corner shape.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qdarktheme.load_stylesheet(corner_shape="sharp")

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/customize_style/change_corner_to_sharp.py
            :start-at: import sys

    .. tab-item:: Result

        .. image:: ../../examples/customize_style/change_corner_to_sharp.png
            :class: dark-light

Use QPalette to your Qt Application
-----------------------------------

You can also apply dark and light color to your Qt Application using QPalette of PyQtDarkTheme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            qdarktheme.load_palette()

    .. tab-item:: Full source

        .. literalinclude:: ../../examples/qpalette/apply_dark_palette.py
            :start-at: import sys

    .. tab-item:: Gallery

        .. image:: ../../images/widget_gallery_dark_qpalette.png
            :class: dark-light

And you can get theme color from QPalette of PyQtDarkTheme.

.. tab-set::

    .. tab-item:: Source

        .. code-block:: Python

            dark_palette = qdarktheme.load_palette()
            palette = app.palette()
            palette.setColor(QPalette.ColorRole.Link, dark_palette.link().color())

    .. tab-item:: Full Source

        .. literalinclude:: ../../examples/qpalette/get_theme_color.py
            :start-at: import sys
