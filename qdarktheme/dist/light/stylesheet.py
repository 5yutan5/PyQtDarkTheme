STYLE_SHEET = """
/* ==========================================================================================
 * PyQtDarkTheme.
 *
 *  This is originally a fork of QDarkStyleSheet distributed under the terms of the MIT License.
 *   see https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/LICENSE.rst#the-mit-license-mit---code
 *
 * Original code:
 *   https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/qdarkstyle/dark/style.qss
 *
 * -------------------------------------------------------------------------------------------
 * The MIT License (MIT)
 *
 * Copyright (c) 2013-2014 Colin Duquesnoy
 * Copyright (c) 2021- Yunosuke Ohsugi
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
QWidget {
    background-color: rgba(248.000, 249.000, 250.000, 1.000);
    color: rgba(77.000, 81.000, 87.000, 1.000);
    selection-background-color: rgba(0.000, 129.000, 219.000, 1.000);
    selection-color: rgba(248.000, 249.000, 250.000, 1.000);
}
QWidget:disabled {
    color: rgba(186.000, 189.000, 194.000, 1.000);
    selection-background-color: rgba(218.000, 220.000, 224.000, 1.000);
    selection-color: rgba(186.000, 189.000, 194.000, 1.000);
}
QWidget {
    backward-icon: url(${path}/dist/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    forward-icon: url(${path}/dist/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    leftarrow-icon: url(${path}/dist/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    rightarrow-icon: url(${path}/dist/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    dialog-ok-icon: url(${path}/dist/light/svg/check__icon-foreground__rotate-0.svg);
    dialog-cancel-icon: url(${path}/dist/light/svg/close__icon-foreground__rotate-0.svg);
    dialog-yes-icon: url(${path}/dist/light/svg/check_circle__icon-foreground__rotate-0.svg);
    dialog-no-icon: url(${path}/dist/light/svg/cancel__icon-foreground__rotate-0.svg);
    dialog-apply-icon: url(${path}/dist/light/svg/check__icon-foreground__rotate-0.svg);
    dialog-reset-icon: url(${path}/dist/light/svg/restart_alt__icon-foreground__rotate-0.svg);
    dialog-save-icon: url(${path}/dist/light/svg/save__icon-foreground__rotate-0.svg);
    dialog-discard-icon: url(${path}/dist/light/svg/delete__icon-foreground__rotate-0.svg);
    dialog-close-icon: url(${path}/dist/light/svg/close__icon-foreground__rotate-0.svg);
    dialog-open-icon: url(${path}/dist/light/svg/folder_open__icon-foreground__rotate-0.svg);
    dialog-help-icon: url(${path}/dist/light/svg/help__icon-foreground__rotate-0.svg);
    filedialog-parent-directory-icon: url(${path}/dist/light/svg/arrow_upward__icon-foreground__rotate-0.svg);
    filedialog-new-directory-icon: url(${path}/dist/light/svg/create_new_folder__icon-foreground__rotate-0.svg);
    titlebar-close-icon: url(${path}/dist/light/svg/close__icon-foreground__rotate-0.svg);
    titlebar-normal-icon: url(${path}/dist/light/svg/flip_to_front__icon-foreground__rotate-0.svg);
}
QCommandLinkButton {
    qproperty-icon: url(${path}/dist/light/svg/east__highlight__rotate-0.svg);
}
QMainWindow::separator {
    width: 4px;
    height: 4px;
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QMainWindow::separator:hover,
QMainWindow::separator:pressed {
    background-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QToolTip {
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
    color: rgba(77.000, 81.000, 87.000, 1.000);
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
}
QSizeGrip {
  width: 0;
  height: 0;
  image: none;
}
QStatusBar {
    background-color: rgba(223.000, 225.000, 229.000, 1.000);
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
    background-color: rgba(209.000, 212.000, 218.000, 1.000);
}
QStatusBar QWidget:pressed {
    background-color: rgba(195.000, 199.000, 206.000, 1.000);
}
QStatusBar QWidget:disabled {
    background-color: rgba(237.000, 238.000, 240.000, 1.000);
}
QStatusBar QWidget:checked {
    background-color: rgba(195.000, 199.000, 206.000, 1.000);
}
QCheckBox,
QRadioButton {
    border-width: 2px 0;
    border-style: solid;
    border-color: transparent;
}
QCheckBox:hover,
QRadioButton:hover {
    border-bottom: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QCheckBox::indicator,
QRadioButton::indicator {
    margin: 0 0 2 10;
    height: 18px;
    width: 18px;
}
QRadioButton {
    spacing: 8px;
}
QRadioButton::indicator:unchecked {
    image: url(${path}/dist/light/svg/radio_button_unchecked__icon-foreground__rotate-0.svg);
}
QRadioButton::indicator:unchecked:disabled {
    image: url(${path}/dist/light/svg/radio_button_unchecked__icon-foreground-disabled__rotate-0.svg);
}
QRadioButton::indicator:checked {
    image: url(${path}/dist/light/svg/radio_button_checked__highlight__rotate-0.svg);
}
QRadioButton::indicator:checked:disabled {
    image: url(${path}/dist/light/svg/radio_button_checked__icon-foreground-disabled__rotate-0.svg);
}
QGroupBox {
    font-weight: bold;
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
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
QMenuBar {
    background-color: rgba(248.000, 249.000, 250.000, 1.000);
    padding: 2px;
    border-bottom: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
}
QMenuBar::item {
    background: transparent;
    padding: 4px;
}
QMenuBar::item:selected {
    padding: 4px;
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 4px;
}
QMenuBar::item:pressed {
    padding: 4px;
    margin-bottom: 0px;
    padding-bottom: 0px;
}
QToolBar {
    background-color: rgba(235.000, 235.000, 235.000, 1.000);
    padding: 1px;
    font-weight: bold;
    spacing: 2px;
    margin: 1px;
}
QToolBar::handle:horizontal {
    width: 20px;
    image: url(${path}/dist/light/svg/drag_indicator_horizontal__icon-foreground__rotate-0.svg);
}
QToolBar::handle:vertical {
    height: 20px;
    image: url(${path}/dist/light/svg/drag_indicator_horizontal__icon-foreground__rotate-90.svg);
}
QToolBar::separator {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
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
    background-color: rgba(215.000, 215.000, 215.000, 1.000);
}
QToolBar > QToolButton:pressed {
    background-color: rgba(196.000, 196.000, 196.000, 1.000);
}
QToolBar > QToolButton:checked {
    background-color: rgba(196.000, 196.000, 196.000, 1.000);
}
QToolBar > QToolButton#qt_toolbar_ext_button {
    image: url(${path}/dist/light/svg/double_arrow__icon-foreground__rotate-0.svg);
}
QToolBar > QToolButton#qt_toolbar_ext_button:disabled {
    image: url(${path}/dist/light/svg/double_arrow__icon-foreground-disabled__rotate-0.svg);
}
QMenu {
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
    padding: 8px 0;
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
}
QMenu::separator {
    height: 1px;
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QMenu::item {
    padding: 4px 28px;
}
QMenu::item:selected {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
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
    image: url(${path}/dist/light/svg/chevron_right__icon-foreground__rotate-0.svg);
}
QMenu::right-arrow:disabled {
    image: url(${path}/dist/light/svg/chevron_right__icon-foreground-disabled__rotate-0.svg);
}
QScrollBar:horizontal {
    height: 7px;
    margin: 0 6px;
}
QScrollBar:vertical {
    width: 7px;
    margin: 6px 0;
}
QScrollBar::handle {
    background-color: rgba(155.000, 155.000, 157.000, 1.000);
    border-radius: 3px;
}
QScrollBar::handle:hover {
    background-color: rgba(117.000, 117.000, 119.000, 1.000);
}
QScrollBar::handle:horizontal {
    min-width: 8px;
}
QScrollBar::handle:vertical {
    min-height: 8px;
}
QScrollBar::sub-line, QScrollBar::add-line {
    width: 0;
    height: 0;
}
QScrollBar::sub-page, QScrollBar::add-page {
    background-color: transparent;
}
QProgressBar {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 4px;
    text-align: center;
    color: rgba(77.000, 81.000, 87.000, 1.000);
}
QProgressBar::chunk {
    background-color: rgba(0.000, 129.000, 219.000, 1.000);
    border-radius: 3px;
}
QProgressBar::chunk:disabled {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QPushButton {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    padding: 4px 8px;
    border-radius: 4px;
    color: rgba(0.000, 129.000, 219.000, 1.000);
}
QPushButton:hover {
    background-color: rgba(226.000, 234.000, 251.000, 1.000);
}
QPushButton:pressed {
    background-color: rgba(181.000, 202.000, 244.000, 1.000);
}
QPushButton:checked {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QPushButton:disabled {
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QPushButton[flat=true]:!checked {
    border-color: transparent;
}
QDialogButtonBox QPushButton {
    min-width: 65px;
}
QToolButton {
    padding: 5px;
    border-radius: 2px;
    spacing: 2px;
}
QToolButton:hover {
    background-color: rgba(226.000, 234.000, 251.000, 1.000);
}
QToolButton:pressed {
    background-color: rgba(181.000, 202.000, 244.000, 1.000);
}
QToolButton:selected,
QToolButton:checked {
    background-color: rgba(181.000, 202.000, 244.000, 1.000);
}
QToolButton::checked:disabled {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
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
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QToolButton::menu-indicator {
    height: 18px;
    width: 18px;
    top: 6px;
    left: 3px;
    image: url(${path}/dist/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QToolButton::menu-indicator:disabled {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QToolButton::menu-arrow {
    height: 8px;
    width: 8px;
}
QToolButton[popupMode="1"] {
    padding-right: 14px;
}
QComboBox {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 4px;
    min-height: 1.5em;
    padding: 0 4px;
    background-color: rgba(248.000, 249.000, 250.000, 1.000);
}
QComboBox:focus,
QComboBox:open {
    border: 1px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QComboBox::drop-down {
    subcontrol-position: center right;
    border: none;
    padding-right: 4px;
}
QComboBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QComboBox::down-arrow:disabled {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QComboBox::item:selected {
    border: none;
    background-color: rgba(76.000, 166.000, 229.000, 1.000);
    color: rgba(77.000, 81.000, 87.000, 1.000);
}
QComboBox QAbstractItemView {
    margin: 0;
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    selection-background-color: rgba(76.000, 166.000, 229.000, 1.000);
    selection-color: rgba(77.000, 81.000, 87.000, 1.000);
    padding: 2px;
}
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
    background-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QSlider::sub-page:disabled,
QSlider::add-page:disabled,
QSlider::handle:disabled {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QSlider::add-page {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
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
QTabWidget::pane {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 3px;
}
QTabBar {
    qproperty-drawBase: 0;
}
QTabBar::close-button:selected {
    image: url(${path}/dist/light/svg/close__icon-foreground__rotate-0.svg);
}
QTabBar::close-button:!selected {
    image: url(${path}/dist/light/svg/close__tabbar-button-inselected__rotate-0.svg)
}
QTabBar::close-button:disabled {
    image: url(${path}/dist/light/svg/close__icon-foreground-disabled__rotate-0.svg);
}
QTabBar::close-button:hover {
    background-color: rgba(147.000, 178.000, 239.000, 1.000);
    border-radius: 4px
}
QTabBar::close-button:hover:!selected {
    background-color: rgba(174.000, 197.000, 244.000, 1.000);
}
QTabBar::tab {
    padding: 3px;
}
QTabBar::tab:hover {
    background-color: rgba(226.000, 234.000, 251.000, 1.000);
}
QTabBar::tab:selected {
    color: rgba(0.000, 129.000, 219.000, 1.000);
    background-color: rgba(181.000, 202.000, 244.000, 1.000);
}
QTabBar::tab:selected:disabled {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
    color: rgba(186.000, 189.000, 194.000, 1.000);
}
QTabBar::tab:top {
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
    border-bottom: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
    margin-left: 4px;
}
QTabBar::tab:top:selected {
    border-bottom: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:top:hover {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:top:selected:disabled {
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QTabBar::tab:bottom {
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    border-top: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
    margin-left: 4px;
}
QTabBar::tab:bottom:selected {
    border-top: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:bottom:hover {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:bottom:selected:disabled {
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QTabBar::tab:left {
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    border-right: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
    margin-top: 4px;
}
QTabBar::tab:left:selected {
    border-right: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:left:hover {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:left:selected:disabled {
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QTabBar::tab:right {
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    border-left: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
    margin-top: 4px;
}
QTabBar::tab:right:selected {
    border-left: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:right:hover {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTabBar::tab:right:selected:disabled {
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QDockWidget {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 4px;
}
QDockWidget::title {
    padding: 3px;
    spacing: 4px;
    border: none;
    background-color: rgba(237.000, 238.000, 240.000, 1.000);
}
QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background-color: rgba(226.000, 234.000, 251.000, 1.000);
    border-radius: 2px
}
QFrame {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    padding: 1px;
    border-radius: 4px;
}
QLCDNumber {
    color: rgba(77.000, 81.000, 87.000, 1.000);
    min-width: 2em;
    margin: 2px;
}
QLabel {
    border: none;
}
QStackedWidget {
    border: none;
}
QToolBox {
    border: none;
}
QToolBox:selected {
    border: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QToolBox::tab {
    background-color: rgba(237.000, 238.000, 240.000, 1.000);
    border-bottom: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
}
QToolBox::tab:selected {
    border-bottom: 2px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QToolBox::tab:selected:disabled {
    border-bottom: 2px solid rgba(218.000, 220.000, 224.000, 1.000);
}
QSplitter {
    border: none;
}
QSplitter::handle {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
    margin: 1px 3px;
}
QSplitter::handle:hover {
    background-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QSplitter::handle:horizontal {
    width: 5px;
    image: url(${path}/dist/light/svg/horizontal_rule__icon-foreground__rotate-90.svg);
}
QSplitter::handle:horizontal:disabled {
    image: url(${path}/dist/light/svg/horizontal_rule__icon-foreground-disabled__rotate-90.svg);
}
QSplitter::handle:vertical {
    height: 5px;
    image: url(${path}/dist/light/svg/horizontal_rule__icon-foreground__rotate-0.svg);
}
QSplitter::handle:vertical:disabled {
    image: url(${path}/dist/light/svg/horizontal_rule__icon-foreground-disabled__rotate-0.svg);
}
QSplitterHandle::item:hover {}
QAbstractScrollArea {
    selection-background-color: rgba(76.000, 166.000, 229.000, 1.000);
    selection-color: rgba(77.000, 81.000, 87.000, 1.000);
    margin: 1px;
}
QAbstractScrollArea:disabled {
    selection-background-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTextEdit, QPlainTextEdit {
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
}
QTextEdit:focus,
QTextEdit:selected,
QPlainTextEdit:focus,
QPlainTextEdit:selected {
    border: 1px solid rgba(0.000, 129.000, 219.000, 1.000);
    selection-background-color: rgba(162.000, 216.000, 255.000, 1.000);
}
QTextEdit:!focus,
QPlainTextEdit:!focus {
    $env_patch{"version": ">=5.15.0", "value": "selection-background-color: rgba(228.000, 230.000, 242.000, 1.000)"};
}
QTextEdit:!active,
QPlainTextEdit:!active {
    $env_patch{"version": "<5.15.0", "value": "selection-background-color: rgba(228.000, 230.000, 242.000, 1.000)"};
}
QAbstractItemView {
    alternate-background-color: rgba(233.000, 236.000, 239.000, 1.000);
}
QAbstractItemView:item {
    spacing: 6px;
    border-color: transparent;
}
QAbstractItemView:selected:!active,
QAbstractItemView:selected:!focus,
QAbstractItemView::item:selected:!active,
QTreeView::branch:selected:!active {
    background-color: rgba(228.000, 230.000, 242.000, 1.000);
}
QAbstractItemView::item:selected,
QTreeView::branch:selected {
    background-color: rgba(76.000, 166.000, 229.000, 1.000);
    color: rgba(77.000, 81.000, 87.000, 1.000);
}
QAbstractItemView::item:!selected:hover,
QTreeView::branch:!selected:hover {
    background-color: rgba(211.000, 211.000, 211.000, 1.000);
}
QAbstractItemView::item:selected:disabled {
    color: rgba(186.000, 189.000, 194.000, 1.000);
}
QAbstractItemView QLineEdit,
QAbstractItemView QAbstractSpinBox,
QAbstractItemView QComboBox,
QAbstractItemView QAbstractButton {
    padding: 0px;
    margin: 1px;
}
QTreeView::branch {
    border-image: url(${path}/dist/light/svg/vertical_line__guides-stroke-inactive__rotate-0.svg) 0;
}
QTreeView::branch:active {
    border-image: url(${path}/dist/light/svg/vertical_line__icon-foreground__rotate-0.svg) 0;
}
QTreeView::branch:disabled {
    border-image: url(${path}/dist/light/svg/vertical_line__icon-foreground-disabled__rotate-0.svg) 0;
}
QTreeView::branch:has-siblings:adjoins-item,
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: none;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: none;
    image: url(${path}/dist/light/svg/chevron_right__icon-foreground__rotate-0.svg);
}
QTreeView::branch:has-children:!has-siblings:closed:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled {
    image: url(${path}/dist/light/svg/chevron_right__icon-foreground-disabled__rotate-0.svg);
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    border-image: none;
    image: url(${path}/dist/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled  {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QTableView {
    gridline-color: rgba(88.000, 89.000, 92.000, 1.000);
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
}
QTableView QTableCornerButton::section {
    border-right: 2px solid transparent;
    border-bottom: 2px solid transparent;
    border-top-left-radius: 2px;
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QTableView QTableCornerButton::section:pressed {
    background-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QTableView QHeaderView{
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
}
QHeaderView {
    padding: 0;
    margin: 0;
    border: none;
    border-radius: 0;
}
QHeaderView::section {
    background-color: rgba(218.000, 220.000, 224.000, 1.000);
    text-align: left;
    font-size: 13px;
    padding: 0 4px;
    border: none;
}
QHeaderView::section:horizontal:on,
QHeaderView::section:vertical:on {
    border-color: rgba(0.000, 129.000, 219.000, 1.000);
}
QHeaderView::section:horizontal:on:disabled,
QHeaderView::section:vertical:on:disabled {
    color: rgba(218.000, 220.000, 224.000, 1.000);
    border-color: rgba(218.000, 220.000, 224.000, 1.000);
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
    image: url(${path}/dist/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QHeaderView::down-arrow:disabled {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QHeaderView::up-arrow {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground__rotate-0.svg);
}
QHeaderView::up-arrow:disabled {
    image: url(${path}/dist/light/svg/expand_less__icon-foreground-disabled__rotate-0.svg);
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
QCalendarWidget {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    border-radius: 4px;
}
QCalendarWidget QWidget {
    background-color: rgba(255.000, 255.000, 255.000, 1.000);
}
QCalendarWidget QTableView {
    alternate-background-color: rgba(218.000, 220.000, 224.000, 1.000);
}
QLineEdit,
QAbstractSpinBox {
    border: 1px solid rgba(218.000, 220.000, 224.000, 1.000);
    padding: 3px 4px;
    min-height: 1em;
    background-color: rgba(248.000, 249.000, 250.000, 1.000);
    border-radius: 4px;
}
QLineEdit:focus,
QAbstractSpinBox:focus {
    border: 1px solid rgba(0.000, 129.000, 219.000, 1.000);
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
    background-color: rgba(226.000, 234.000, 251.000, 1.000);
}
QAbstractSpinBox::up-button {
    subcontrol-position: top right;
    margin: 3px 3px 1px 1px;
}
QAbstractSpinBox::up-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/light/svg/arrow_drop_up__icon-foreground__rotate-0.svg);
}
QAbstractSpinBox::up-arrow:disabled {
    image: url(${path}/dist/light/svg/arrow_drop_up__icon-foreground-disabled__rotate-0.svg);
}
QAbstractSpinBox::down-button {
    subcontrol-position: bottom right;
    margin: 1px 3px 3px 1px;
}
QAbstractSpinBox::down-arrow {
    height: 23px;
    width: 23px;
    image: url(${path}/dist/light/svg/arrow_drop_up__icon-foreground__rotate-180.svg);
}
QAbstractSpinBox::down-arrow:disabled {
    image: url(${path}/dist/light/svg/arrow_drop_up__icon-foreground-disabled__rotate-180.svg);
}
QDateTimeEdit::drop-down {
    subcontrol-position: center right;
    border: none;
    padding-right: 4px;
    width: 16px;
    image: url(${path}/dist/light/svg/calendar_today__icon-foreground__rotate-0.svg);
}
QDateTimeEdit::drop-down:disabled {
    image: url(${path}/dist/light/svg/calendar_today__icon-foreground-disabled__rotate-0.svg);
}
QDateTimeEdit::down-arrow[calendarPopup="true"] {
    image: none;
}
QDateTimeEdit QAbstractItemView {
    border: 1px solid rgba(0.000, 129.000, 219.000, 1.000);
}
QDateTimeEdit QCalendarWidget QAbstractItemView {
    padding: -1px;
    border: none;
}
QFileDialog > QFrame QAbstractItemView {
    border: none;
}
QFileDialog > QFrame > QFrame QFrame QFrame {
    border: none;
    padding: 0;
}
QFontDialog QListView {
    min-height: 60px;
}
QFontDialog QScrollBar:vertical {
    margin: 0;
}
QComboBox::indicator:checked,
QMenu::indicator:checked {
    width: 18px;
    image: url(${path}/dist/light/svg/check__icon-foreground__rotate-0.svg);
}
QMenu::indicator {
    width: 18px;
    background-color: rgba(196.000, 199.000, 204.000, 1.000);
    border-radius: 4px;
    margin-left: 3px;
}
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
    image: url(${path}/dist/light/svg/check_box_outline_blank__icon-foreground__rotate-0.svg);
}
QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled,
QAbstractItemView::indicator:unchecked:disabled {
    image: url(${path}/dist/light/svg/check_box_outline_blank__icon-foreground-disabled__rotate-0.svg);
}
QCheckBox::indicator:checked,
QGroupBox::indicator:checked,
QAbstractItemView::indicator:checked {
    image: url(${path}/dist/light/svg/check_box__highlight__rotate-0.svg);
}
QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled,
QAbstractItemView::indicator:checked:disabled {
    image: url(${path}/dist/light/svg/check_box__icon-foreground-disabled__rotate-0.svg);
}
QCheckBox::indicator:indeterminate,
QAbstractItemView::indicator:indeterminate {
    image: url(${path}/dist/light/svg/indeterminate_check_box__highlight__rotate-0.svg);
}
QCheckBox::indicator:indeterminate:disabled,
QAbstractItemView::indicator:indeterminate:disabled {
    image: url(${path}/dist/light/svg/indeterminate_check_box__icon-foreground-disabled__rotate-0.svg);
}
QMenu {
    $env_patch{"version": "<6.0.0", "value": "border-radius: 8px"};
}
QComboBox QAbstractItemView {
    $env_patch{"version": ">=6.0.0", "value": "border-radius: 0; margin: 0"};
}
PlotWidget {
    padding: 0px;
}

"""
