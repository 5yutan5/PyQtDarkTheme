"""Main module of widget gallery."""
import qdarktheme
from qdarktheme.qtpy.QtCore import QDir, Qt, Slot
from qdarktheme.qtpy.QtGui import QAction, QActionGroup, QFont, QIcon
from qdarktheme.qtpy.QtWidgets import (
    QApplication,
    QColorDialog,
    QFileDialog,
    QFontDialog,
    QLabel,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QSizePolicy,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QToolButton,
    QWidget,
)
from qdarktheme.util import get_qdarktheme_root_path
from qdarktheme.widget_gallery.ui.dock_ui import DockUI
from qdarktheme.widget_gallery.ui.frame_ui import FrameUI
from qdarktheme.widget_gallery.ui.widgets_ui import WidgetsUI


class _WidgetGalleryUI:
    def setup_ui(self, main_win: QMainWindow) -> None:
        # Actions
        self.action_open_folder = QAction(QIcon("icons:folder_open_24dp.svg"), "Open folder dialog")
        self.action_open_color_dialog = QAction(QIcon("icons:palette_24dp.svg"), "Open color dialog")
        self.action_open_font_dialog = QAction(QIcon("icons:font_download_24dp.svg"), "Open font dialog")
        self.action_enable = QAction(QIcon("icons:circle_24dp.svg"), "Enable")
        self.action_disable = QAction(QIcon("icons:clear_24dp.svg"), "Disable")
        self.actions_theme = [QAction(theme, main_win) for theme in ["dark", "light"]]
        self.actions_page = (
            QAction(QIcon("icons:widgets_24dp.svg"), "Move to widgets"),
            QAction(QIcon("icons:flip_to_front_24dp.svg"), "Move to dock"),
            QAction(QIcon("icons:crop_din_24dp.svg"), "Move to frame"),
        )
        self.actions_message_box = (
            QAction(text="Open question dialog"),
            QAction(text="Open information dialog"),
            QAction(text="Open warning dialog"),
            QAction(text="Open critical dialog"),
        )
        self.actions_corner_radius = (QAction(text="rounded"), QAction(text="sharp"))

        action_group_toolbar = QActionGroup(main_win)

        # Widgets
        self.central_window = QMainWindow()
        self.stack_widget = QStackedWidget()
        self.toolbar = QToolBar("Toolbar")

        activitybar = QToolBar("activitybar")
        statusbar = QStatusBar()
        menubar = QMenuBar()
        tool_btn_settings, tool_btn_theme, tool_btn_enable, tool_btn_disable, tool_btn_message_box = (
            QToolButton() for _ in range(5)
        )

        spacer = QToolButton()

        # Setup Actions
        for action in self.actions_page:
            action.setCheckable(True)
            action_group_toolbar.addAction(action)
        self.actions_page[0].setChecked(True)

        # Setup Widgets
        spacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        spacer.setEnabled(False)

        activitybar.setMovable(False)
        activitybar.addActions(self.actions_page)
        activitybar.addWidget(spacer)
        activitybar.addWidget(tool_btn_settings)

        tool_btn_settings.setIcon(QIcon("icons:settings_24dp.svg"))
        tool_btn_settings.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        tool_btn_enable.setDefaultAction(self.action_enable)
        tool_btn_disable.setDefaultAction(self.action_disable)
        tool_btn_message_box.setIcon(QIcon("icons:announcement_24dp.svg"))
        tool_btn_message_box.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        tool_btn_theme.setIcon(QIcon("icons:contrast_24dp.svg"))
        tool_btn_theme.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        self.toolbar.addActions((self.action_open_folder, self.action_open_color_dialog, self.action_open_font_dialog))
        self.toolbar.addSeparator()
        self.toolbar.addWidget(QLabel("Popup"))
        self.toolbar.addWidget(tool_btn_message_box)
        self.toolbar.addWidget(tool_btn_theme)

        statusbar.addPermanentWidget(tool_btn_enable)
        statusbar.addPermanentWidget(tool_btn_disable)
        statusbar.showMessage("Enable")

        menu_toggle = menubar.addMenu("&Toggle")
        menu_toggle.addActions((self.action_enable, self.action_disable))
        menu_theme = menubar.addMenu("&Theme")
        menu_theme.addActions(self.actions_theme)
        menu_dialog = menubar.addMenu("&Dialog")
        menu_option = menubar.addMenu("&Option")
        menu_option.addActions(self.actions_corner_radius)
        menu_dialog.addActions((self.action_open_folder, self.action_open_color_dialog, self.action_open_font_dialog))
        menu_message_box = menu_dialog.addMenu("&Messages")
        menu_message_box.addActions(self.actions_message_box)

        tool_btn_settings.setMenu(menu_toggle)
        tool_btn_theme.setMenu(menu_theme)
        tool_btn_message_box.setMenu(menu_message_box)

        self.action_enable.setEnabled(False)

        # Layout
        for ui in (WidgetsUI, DockUI, FrameUI):
            container = QWidget()
            ui().setup_ui(container)
            self.stack_widget.addWidget(container)

        self.central_window.setCentralWidget(self.stack_widget)
        self.central_window.addToolBar(self.toolbar)

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
        self._theme = "dark"
        self._border_radius = "rounded"

        # Signal
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
        for action in self._ui.actions_page:
            action.triggered.connect(self._change_page)
        for action in self._ui.actions_message_box:
            action.triggered.connect(self._popup_message_box)
        for action in self._ui.actions_corner_radius:
            action.triggered.connect(self._change_corner_radius)

    @Slot()
    def _change_page(self) -> None:
        action_name: str = self.sender().text()  # type: ignore
        if "widgets" in action_name:
            index = 0
        elif "dock" in action_name:
            index = 1
        else:
            index = 2
        self._ui.stack_widget.setCurrentIndex(index)

    @Slot()
    def _toggle_state(self) -> None:
        state: str = self.sender().text()  # type: ignore
        self._ui.central_window.centralWidget().setEnabled(state == "Enable")
        self._ui.toolbar.setEnabled(state == "Enable")
        self._ui.action_enable.setEnabled(state == "Disable")
        self._ui.action_disable.setEnabled(state == "Enable")
        self.statusBar().showMessage(state)

    @Slot()
    def _change_theme(self) -> None:
        self._theme = self.sender().text()  # type: ignore
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet(self._theme, self._border_radius))

    @Slot()
    def _change_corner_radius(self) -> None:
        self._border_radius: str = self.sender().text()  # type: ignore
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet(self._theme, self._border_radius))

    @Slot()
    def _popup_message_box(self) -> None:
        action_name: str = self.sender().text()  # type: ignore
        if "question" in action_name:
            QMessageBox.question(self, "Question", "Question")
        elif "information" in action_name:
            QMessageBox.information(self, "Information", "Information")
        elif "warning" in action_name:
            QMessageBox.warning(self, "Warning", "Warning")
        elif "critical" in action_name:
            QMessageBox.critical(self, "Critical", "Critical")
