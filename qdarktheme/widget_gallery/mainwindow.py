"""Main module of widget gallery."""
import qdarktheme
from qdarktheme.qtpy.QtCore import QDir, Qt, Slot
from qdarktheme.qtpy.QtGui import QAction, QActionGroup, QFont, QIcon
from qdarktheme.qtpy.QtWidgets import (
    QApplication,
    QColorDialog,
    QDockWidget,
    QFileDialog,
    QFontDialog,
    QMainWindow,
    QMenuBar,
    QSizePolicy,
    QStackedWidget,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QToolButton,
    QWidget,
)
from qdarktheme.util import get_qdarktheme_root_path
from qdarktheme.widget_gallery.home_ui import HomeUI


class _DockUI:
    def setup_ui(self, main_win: QMainWindow) -> None:
        # Attribute
        left_dock = QDockWidget("Left dock")
        right_dock = QDockWidget("Right dock")
        top_dock = QDockWidget("Top dock")
        bottom_dock = QDockWidget("Bottom dock")

        # Setup ui
        left_dock.setWidget(QTextEdit("This is the left widget."))
        right_dock.setWidget(QTextEdit("This is the right widget."))
        top_dock.setWidget(QTextEdit("This is the top widget."))
        bottom_dock.setWidget(QTextEdit("This is the bottom widget."))
        for dock in (left_dock, right_dock, top_dock, bottom_dock):
            dock.setAllowedAreas(
                Qt.DockWidgetArea.LeftDockWidgetArea
                | Qt.DockWidgetArea.RightDockWidgetArea
                | Qt.DockWidgetArea.BottomDockWidgetArea
                | Qt.DockWidgetArea.TopDockWidgetArea
            )

        # Layout
        main_win.setCentralWidget(QTextEdit("This is the central widget."))
        main_win.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, left_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, right_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, top_dock)
        main_win.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, bottom_dock)


class _WidgetGalleryUI:
    def setup_ui(self, main_win: QMainWindow) -> None:
        # Actions
        self.action_change_home = QAction(QIcon("icons:home_24dp.svg"), "Move to home")
        self.action_change_dock = QAction(QIcon("icons:flip_to_front_24dp.svg"), "Move to dock")
        self.action_open_folder = QAction(QIcon("icons:folder_open_24dp.svg"), "Open folder dialog")
        self.action_open_color_dialog = QAction(QIcon("icons:palette_24dp.svg"), "Open color dialog")
        self.action_open_font_dialog = QAction(QIcon("icons:font_download_24dp.svg"), "Open font dialog")
        self.action_enable = QAction(QIcon("icons:circle_24dp.svg"), "Enable")
        self.action_disable = QAction(QIcon("icons:clear_24dp.svg"), "Disable")
        self.actions_theme = [QAction(theme, main_win) for theme in ["dark", "light"]]

        action_group_toolbar = QActionGroup(main_win)

        # Widgets
        self.central_window = QMainWindow()
        self.stack_widget = QStackedWidget()

        activitybar = QToolBar("activitybar")
        toolbar = QToolBar("Toolbar")
        statusbar = QStatusBar()
        menubar = QMenuBar()
        tool_btn_settings, tool_btn_theme, tool_btn_enable, tool_btn_disable = (QToolButton() for _ in range(4))

        spacer = QToolButton()

        # Setup Actions
        self.action_change_home.setCheckable(True)
        self.action_change_dock.setCheckable(True)
        self.action_change_home.setChecked(True)
        action_group_toolbar.addAction(self.action_change_home)
        action_group_toolbar.addAction(self.action_change_dock)

        # Setup Widgets
        spacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        spacer.setEnabled(False)

        activitybar.setMovable(False)
        activitybar.addActions((self.action_change_home, self.action_change_dock))
        activitybar.addWidget(spacer)
        activitybar.addWidget(tool_btn_settings)

        tool_btn_settings.setIcon(QIcon("icons:settings_24dp.svg"))
        tool_btn_settings.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        tool_btn_enable.setDefaultAction(self.action_enable)
        tool_btn_disable.setDefaultAction(self.action_disable)
        tool_btn_theme.setIcon(QIcon("icons:contrast_24dp.svg"))
        tool_btn_theme.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        toolbar.addActions((self.action_open_folder, self.action_open_color_dialog, self.action_open_font_dialog))
        toolbar.addSeparator()
        toolbar.addWidget(tool_btn_theme)

        statusbar.addPermanentWidget(tool_btn_enable)
        statusbar.addPermanentWidget(tool_btn_disable)
        statusbar.showMessage("Enable")

        menu_toggle = menubar.addMenu("&Toggle")
        menu_toggle.addActions((self.action_enable, self.action_disable))
        menu_theme = menubar.addMenu("&Theme")
        menu_theme.addActions(self.actions_theme)
        menu_dialog = menubar.addMenu("&Dialog")
        menu_dialog.addActions((self.action_open_folder, self.action_open_color_dialog, self.action_open_font_dialog))

        tool_btn_settings.setMenu(menu_toggle)
        tool_btn_theme.setMenu(menu_theme)

        self.action_enable.setEnabled(False)

        # Layout
        stack_1 = QWidget()
        HomeUI().setup_ui(stack_1)
        self.stack_widget.addWidget(stack_1)
        stack_2 = QMainWindow()
        _DockUI().setup_ui(stack_2)
        self.stack_widget.addWidget(stack_2)

        self.central_window.setCentralWidget(self.stack_widget)
        self.central_window.addToolBar(toolbar)

        main_win.setCentralWidget(self.central_window)
        main_win.addToolBar(Qt.ToolBarArea.LeftToolBarArea, activitybar)
        main_win.setMenuBar(menubar)
        main_win.setStatusBar(statusbar)


class WidgetGallery(QMainWindow):
    """The main window class of example app."""

    def __init__(self) -> None:
        """Initialize the WidgetGallery class."""
        super().__init__()
        QDir.addSearchPath("icons", f"{get_qdarktheme_root_path().as_posix()}/widget_gallery/svg")
        self._ui = _WidgetGalleryUI()
        self._ui.setup_ui(self)

        # Signal
        self._ui.action_change_home.triggered.connect(self._change_page)
        self._ui.action_change_dock.triggered.connect(self._change_page)
        self._ui.action_open_folder.triggered.connect(
            lambda: QFileDialog.getOpenFileName(self, "Open File", options=QFileDialog.Option.DontUseNativeDialog)
        )
        self._ui.action_open_color_dialog.triggered.connect(
            lambda: QColorDialog.getColor(parent=self, options=QColorDialog.ColorDialogOption.DontUseNativeDialog)
        )
        self._ui.action_open_font_dialog.triggered.connect(
            lambda: QFontDialog.getFont(QFont(), parent=self, options=QFontDialog.FontDialogOption.DontUseNativeDialog)
        )
        self._ui.action_enable.triggered.connect(self._toggle_state)
        self._ui.action_disable.triggered.connect(self._toggle_state)
        for action in self._ui.actions_theme:
            action.triggered.connect(self._change_theme)

    @Slot()
    def _change_page(self) -> None:
        action_name: str = self.sender().text()
        self._ui.stack_widget.setCurrentIndex(0 if action_name == "Move to home" else 1)

    @Slot()
    def _toggle_state(self) -> None:
        state: str = self.sender().text()
        self._ui.central_window.centralWidget().setEnabled(state == "Enable")
        self._ui.action_enable.setEnabled(state == "Disable")
        self._ui.action_disable.setEnabled(state == "Enable")
        self.statusBar().showMessage(state)

    @Slot()
    def _change_theme(self) -> None:
        theme: str = self.sender().text()
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet(theme))
