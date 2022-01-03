How to use PyQtDarkTheme
========================


Apply dark theme to your Application
------------------------------------
PyQtDarkTheme applies a flat theme to your Qt applications using Qt stylesheets system.

#. PySide6
    .. code-block:: python

        import sys

        from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

        import qdarktheme

        app = QApplication(sys.argv)
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        app.exec()
#. PyQt6
    .. code-block:: python

        import sys

        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

        import qdarktheme

        app = QApplication(sys.argv)
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        app.exec()
#. PySide2
    .. code-block:: python

        import sys

        from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

        import qdarktheme

        app = QApplication(sys.argv)
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        app.exec_()
#. PyQt5
    .. code-block:: python

        import sys

        from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

        import qdarktheme

        app = QApplication(sys.argv)
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        app.exec()
#. pyqtgraph
    .. code-block:: python

        import pyqtgraph as pg
        from pyqtgraph.Qt.QtGui import QMainWindow, QPushButton

        import qdarktheme

        app = pg.mkQApp()
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)

        # Apply dark theme
        app.setStyleSheet(qdarktheme.load_stylesheet())

        main_win.show()

        pg.exec()


Toggle dark/light Theme
-----------------------

You can easily switch between light and dark theme.

.. code-block:: python

    import sys

    from PyQt6.QtCore import pyqtSlot
    from PyQt6.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QWidget

    import qdarktheme

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    combobox = QComboBox()


    @pyqtSlot(str)
    def toggle_theme(theme) -> None:
        stylesheet = qdarktheme.load_stylesheet(theme)
        QApplication.instance().setStyleSheet(stylesheet)


    combobox.addItems(qdarktheme.get_themes())
    combobox.currentTextChanged.connect(toggle_theme)

    layout = QHBoxLayout()
    layout.addWidget(combobox)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    main_win.setCentralWidget(central_widget)

    # Apply dark theme
    app.setStyleSheet(qdarktheme.load_stylesheet())

    main_win.show()

    app.exec()

On some operating systems we can detect if a dark or light mode is selected system-wide.
By using `darkdetect <https://github.com/albertosottile/darkdetect>`_, You can easily sync your application theme with this operating system theme.

.. code-block:: python

    import sys

    import darkdetect
    from PySide6.QtCore import Slot
    from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

    import qdarktheme

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    theme_label = QLabel()

    main_win.setCentralWidget(theme_label)


    @Slot()
    def sync_theme_with_system() -> None:
        theme = darkdetect.theme().lower()
        theme_label.setText(f"Theme: {theme}")
        stylesheet = qdarktheme.load_stylesheet(theme)
        QApplication.instance().setStyleSheet(stylesheet)


    app.paletteChanged.connect(sync_theme_with_system)
    sync_theme_with_system()

    main_win.show()

    app.exec()


Toggle dark/light Theme with pyqtgraph
--------------------------------------

You can also switch between light and dark theme with pyqtgraph.

.. code-block:: python

    import sys

    import pyqtgraph as pg
    from PySide6.QtCore import Slot
    from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow, QVBoxLayout, QWidget

    import qdarktheme

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    combobox = QComboBox()
    plot_widget = pg.PlotWidget()


    @Slot(str)
    def toggle_theme(theme) -> None:
        stylesheet = qdarktheme.load_stylesheet(theme)
        QApplication.instance().setStyleSheet(stylesheet)
        plot_widget.setBackground("k" if theme == "dark" else "w")


    combobox.addItems(qdarktheme.get_themes())
    combobox.currentTextChanged.connect(toggle_theme)

    layout = QVBoxLayout()
    layout.addWidget(combobox)
    layout.addWidget(plot_widget)

    central_widget = QWidget()
    central_widget.setLayout(layout)
    main_win.setCentralWidget(central_widget)

    # Apply dark theme
    app.setStyleSheet(qdarktheme.load_stylesheet())

    main_win.show()

    app.exec()
