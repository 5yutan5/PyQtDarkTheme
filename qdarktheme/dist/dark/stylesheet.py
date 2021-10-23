STYLE_SHEET = """

/* ==========================================================================================
 * PyQtDarkTheme.
 *
 *  Copyright (c) 2013-2014 Colin Duquesnoy
 *  Copyright (c) 2021- Yunosuke Ohsugi
 *
 *  Distributed under the terms of the MIT License.
 *   see https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/LICENSE.rst#the-mit-license-mit---code
 *
 * Original code:
 *   https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/qdarkstyle/dark/style.qss
 *
 * (see NOTICE.md in the PyQtDarkTheme root directory for details)
 * ==========================================================================================
 */

* {
    padding: 0px;
    margin: 0px;
    border: 0px;
    border-style: none;
    border-image: none;
    outline: 0;
}
QToolBar * {
    margin: 0px;
    padding: 0px;
}

/* QWidget ----------------------------------------------------------------

--------------------------------------------------------------------------- */
QWidget {
    background-color: rgba(32.000, 33.000, 36.000, 1.000);
    color: rgba(228.000, 231.000, 235.000, 1.000);
    selection-background-color: rgba(138.000, 180.000, 247.000, 1.000);
    selection-color: rgba(32.000, 33.000, 36.000, 1.000);
}
QWidget:disabled {
    color: rgba(105.000, 113.000, 119.000, 1.000);
    selection-background-color: rgba(83.000, 87.000, 91.000, 1.000);
    selection-color: rgba(105.000, 113.000, 119.000, 1.000);
}

/* Override default icons -------------------------------------------------

document: https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-icons

--------------------------------------------------------------------------- */
QWidget {
    backward-icon: url(${path}/dist/dark/svg/arrow_upward_icon-foreground_270.svg);
    forward-icon: url(${path}/dist/dark/svg/arrow_upward_icon-foreground_90.svg);
    leftarrow-icon: url(${path}/dist/dark/svg/arrow_upward_icon-foreground_270.svg);
    rightarrow-icon: url(${path}/dist/dark/svg/arrow_upward_icon-foreground_90.svg);

    dialog-ok-icon: url(${path}/dist/dark/svg/check_icon-foreground_0.svg);
    dialog-cancel-icon: url(${path}/dist/dark/svg/close_icon-foreground_0.svg);
    dialog-yes-icon: url(${path}/dist/dark/svg/check_circle_icon-foreground_0.svg);
    dialog-no-icon: url(${path}/dist/dark/svg/cancel_icon-foreground_0.svg);
    dialog-apply-icon: url(${path}/dist/dark/svg/check_icon-foreground_0.svg);
    dialog-reset-icon: url(${path}/dist/dark/svg/restart_alt_icon-foreground_0.svg);
    dialog-save-icon: url(${path}/dist/dark/svg/save_icon-foreground_0.svg);
    dialog-discard-icon: url(${path}/dist/dark/svg/delete_icon-foreground_0.svg);
    dialog-close-icon: url(${path}/dist/dark/svg/close_icon-foreground_0.svg);
    dialog-open-icon: url(${path}/dist/dark/svg/folder_open_icon-foreground_0.svg);
    dialog-help-icon: url(${path}/dist/dark/svg/help_icon-foreground_0.svg);

    filedialog-parent-directory-icon: url(${path}/dist/dark/svg/arrow_upward_icon-foreground_0.svg);
    filedialog-new-directory-icon: url(${path}/dist/dark/svg/create_new_folder_icon-foreground_0.svg);
    titlebar-close-icon: url(${path}/dist/dark/svg/close_icon-foreground_0.svg);
    titlebar-normal-icon: url(${path}/dist/dark/svg/flip_to_front_icon-foreground_0.svg);
}

QCommandLinkButton {
    qproperty-icon: url(${path}/dist/dark/svg/east_highlight_0.svg);
}

/* QMainWindow ------------------------------------------------------------

This adjusts the splitter in the dock widget, not qsplitter
examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow

--------------------------------------------------------------------------- */
QMainWindow::separator {
    width: 4px;
    height: 4px;
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QMainWindow::separator:hover,
QMainWindow::separator:pressed {
    background-color: rgba(138.000, 180.000, 247.000, 1.000);
}

/* QToolTip ---------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip

--------------------------------------------------------------------------- */
QToolTip {
    background-color: rgba(41.000, 42.000, 45.000, 1.000);
    color: rgba(228.000, 231.000, 235.000, 1.000);
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
}

/* QSizeGrip --------------------------------------------------------------

There is no size grip in modern apps. So we hide size grip.
examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip

--------------------------------------------------------------------------- */
QSizeGrip {
  width: 0;
  height: 0;
  image: none;
}

/* QStatusBar -------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar

--------------------------------------------------------------------------- */
QStatusBar {
    background-color: rgba(42.000, 43.000, 46.000, 1.000);
}
QStatusBar::item {
    border: none;
}

QStatusBar QWidget {
    background-color: transparent;
    padding: 3px;
    border-radius: 4px;
}
QStatusBar QWidget:hover {
    background-color: rgba(68.000, 70.000, 74.000, 1.000);
}
QStatusBar QWidget:pressed {
    background-color: rgba(79.000, 80.000, 84.000, 1.000);
}
QStatusBar QWidget:disabled {
    background-color: rgba(32.000, 33.000, 36.000, 1.000);
}
QStatusBar QWidget:checked {
    background-color: rgba(79.000, 80.000, 84.000, 1.000);
}

/* QCheckBox --------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox

--------------------------------------------------------------------------- */
QCheckBox:hover {
    border-bottom: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QCheckBox::indicator {
    margin: 0 0 2 10;
    height: 18px;
    width: 18px;
}

QRadioButton {
    spacing: 8px;
}
QRadioButton:hover {
    border-bottom: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QRadioButton::indicator {
    margin: 0 0 2 10;
    height: 18px;
    width: 18px;
}
QRadioButton::indicator:unchecked {
    image: url(${path}/dist/dark/svg/radio_button_unchecked_icon-foreground_0.svg);
}
QRadioButton::indicator:unchecked:disabled {
    image: url(${path}/dist/dark/svg/radio_button_unchecked_icon-foreground-disabled_0.svg);
}
QRadioButton::indicator:checked {
    image: url(${path}/dist/dark/svg/radio_button_checked_highlight_0.svg);
}
QRadioButton::indicator:checked:disabled {
    image: url(${path}/dist/dark/svg/radio_button_checked_icon-foreground-disabled_0.svg);
}

/* QGroupBox QRadioButton -------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox
examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton

--------------------------------------------------------------------------- */
QGroupBox {
    font-weight: bold;
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
    padding: 2px;
    margin: 9px 0 4px 0;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 7px;
    top: 2px;
    spacing: 6px;
    margin: 0 2px 0 2px;
}

/* QMenuBar ---------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar

--------------------------------------------------------------------------- */
QMenuBar {
    background-color: rgba(32.000, 33.000, 36.000, 1.000);
    padding: 2px;
    border-bottom: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
}
QMenuBar::item {
    background: transparent;
    padding: 4px;
}
QMenuBar::item:selected {
    padding: 4px;
    background-color: rgba(68.000, 70.000, 77.000, 1.000);
    border-radius: 4px;
}
QMenuBar::item:pressed {
    padding: 4px;
    margin-bottom: 0px;
    padding-bottom: 0px;
}

/* QToolBar ---------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar

--------------------------------------------------------------------------- */
QToolBar {
    background-color: rgba(51.000, 51.000, 51.000, 1.000);
    padding: 1px;
    font-weight: bold;
    spacing: 2px;
    margin: 1px;
}
QToolBar::handle:horizontal {
    width: 20px;
    image: url(${path}/dist/dark/svg/drag_indicator_horizontal_icon-foreground_0.svg);
}
QToolBar::handle:vertical {
    height: 20px;
    image: url(${path}/dist/dark/svg/drag_indicator_horizontal_icon-foreground_90.svg);
}
QToolBar::separator {
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QToolBar::separator:horizontal {
    width: 2px;
    margin: 0 6px;
}
QToolBar::separator:vertical {
    height: 2px;
    margin: 6px 0;
}

QToolBar > QToolButton {
    background-color: transparent;
    padding: 3px;
    border-radius: 4px;
}
QToolBar > QToolButton:hover {
    background-color: rgba(68.000, 70.000, 74.000, 1.000);
}
QToolBar > QToolButton:pressed {
    background-color: rgba(79.000, 80.000, 84.000, 1.000);
}
QToolBar > QToolButton:checked {
    background-color: rgba(79.000, 80.000, 84.000, 1.000);
}
QToolBar > QToolButton#qt_toolbar_ext_button {
    image: url(${path}/dist/dark/svg/double_arrow_icon-foreground_0.svg);
}
QToolBar > QToolButton#qt_toolbar_ext_button:disabled {
    image: url(${path}/dist/dark/svg/double_arrow_icon-foreground-disabled_0.svg);
}

/* QMenu ------------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu

--------------------------------------------------------------------------- */
QMenu {
    background-color: rgba(41.000, 42.000, 45.000, 1.000);
    padding: 8px 0;
}
QMenu::separator {
    height: 1px;
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QMenu::item {
    padding: 4px 28px;
}
QMenu::item:selected {
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QMenu::icon {
    padding-left: 10px;
    width: 14px;
    height: 14px;
}
QMenu::right-arrow {
    margin: 2px;
    padding-left: 12px;
    height: 20px;
    width: 20px;
    image: url(${path}/dist/dark/svg/chevron_right_icon-foreground_0.svg);
}
QMenu::right-arrow:disabled {
    image: url(${path}/dist/dark/svg/chevron_right_icon-foreground-disabled_0.svg);
}

/* QScrollBar -------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar

--------------------------------------------------------------------------- */
QScrollBar:horizontal {
    height: 12px;
    margin: 0 12px;
}
QScrollBar:vertical {
    width: 12px;
    margin: 12px 0;
}
QScrollBar::handle {
    background-color: rgba(65.000, 66.000, 66.000, 1.000);
    margin: 1px;
    border-radius: 5px;
}
QScrollBar::handle:hover {
    background-color: rgba(94.000, 94.000, 94.000, 1.000);
}
QScrollBar::handle:horizontal {
    min-width: 8px;
}
QScrollBar::handle:vertical {
    min-height: 8px;
}
/* There is no support button in modern apps. So we hide button of QScrollBar. */
QScrollBar::sub-line, QScrollBar::add-line {
    width: 0;
    height: 0;
}
/* We hide background of QScrollBar */
QScrollBar::sub-page, QScrollBar::add-page {
    background-color: transparent;
}

/* QProgressBar -----------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar

--------------------------------------------------------------------------- */
QProgressBar {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
    text-align: center;
    color: rgba(228.000, 231.000, 235.000, 1.000);
}
QProgressBar::chunk {
    background-color: rgba(138.000, 180.000, 247.000, 1.000);
    border-radius: 3px;
}
QProgressBar::chunk:disabled {
    background-color: rgba(83.000, 87.000, 91.000, 1.000);
}

/* QPushButton ------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton

--------------------------------------------------------------------------- */
QPushButton {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    padding: 4px 8px;
    border-radius: 4px;
    color: rgba(138.000, 180.000, 247.000, 1.000);
}
QPushButton:hover {
    background-color: rgba(30.000, 43.000, 60.000, 1.000);
}
QPushButton:pressed {
    background-color: rgba(46.000, 70.000, 94.000, 1.000);
}
QPushButton:checked {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QPushButton:disabled {
    border-color: rgba(63.000, 64.000, 66.000, 1.000);
}

QPushButton[flat=true]:!checked {
    border-color: transparent;
}

/* QDialogButtonBox -------------------------------------------------------

--------------------------------------------------------------------------- */
QDialogButtonBox QPushButton {
    min-width: 65px;
}

/* QToolButton ------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton

--------------------------------------------------------------------------- */
QToolButton {
    padding: 5px;
    border-radius: 2px;
    spacing: 2px;
}
QToolButton:hover {
    background-color: rgba(30.000, 43.000, 60.000, 1.000);
}
QToolButton:pressed {
    background-color: rgba(46.000, 70.000, 94.000, 1.000);
}
QToolButton:selected,
QToolButton:checked {
    background-color: rgba(46.000, 70.000, 94.000, 1.000);
}
QToolButton::checked:disabled {
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QToolButton::menu-button {
    padding: 1px;
    border-radius: 4px;
    width: 12px;
}
QToolButton::menu-button {
    border: 1px solid transparent;
}
QToolButton::menu-button:hover, QToolButton::menu-button:checked:hover {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QToolButton::menu-indicator {
    height: 18px;
    width: 18px;
    top: 6px;
    left: 3px;
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground_180.svg);
}
QToolButton::menu-indicator:disabled {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground-disabled_180.svg);
}
QToolButton::menu-arrow {
    height: 8px;
    width: 8px;
}
QToolButton[popupMode="1"] { /* MenuButtonPopup */
    padding-right: 14px;
}

/* QComboBox --------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox

--------------------------------------------------------------------------- */
QComboBox {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
    min-height: 1.5em;
    padding: 0 4px;
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QComboBox:focus,
QComboBox:open {
    border: 1px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QComboBox::drop-down {
    subcontrol-position: center right;
    border: none;
    padding-right: 4px;
}
QComboBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground_180.svg);
}
QComboBox::down-arrow:disabled {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground-disabled_180.svg);
}
/* Setting color background color of selected item when editable is false. */
QComboBox::item:selected {
    border: none;  /* With this setting, the indicator border disappears. */
    background-color: rgba(0.000, 72.000, 117.000, 1.000);
    color: rgba(228.000, 231.000, 235.000, 1.000);
}

QComboBox QAbstractItemView {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    selection-background-color: rgba(0.000, 72.000, 117.000, 1.000);
    selection-color: rgba(228.000, 231.000, 235.000, 1.000);
    padding: 2px;
}

/* QSlider ----------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider

--------------------------------------------------------------------------- */
QSlider {
    padding: 2px 0;
}
QSlider:focus {
    border: none;
}
QSlider::groove {
    border-radius: 2px;
}
QSlider::groove:horizontal {
    height: 4px;
}
QSlider::groove:vertical {
    width: 4px;
}
QSlider::sub-page, QSlider::handle {
    background-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QSlider::sub-page:disabled,
QSlider::add-page:disabled,
QSlider::handle:disabled {
    background-color: rgba(83.000, 87.000, 91.000, 1.000);
}
QSlider::add-page {
    background-color: rgba(54.000, 86.000, 140.000, 1.000);
}
QSlider::handle:hover {
    background-color: rgba(127.000, 166.000, 228.000, 1.000);
}
QSlider::handle:horizontal {
    width: 16px;
    height: 8px;
    margin: -6px 0;
    border-radius: 8px;
}
QSlider::handle:vertical {
    width: 8px;
    height: 16px;
    margin: 0 -6px;
    border-radius: 8px;
}

/* QTabWidget QTabBar -----------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar

--------------------------------------------------------------------------- */
QTabWidget::pane {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 3px;
}

QTabBar::close-button:selected {
    image: url(${path}/dist/dark/svg/close_icon-foreground_0.svg);
}
QTabBar::close-button:!selected {
    image: url(${path}/dist/dark/svg/close_tabbar-button-inselected_0.svg)
}
QTabBar::close-button:disabled {
    image: url(${path}/dist/dark/svg/close_icon-foreground-disabled_0.svg);
}
QTabBar::close-button:hover {
    background-color: rgba(85.000, 128.000, 173.000, 1.000);
    border-radius: 4px
}
QTabBar::close-button:hover:!selected {
    background-color: rgba(50.000, 71.000, 99.000, 1.000);
}
QTabBar::tab {
    padding: 3px;
}
QTabBar::tab:hover {
    background-color: rgba(30.000, 43.000, 60.000, 1.000);
}
QTabBar::tab:selected {
    color: rgba(138.000, 180.000, 247.000, 1.000);
    background-color: rgba(46.000, 70.000, 94.000, 1.000);
}
QTabBar::tab:selected:disabled {
    background-color: rgba(83.000, 87.000, 91.000, 1.000);
    color: rgba(105.000, 113.000, 119.000, 1.000);
}
QTabBar::tab:top {
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
    border-bottom: 2px solid rgba(63.000, 64.000, 66.000, 1.000);
    margin-left: 4px;
}
QTabBar::tab:top:selected {
    border-bottom: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:top:hover {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:top:selected:disabled {
    border-color: rgba(83.000, 87.000, 91.000, 1.000);
}
QTabBar::tab:bottom {
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    border-top: 2px solid rgba(63.000, 64.000, 66.000, 1.000);
    margin-left: 4px;
}
QTabBar::tab:bottom:selected {
    border-top: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:bottom:hover {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:bottom:selected:disabled {
    border-color: rgba(83.000, 87.000, 91.000, 1.000);
}
QTabBar::tab:left {
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    border-right: 2px solid rgba(63.000, 64.000, 66.000, 1.000);
    margin-top: 4px;
}
QTabBar::tab:left:selected {
    border-right: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:left:hover {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:left:selected:disabled {
    border-color: rgba(83.000, 87.000, 91.000, 1.000);
}
QTabBar::tab:right {
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    border-left: 2px solid rgba(63.000, 64.000, 66.000, 1.000);
    margin-top: 4px;
}
QTabBar::tab:right:selected {
    border-left: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:right:hover {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QTabBar::tab:right:selected:disabled {
    border-color: rgba(83.000, 87.000, 91.000, 1.000);
}

/* QDockWiget -------------------------------------------------------------

--------------------------------------------------------------------------- */
QDockWidget {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
}
QDockWidget::title {
  /* Better size for title bar */
    padding: 3px;
    spacing: 4px;
    border: none;
    background-color: rgba(0.000, 0.000, 0.000, 1.000);
}
/*
Hover is already set in the QToolbutton:hover, but it is not worked in
QDockWidget::title. Therefore, we need to set it again here.
*/
QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background-color: rgba(30.000, 43.000, 60.000, 1.000);
    border-radius: 2px
}

/* QFrame -----------------------------------------------------------------

https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe

--------------------------------------------------------------------------- */
QFrame {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    padding: 1px;
    border-radius: 4px;
}

/* QLCDNumber -------------------------------------------------------------

--------------------------------------------------------------------------- */
QLCDNumber {
    color: rgba(228.000, 231.000, 235.000, 1.000);
    min-width: 2em;
    margin: 2px;
}

/* QLabel -----------------------------------------------------------------

https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe

--------------------------------------------------------------------------- */
QLabel {
    border: none;
}

/* QStackedWidget ---------------------------------------------------------

--------------------------------------------------------------------------- */
QStackedWidget {
    border: none;
}

/* QToolBox ---------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox

--------------------------------------------------------------------------- */
QToolBox {
    border: none;
}
QToolBox:selected {
    border: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QToolBox::tab {
    background-color: rgba(0.000, 0.000, 0.000, 1.000);
    border-bottom: 2px solid rgba(63.000, 64.000, 66.000, 1.000);
}
QToolBox::tab:selected {
    border-bottom: 2px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QToolBox::tab:selected:disabled {
    border-bottom: 2px solid rgba(83.000, 87.000, 91.000, 1.000);
}

/* QSplitter --------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter

--------------------------------------------------------------------------- */
QSplitter {
    border: none;
}
QSplitter::handle {
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
    margin: 1px 3px;
}
QSplitter::handle:hover {
    background-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QSplitter::handle:horizontal {
    width: 5px;
    image: url(${path}/dist/dark/svg/horizontal_rule_icon-foreground_90.svg);
}
QSplitter::handle:horizontal:disabled {
    image: url(${path}/dist/dark/svg/horizontal_rule_icon-foreground-disabled_90.svg);
}
QSplitter::handle:vertical {
    height: 5px;
    image: url(${path}/dist/dark/svg/horizontal_rule_icon-foreground_0.svg);
}
QSplitter::handle:vertical:disabled {
    image: url(${path}/dist/dark/svg/horizontal_rule_icon-foreground-disabled_0.svg);
}

/*
QSplitterHandle is the QSplitter handle class.
[QSplitter::handle:hover] is enabled by the following settings.
Warning: This setting is not mentioned in the documentation.
*/
QSplitterHandle::item:hover {}

/* QAbstractScrollArea ----------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea

--------------------------------------------------------------------------- */
QAbstractScrollArea {
    selection-background-color: rgba(0.000, 72.000, 117.000, 1.000);
    selection-color: rgba(228.000, 231.000, 235.000, 1.000);
    margin: 1px;
}
QAbstractScrollArea:disabled {
    selection-background-color: rgba(228.000, 231.000, 235.000, 1.000);
}

/* QTextEdit QPlainTextEdit------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets

--------------------------------------------------------------------------- */
QTextEdit, QPlainTextEdit {
    background-color: rgba(30.000, 29.000, 30.000, 1.000);
}
QTextEdit:focus,
QTextEdit:selected,
QPlainTextEdit:focus,
QPlainTextEdit:selected {
    border: 1px solid rgba(138.000, 180.000, 247.000, 1.000);
    selection-background-color: rgba(18.000, 80.000, 123.000, 1.000);
}

/* In version +5.15, [!active] state is disabled. */
/* In version -5.15, [!focus] state is disabled. */
QTextEdit:!focus,
QPlainTextEdit:!focus {
    $env_patch{"version": ">=5.15", "value": "selection-background-color: rgba(57.000, 61.000, 65.000, 1.000)"};
}
QTextEdit:!active,
QPlainTextEdit:!active {
    $env_patch{"version": "<5.15", "value": "selection-background-color: rgba(57.000, 61.000, 65.000, 1.000)"};
}

/* QAbstractItemView ------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox

--------------------------------------------------------------------------- */
QAbstractItemView {
    alternate-background-color: rgba(41.000, 43.000, 46.000, 1.000);
}
QAbstractItemView:item {
    spacing: 6px;
    border-color: transparent;  /* Fix indicator bug on Qt6 */
}
QAbstractItemView:selected:!active,
QAbstractItemView:selected:!focus,
QAbstractItemView::item:selected:!active,
QTreeView::branch:selected:!active {
    background-color: rgba(57.000, 61.000, 65.000, 1.000);
}
QAbstractItemView::item:selected,
QTreeView::branch:selected {
    background-color: rgba(0.000, 72.000, 117.000, 1.000);
    color: rgba(228.000, 231.000, 235.000, 1.000);
}
QAbstractItemView::item:!selected:hover,
QTreeView::branch:!selected:hover {
    background-color: rgba(41.000, 45.000, 46.000, 1.000);
}
QAbstractItemView::item:selected:disabled {
    color: rgba(105.000, 113.000, 119.000, 1.000);
}

QAbstractItemView QLineEdit {
    padding: 2px;
}

/* QListView QTreeView ---------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview
examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview

--------------------------------------------------------------------------- */
QTreeView::branch {
    border-image: url(${path}/dist/dark/svg/vertical_line_guides-stroke-inactive_0.svg) 0;
}
QTreeView::branch:active {
    border-image: url(${path}/dist/dark/svg/vertical_line_icon-foreground_0.svg) 0;
}
QTreeView::branch:disabled {
    border-image: url(${path}/dist/dark/svg/vertical_line_icon-foreground-disabled_0.svg) 0;
}
QTreeView::branch:has-siblings:adjoins-item,
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: none;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: none;
    image: url(${path}/dist/dark/svg/chevron_right_icon-foreground_0.svg);
}
QTreeView::branch:has-children:!has-siblings:closed:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled {
    image: url(${path}/dist/dark/svg/chevron_right_icon-foreground-disabled_0.svg);
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    border-image: none;
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground_180.svg);
}
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled  {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground-disabled_180.svg);
}

/* QTableView -------------------------------------------------------------

Set the background color to black.
examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview

--------------------------------------------------------------------------- */
QTableView {
    gridline-color: rgba(88.000, 89.000, 92.000, 1.000);
    background-color: rgba(0.000, 0.000, 0.000, 1.000);
}

QTableView QTableCornerButton::section {
    border-right: 2px solid transparent;
    border-bottom: 2px solid transparent;
    border-top-left-radius: 2px;
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
}
QTableView QTableCornerButton::section:pressed {
    background-color: rgba(138.000, 180.000, 247.000, 1.000);
}

QTableView QHeaderView{
    background-color: rgba(0.000, 0.000, 0.000, 1.000);
}

/* QHeaderView ------------------------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview

--------------------------------------------------------------------------- */
QHeaderView {
    padding: 0;
    margin: 0;
    border: none;
    border-radius: 0;
}
QHeaderView::section {
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
    text-align: left;
    font-size: 13px;
    padding: 0 4px;
    border: none;
}
QHeaderView::section:horizontal:on,
QHeaderView::section:vertical:on {
    border-color: rgba(138.000, 180.000, 247.000, 1.000);
}
QHeaderView::section:horizontal:on:disabled,
QHeaderView::section:vertical:on:disabled {
    color: rgba(83.000, 87.000, 91.000, 1.000);
    border-color: rgba(83.000, 87.000, 91.000, 1.000);
}
QHeaderView::section:horizontal {
    border-top: 2px solid transparent;
    margin-right: 1px;
}
QHeaderView::section:vertical {
    border-left: 2px solid transparent;
    margin-bottom: 1px;
}
QHeaderView::section::last,
QHeaderView::section::only-one {
    margin: 0;
}
QHeaderView::down-arrow {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground_180.svg);
}
QHeaderView::down-arrow:disabled {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground-disabled_180.svg);
}
QHeaderView::up-arrow {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground_0.svg);
}
QHeaderView::up-arrow:disabled {
    image: url(${path}/dist/dark/svg/expand_less_icon-foreground-disabled_0.svg);
}
QHeaderView::down-arrow::horizontal,
QHeaderView::up-arrow::horizontal {
    width: 20px;
    padding-right: 2px;
}
QHeaderView::down-arrow::vertical,
QHeaderView::up-arrow::vertical {
    height: 0px;
}

QTreeView[sortingEnabled="false"] QHeaderView::down-arrow,
QTreeView[sortingEnabled="false"] QHeaderView::up-arrow,
QTableView[sortingEnabled="false"] QHeaderView::down-arrow,
QTableView[sortingEnabled="false"] QHeaderView::up-arrow {
    width: 0;
    padding: 0;
}

/* QCalendarWidget --------------------------------------------------------

--------------------------------------------------------------------------- */
QCalendarWidget {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
}

QCalendarWidget QWidget {
    background-color: rgba(0.000, 0.000, 0.000, 1.000);
}
QCalendarWidget QTableView {
    alternate-background-color: rgba(63.000, 64.000, 66.000, 1.000);
}

/* QAbstractSpinBox QLineEdit----------------------------------------------

examples: https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit

--------------------------------------------------------------------------- */
QLineEdit,
QAbstractSpinBox {
    border: 1px solid rgba(63.000, 64.000, 66.000, 1.000);
    padding: 3px 4px;
    /* Adjust the min-height of QLineEdit to the height of the characters. */
    min-height: 1em;
    background-color: rgba(63.000, 64.000, 66.000, 1.000);
    border-radius: 4px;
}
QLineEdit:focus,
QAbstractSpinBox:focus {
    border: 1px solid rgba(138.000, 180.000, 247.000, 1.000);
}
QAbstractSpinBox::up-button,
QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    width: 12px;
    height: 4px;
    padding: 3px;
    border-radius: 0;
}
QAbstractSpinBox::up-button:hover,
QAbstractSpinBox::down-button:hover {
    background-color: rgba(88.000, 89.000, 92.000, 1.000);
}
QAbstractSpinBox::up-button {
    subcontrol-position: top right;
    margin: 3px 3px 1px 1px;
}
QAbstractSpinBox::up-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/dark/svg/arrow_drop_up_icon-foreground_0.svg);
}
QAbstractSpinBox::up-arrow:disabled {
    image: url(${path}/dist/dark/svg/arrow_drop_up_icon-foreground-disabled_0.svg);
}
QAbstractSpinBox::down-button {
    subcontrol-position: bottom right;
    margin: 1px 3px 3px 1px;
}
QAbstractSpinBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/dark/svg/arrow_drop_up_icon-foreground_180.svg);
}
QAbstractSpinBox::down-arrow:disabled {
    image: url(${path}/dist/dark/svg/arrow_drop_up_icon-foreground-disabled_180.svg);
}

/* QDateTimeEdit ----------------------------------------------------------

--------------------------------------------------------------------------- */
QDateTimeEdit::drop-down {
    subcontrol-position: center right;
    border: none;
    padding-right: 4px;
    width: 16px;
    image: url(${path}/dist/dark/svg/calendar_today_icon-foreground_0.svg);
}
QDateTimeEdit::drop-down:disabled {
    image: url(${path}/dist/dark/svg/calendar_today_icon-foreground-disabled_0.svg);
}
/*
There is a bug in Qt, where the down-arrow icon show when `calendarPopup = True`.
So hide down-arrow icon when `calendarPopup = True`.
*/
QDateTimeEdit::down-arrow[calendarPopup="true"] {
    image: none;
}

QDateTimeEdit QAbstractItemView {
    border: 1px solid rgba(138.000, 180.000, 247.000, 1.000);
}

/*
Fix bug where the last line was off the calendar.
*/
QDateTimeEdit QCalendarWidget QAbstractItemView {
    padding: -1px;
    border: none;
}

/* Check ------------------------------------------------------------------

--------------------------------------------------------------------------- */
QComboBox::indicator:checked,
QMenu::indicator:checked {
    width: 20px;
    image: url(${path}/dist/dark/svg/check_icon-foreground_0.svg);
}

/* Check indicator --------------------------------------------------------

document: https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-sub-controls

--------------------------------------------------------------------------- */
QCheckBox {
    spacing: 8px;
}
QGroupBox::title {
    spacing: 6px;
}
QGroupBox::indicator,
QAbstractItemView::indicator {
    height: 18px;
    width: 18px;
}
QCheckBox::indicator:unchecked,
QGroupBox::indicator:unchecked,
QAbstractItemView::indicator:unchecked {
    image: url(${path}/dist/dark/svg/check_box_outline_blank_icon-foreground_0.svg);
}
QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled,
QAbstractItemView::indicator:unchecked:disabled {
    image: url(${path}/dist/dark/svg/check_box_outline_blank_icon-foreground-disabled_0.svg);
}
QCheckBox::indicator:checked,
QGroupBox::indicator:checked,
QAbstractItemView::indicator:checked {
    image: url(${path}/dist/dark/svg/check_box_highlight_0.svg);
}
QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled,
QAbstractItemView::indicator:checked:disabled {
    image: url(${path}/dist/dark/svg/check_box_icon-foreground-disabled_0.svg);
}
QCheckBox::indicator:indeterminate,
QAbstractItemView::indicator:indeterminate {
    image: url(${path}/dist/dark/svg/indeterminate_check_box_highlight_0.svg);
}
QCheckBox::indicator:indeterminate:disabled,
QAbstractItemView::indicator:indeterminate:disabled {
    image: url(${path}/dist/dark/svg/indeterminate_check_box_icon-foreground-disabled_0.svg);
}

/* Rounded popup ----------------------------------------------------------

--------------------------------------------------------------------------- */
/* In Qt6, the style crashes by rounded popup. */
QMenu {
    $env_patch{"version": "<6.0", "value": "border-radius: 8px"};
}
QComboBox QAbstractItemView {
    $env_patch{"version": ">=6.0", "value": "border-radius: 0; margin: 0"};
}

/* PyQtGraph
=========================================================================== */

/* PlotWidget -------------------------------------------------------------

--------------------------------------------------------------------------- */
PlotWidget {
    /* Fix cut labels in plots
    https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/134 */
    padding: 0px;
}

"""
