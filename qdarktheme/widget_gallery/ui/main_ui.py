# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from qdarktheme.qtpy.QtCore import Qt
from qdarktheme.qtpy.QtGui import QAction, QActionGroup, QIcon
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
from qdarktheme.widget_gallery.ui.sub_ui import DockUI, HomeUI


class UI:
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
        tool_btn_settings, tool_btn_theme, tool_btn_enable, tool_btn_disable = [QToolButton() for _ in range(4)]

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

        # setup custom property
        activitybar.setProperty("type", "activitybar")

        # layout
        stack_1 = QWidget()
        HomeUI().setup_ui(stack_1)
        self.stack_widget.addWidget(stack_1)
        stack_2 = QMainWindow()
        DockUI().setup_ui(stack_2)
        self.stack_widget.addWidget(stack_2)

        self.central_window.setCentralWidget(self.stack_widget)
        self.central_window.addToolBar(toolbar)

        main_win.setCentralWidget(self.central_window)
        main_win.addToolBar(Qt.ToolBarArea.LeftToolBarArea, activitybar)
        main_win.setMenuBar(menubar)
        main_win.setStatusBar(statusbar)
