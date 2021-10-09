# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtGui import QAction, QActionGroup
from qdarktheme.qtpy.QtWidgets import (
    QMainWindow,
    QMenuBar,
    QSizePolicy,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QToolButton,
    QWidget,
)
from qdarktheme.widget_gallery.icon_manager import get_icon
from qdarktheme.widget_gallery.ui.dock import DockUI
from qdarktheme.widget_gallery.ui.home import HomeUI


class UI:
    def setup_ui(self, main_win: QMainWindow) -> None:
        # Actions
        self.action_change_home = QAction(get_icon("home"), "Move to home")
        self.action_change_dock = QAction(get_icon("flip_to_front"), "Move to dock")
        self.action_open_folder = QAction(get_icon("folder_open"), "Open folder dialog")
        self.action_open_color_dialog = QAction(get_icon("palette"), "Open color dialog", main_win)
        self.action_enable = QAction(get_icon("circle"), "Enable")
        self.action_disable = QAction(get_icon("clear"), "Disable")
        self.actions_theme = [QAction(theme, main_win) for theme in ["dark", "light"]]

        self.action_group_toolbar = QActionGroup(main_win)

        # Widgets
        self.central_window = QMainWindow()
        self.stack_widget = QStackedWidget()

        activitybar = QToolBar("activitybar")
        toolbar = QToolBar("Toolbar")
        statusbar = QStatusBar()
        menubar = QMenuBar()
        tool_button_settings = QToolButton()
        tool_button_enable = QToolButton()
        tool_button_disable = QToolButton()
        tool_button_theme = QToolButton()

        self.spacer = QToolButton()

        # Setup Actions
        self.action_change_home.setCheckable(True)
        self.action_change_dock.setCheckable(True)
        self.action_change_home.setChecked(True)
        self.action_group_toolbar.addAction(self.action_change_home)
        self.action_group_toolbar.addAction(self.action_change_dock)

        # Setup Widgets
        self.spacer.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.spacer.setEnabled(False)

        activitybar.setMovable(False)
        activitybar.addActions([self.action_change_home, self.action_change_dock])
        activitybar.addWidget(self.spacer)
        activitybar.addWidget(tool_button_settings)

        tool_button_settings.setIcon(get_icon("settings"))
        tool_button_settings.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        tool_button_enable.setDefaultAction(self.action_enable)
        tool_button_disable.setDefaultAction(self.action_disable)
        tool_button_theme.setIcon(get_icon("contrast"))
        tool_button_theme.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        toolbar.addActions([self.action_open_folder, self.action_open_color_dialog])
        toolbar.addSeparator()
        toolbar.addWidget(tool_button_theme)

        statusbar.addPermanentWidget(tool_button_enable)
        statusbar.addPermanentWidget(tool_button_disable)
        statusbar.showMessage("Enable")

        menu_toggle = menubar.addMenu("&Toggle")
        menu_toggle.addActions([self.action_enable, self.action_disable])
        menu_theme = menubar.addMenu("&Theme")
        menu_theme.addActions(self.actions_theme)
        menu_dialog = menubar.addMenu("&Dialog")
        menu_dialog.addActions([self.action_open_folder, self.action_open_color_dialog])

        tool_button_settings.setMenu(menu_toggle)
        tool_button_theme.setMenu(menu_theme)

        self.action_enable.setEnabled(False)

        # setup custom property
        activitybar.setProperty("type", "activitybar")

        # layout
        stack_1 = QWidget()
        home_ui = HomeUI()
        home_ui.setup_ui(stack_1)
        self.stack_widget.addWidget(stack_1)
        stack_2 = QMainWindow()
        dock_ui = DockUI()
        dock_ui._setup_ui(stack_2)
        self.stack_widget.addWidget(stack_2)

        self.central_window.setCentralWidget(self.stack_widget)
        self.central_window.addToolBar(toolbar)

        main_win.setCentralWidget(self.central_window)
        main_win.addToolBar(Qt.ToolBarArea.LeftToolBarArea, activitybar)
        main_win.setMenuBar(menubar)
        main_win.setStatusBar(statusbar)
