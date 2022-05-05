"""Contents that define stylesheet for light theme."""

STYLE_SHEET = """
* {
    padding: 0;
    margin: 0;
    border: none;
    border-style: none;
    border-image: unset;
    outline: none;
}
QToolBar * {
    margin: 0;
    padding: 0;
}
QWidget {
    background: #f8f9fa;
    color: #4d5157;
    selection-background-color: #0081db;
    selection-color: #f8f9fa;
}
QWidget:disabled {
    color: #babdc2;
    selection-background-color: #dadce0;
    selection-color: #babdc2;
}
QWidget {
    backward-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    forward-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    leftarrow-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
    rightarrow-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
    dialog-ok-icon: url(${path}/light/svg/check__icon-foreground.svg);
    dialog-cancel-icon: url(${path}/light/svg/close__icon-foreground.svg);
    dialog-yes-icon: url(${path}/light/svg/check_circle__icon-foreground.svg);
    dialog-no-icon: url(${path}/light/svg/cancel__icon-foreground.svg);
    dialog-apply-icon: url(${path}/light/svg/check__icon-foreground.svg);
    dialog-reset-icon: url(${path}/light/svg/restart_alt__icon-foreground.svg);
    dialog-save-icon: url(${path}/light/svg/save__icon-foreground.svg);
    dialog-discard-icon: url(${path}/light/svg/delete__icon-foreground.svg);
    dialog-close-icon: url(${path}/light/svg/close__icon-foreground.svg);
    dialog-open-icon: url(${path}/light/svg/folder_open__icon-foreground.svg);
    dialog-help-icon: url(${path}/light/svg/help__icon-foreground.svg);
    filedialog-parent-directory-icon: url(${path}/light/svg/arrow_upward__icon-foreground.svg);
    filedialog-new-directory-icon: url(${path}/light/svg/create_new_folder__icon-foreground.svg);
    titlebar-close-icon: url(${path}/light/svg/close__icon-foreground.svg);
    titlebar-normal-icon: url(${path}/light/svg/flip_to_front__icon-foreground.svg);
}
QCommandLinkButton {
    qproperty-icon: url(${path}/light/svg/east__highlight.svg);
}
QMainWindow::separator {
    width: 4px;
    height: 4px;
    background: #dadce0;
}
QMainWindow::separator:hover,
QMainWindow::separator:pressed {
    background: #0081db;
}
QToolTip {
    background: #ffffff;
    color: #4d5157;
    border: 1px solid #dadce0;
}
QSizeGrip {
    width: 0;
    height: 0;
    image: none;
}
QStatusBar {
    background: #dfe1e5;
}
QStatusBar::item {
    border: none;
}
QStatusBar QWidget {
    background: transparent;
    padding: 3px;
    border-radius: $radius{4px};
}
QStatusBar > .QSizeGrip {
    padding: 0;
}
QStatusBar QWidget:hover {
    background: #d1d4da;
}
QStatusBar QWidget:pressed,
QStatusBar QWidget:checked {
    background: #c3c7ce;
}
QStatusBar QWidget:disabled {
    background: #edeef0;
}
QCheckBox,
QRadioButton {
    border-top: 2px solid transparent;
    border-bottom: 2px solid transparent;
}
QCheckBox:!window,
QRadioButton:!window {
    background: transparent;
}
QCheckBox:hover,
QRadioButton:hover {
    border-bottom: 2px solid #0081db;
}
QGroupBox {
    font-weight: bold;
    border: 1px solid #dadce0;
    margin-top: 8px;
    padding: 2px 1px 1px 1px;
    border-radius: $radius{4px};
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 7px;
    margin: 0 2px 0 3px;
}
QGroupBox:flat {
    border-color: transparent;
}
QMenuBar {
    background: #f8f9fa;
    padding: 2px;
    border-bottom: 1px solid #dadce0;
}
QMenuBar::item {
    background: transparent;
    padding: 4px;
}
QMenuBar::item:selected {
    padding: 4px;
    background: #dadce0;
    border-radius: $radius{4px};
}
QMenuBar::item:pressed {
    padding: 4px;
    margin-bottom: 0;
    padding-bottom: 0;
}
QToolBar {
    background: #ebebeb;
    padding: 1px;
    font-weight: bold;
    spacing: 2px;
    margin: 1px;
}
QToolBar::handle:horizontal {
    width: 20px;
    image: url(${path}/light/svg/drag_indicator_horizontal__icon-foreground.svg);
}
QToolBar::handle:vertical {
    height: 20px;
    image: url(${path}/light/svg/drag_indicator_horizontal__icon-foreground__rotate-90.svg);
}
QToolBar::separator {
    background: #dadce0;
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
    background: transparent;
    padding: 3px;
    border-radius: $radius{4px};
}
QToolBar > QToolButton:hover,
QToolBar > QToolButton::menu-button:hover {
    background: #d7d7d7;
}
QToolBar > QToolButton:pressed,
QToolBar > QToolButton::menu-button:pressed,
QToolBar > QToolButton:checked {
    background: #c4c4c4;
}
QToolBar > QToolButton#qt_toolbar_ext_button {
    image: url(${path}/light/svg/double_arrow__icon-foreground.svg);
    $env_patch{"os": "Windows", "value": "padding: 0; qproperty-icon: unset"};
}
QToolBar > QToolButton#qt_toolbar_ext_button:disabled {
    image: url(${path}/light/svg/double_arrow__icon-foreground-disabled.svg);
}
QToolBar > QWidget {
    background: transparent;
}
QMenu {
    background: #ffffff;
    padding: 8px 0;
    border: 1px solid #dadce0;
}
QMenu::separator {
    margin: 4px 0;
    height: 1px;
    background: #dadce0;
}
QMenu::item {
    padding: 4px 28px;
}
QMenu::item:selected {
    background: #dadce0;
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
    image: url(${path}/light/svg/chevron_right__icon-foreground.svg);
}
QMenu::right-arrow:disabled {
    image: url(${path}/light/svg/chevron_right__icon-foreground-disabled.svg);
}
QScrollBar {
    background: #edeff2;
    $env_patch{"os": "Darwin", "value": "background: transparent"};
    border-radius: $radius{4px};
}
QScrollBar:horizontal {
    height: 14px;
    $env_patch{"os": "Darwin", "value": "height: 7px;"};
}
QScrollBar:vertical {
    width: 14px;
    $env_patch{"os": "Darwin", "value": "width: 7px;"};
}
QScrollBar::handle {
    background: rgba(155.000, 155.000, 157.000, 0.737);
    border-radius: $radius{3px};
}
QScrollBar::handle:hover {
    background: rgba(117.000, 117.000, 119.000, 0.827);
}
QScrollBar::handle:pressed {
    background: rgba(96.000, 96.000, 98.000, 0.933);
}
QScrollBar::handle:disabled {
    background-color: #d6dbe2;
}
QScrollBar::handle:horizontal {
    min-width: 8px;
    margin: 4px 14px;
    $env_patch{"os": "Darwin", "value": "margin: 0;"};
}
QScrollBar::handle:horizontal:hover {
    margin: 2px 14px;
    $env_patch{"os": "Darwin", "value": "margin: 0;"};
}
QScrollBar::handle:vertical {
    min-height: 8px;
    margin: 14px 4px;
    $env_patch{"os": "Darwin", "value": "margin: 0;"};
}
QScrollBar::handle:vertical:hover {
    margin: 14px 2px;
    $env_patch{"os": "Darwin", "value": "margin: 0;"};
}
QScrollBar::sub-page, QScrollBar::add-page {
    background: transparent;
}
QScrollBar::sub-line,
QScrollBar::add-line {
    background: transparent;
    width: 14px;
    height: 14px;
    margin: 2px;
    subcontrol-origin: margin;
    $env_patch{"os": "Darwin", "value": "width: 0; height: 0; margin: 0"};
}
QScrollBar::sub-line:vertical {
    subcontrol-position: top;
}
QScrollBar::add-line:vertical {
    subcontrol-position: bottom;
}
QScrollBar::sub-line:horizontal {
    subcontrol-position: left;
}
QScrollBar::add-line:horizontal {
    subcontrol-position: right;
}
QScrollBar::up-arrow {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle.svg);
}
QScrollBar::right-arrow {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle__rotate-90.svg);
}
QScrollBar::down-arrow {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle__rotate-180.svg);
}
QScrollBar::left-arrow {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle__rotate-270.svg);
}
QScrollBar::up-arrow:hover {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle-pressed.svg);
}
QScrollBar::right-arrow:hover {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle-pressed__rotate-90.svg);
}
QScrollBar::down-arrow:hover {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle-pressed__rotate-180.svg);
}
QScrollBar::left-arrow:hover {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-handle-pressed__rotate-270.svg);
}
QScrollBar::up-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-disabled.svg);
}
QScrollBar::right-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-disabled__rotate-90.svg);
}
QScrollBar::down-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-disabled__rotate-180.svg);
}
QScrollBar::left-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__scrollbar-disabled__rotate-270.svg);
}
QProgressBar {
    border: 1px solid #dadce0;
    text-align: center;
    color: #4d5157;
    border-radius: $radius{4px};
}
QProgressBar::chunk {
    background: #0081db;
    border-radius: $radius{3px};
}
QProgressBar::chunk:disabled {
    background: #dadce0;
}
QPushButton {
    color: #0081db;
    border: 1px solid #dadce0;
    padding: 4px 8px;
    border-radius: $radius{4px};
}
QPushButton:!window {
    background: transparent;
}
QPushButton:flat,
QPushButton:default {
    border: none;
    padding: 5px 9px;
}
QPushButton:default {
    color: #f8f9fa;
    background: #0081db;
}
QPushButton:hover,
QPushButton:flat:hover {
    background: rgba(181.000, 202.000, 244.000, 0.333);
}
QPushButton:pressed,
QPushButton:flat:pressed,
QPushButton:checked:pressed,
QPushButton:flat:checked:pressed {
    background: rgba(181.000, 202.000, 244.000, 0.933);
}
QPushButton:checked,
QPushButton:flat:checked {
    background: rgba(181.000, 202.000, 244.000, 0.733);
}
QPushButton:default:hover {
    background: #3781ea;
}
QPushButton:default:pressed {
    background: #6ca1f0;
}
QPushButton:default:disabled {
    background: #dadce0;
}
QDialogButtonBox QPushButton {
    min-width: 65px;
}
QToolButton {
    background: transparent;
    padding: 5px;
    spacing: 2px;
    border-radius: $radius{2px};
}
QToolButton:hover,
QToolButton::menu-button:hover {
    background: rgba(181.000, 202.000, 244.000, 0.333);
}
QToolButton:pressed,
QToolButton:checked:pressed,
QToolButton::menu-button:pressed {
    background: rgba(181.000, 202.000, 244.000, 0.933);
}
QToolButton:selected,
QToolButton:checked {
    background: rgba(181.000, 202.000, 244.000, 0.733);
}
QToolButton::checked:disabled {
    background: #dadce0;
}
QToolButton::menu-indicator {
    height: 18px;
    width: 18px;
    top: 6px;
    left: 3px;
    image: url(${path}/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QToolButton::menu-indicator:disabled {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QToolButton::menu-arrow {
    image: unset;
}
QToolButton::menu-button {
    subcontrol-origin: margin;
    border: none;
    width: 17px;
    border-top-right-radius: $radius{4px};
    border-bottom-right-radius: $radius{4px};
    image: url(${path}/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QToolButton::menu-button:disabled {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QToolButton[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "popupMode=MenuButtonPopup"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "popupMode=\\\"1\\\""}
$env_patch{"version": ">=6.0.0", "value": "popupMode=MenuButtonPopup"}
] {
    padding-right: 1px;
    margin-right: 18px;
    border-top-right-radius: $radius{0};
    border-bottom-right-radius: $radius{0};
}
QComboBox {
    border: 1px solid #dadce0;
    min-height: 1.5em;
    padding: 0 4px;
    background: rgba(255.000, 255.000, 255.000, 0.000);
    border-radius: $radius{4px};
}
QComboBox:focus,
QComboBox:open {
    border: 1px solid #0081db;
}
QComboBox::drop-down {
    border: none;
    padding-right: 4px;
}
QComboBox::down-arrow {
    image: url(${path}/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QComboBox::down-arrow:disabled {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QComboBox::item:selected {
    border: none;
    background: #4ca6e5;
    color: #4d5157;
}
QComboBox QAbstractItemView {
    background: #ffffff;
    margin: 0;
    border: 1px solid #dadce0;
    selection-background-color: #4ca6e5;
    selection-color: #4d5157;
    padding: 2px;
}
QComboBox QAbstractItemView[
$env_patch{"version": "<6.0.0", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border-color: #dadce0;
}
QSlider {
    padding: 2px 0;
}
QSlider::groove {
    border-radius: $radius{2px};
}
QSlider::groove:horizontal {
    height: 4px;
}
QSlider::groove:vertical {
    width: 4px;
}
QSlider::sub-page, QSlider::handle {
    background: #0081db;
}
QSlider::sub-page:disabled,
QSlider::add-page:disabled,
QSlider::handle:disabled {
    background: #dadce0;
}
QSlider::add-page {
    background: #abc6f6;
}
QSlider::handle:hover {
    background: #3781ea;
}
QSlider::handle:pressed {
    background: #6ca1f0;
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
    border: 1px solid #dadce0;
    border-radius: $radius{4px};
}
QTabBar {
    qproperty-drawBase: 0;
}
QTabBar::close-button:selected {
    image: url(${path}/light/svg/close__icon-foreground.svg);
}
QTabBar::close-button:!selected {
    image: url(${path}/light/svg/close__tabbar-button-unselected.svg)
}
QTabBar::close-button:disabled {
    image: url(${path}/light/svg/close__icon-foreground-disabled.svg);
}
QTabBar::close-button:hover {
    background: #93b2ef;
    border-radius: $radius{4px};
}
QTabBar::close-button:hover:!selected {
    background: #aec5f4;
}
QTabBar::tab {
    padding: 3px;
}
QTabBar::tab:hover {
    background: rgba(181.000, 202.000, 244.000, 0.333);
}
QTabBar::tab:selected {
    color: #0081db;
    background: rgba(181.000, 202.000, 244.000, 0.933);
}
QTabBar::tab:selected:disabled {
    background: #dadce0;
    color: #babdc2;
}
QTabBar::tab:top {
    border-bottom: 2px solid #dadce0;
    margin-left: 4px;
    border-top-left-radius: $radius{2px};
    border-top-right-radius: $radius{2px};
}
QTabBar::tab:top:selected {
    border-bottom: 2px solid #0081db;
}
QTabBar::tab:top:hover {
    border-color: #0081db;
}
QTabBar::tab:top:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:bottom {
    border-top: 2px solid #dadce0;
    margin-left: 4px;
    border-bottom-left-radius: $radius{2px};
    border-bottom-right-radius: $radius{2px};
}
QTabBar::tab:bottom:selected {
    border-top: 2px solid #0081db;
}
QTabBar::tab:bottom:hover {
    border-color: #0081db;
}
QTabBar::tab:bottom:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:left {
    border-right: 2px solid #dadce0;
    margin-top: 4px;
    border-top-left-radius: $radius{2px};
    border-bottom-left-radius: $radius{2px};
}
QTabBar::tab:left:selected {
    border-right: 2px solid #0081db;
}
QTabBar::tab:left:hover {
    border-color: #0081db;
}
QTabBar::tab:left:selected:disabled {
    border-color: #dadce0;
}
QTabBar::tab:right {
    border-left: 2px solid #dadce0;
    margin-top: 4px;
    border-top-right-radius: $radius{2px};
    border-bottom-right-radius: $radius{2px};
}
QTabBar::tab:right:selected {
    border-left: 2px solid #0081db;
}
QTabBar::tab:right:hover {
    border-color: #0081db;
}
QTabBar::tab:right:selected:disabled {
    border-color: #dadce0;
}
QDockWidget {
    border: 1px solid #dadce0;
    border-radius: $radius{4px};
}
QDockWidget::title {
    padding: 3px;
    spacing: 4px;
    background: #edeef0;
}
QDockWidget::close-button,
QDockWidget::float-button {
    border-radius: $radius{2px};
}
QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background: rgba(181.000, 202.000, 244.000, 0.333);
}
QDockWidget::close-button:pressed,
QDockWidget::float-button:pressed {
    background: rgba(181.000, 202.000, 244.000, 0.933);
}
QFrame {
    border: 1px solid #dadce0;
    padding: 1px;
    border-radius: $radius{4px};
}
.QFrame {
    padding: 0;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=NoFrame"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border-color: transparent;
    padding: 0;
}
.QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=NoFrame"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"0\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=NoFrame"}
] {
    border: none;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=Panel"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"2\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=Panel"}
] {
    border-color: #ffffff;
    background: #ffffff;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=HLine"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"4\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=HLine"}
] {
    max-height: 2px;
    border: none;
    background: #dadce0;
}
QFrame[
$env_patch{"version": "<6.0.0", "qt": "PySide2", "value": "frameShape=VLine"}
$env_patch{"version": "<6.0.0", "qt": "PyQt5", "value": "frameShape=\\\"5\\\""}
$env_patch{"version": ">=6.0.0", "value": "frameShape=VLine"}
] {
    max-width: 2px;
    border: none;
    background: #dadce0;
}
QLCDNumber {
    color: #4d5157;
    min-width: 2em;
    margin: 2px;
}
QLabel:!window,
QLCDNumber:!window {
    background-color: transparent;
}
QToolBox:selected {
    border: 2px solid #0081db;
}
QToolBox::tab {
    background: #edeef0;
    border-bottom: 2px solid #dadce0;
    border-top-left-radius: $radius{4px};
    border-top-right-radius: $radius{4px};
}
QToolBox::tab:selected {
    border-bottom: 2px solid #0081db;
}
QToolBox::tab:selected:disabled {
    border-bottom: 2px solid #dadce0;
}
QSplitter::handle {
    background: #dadce0;
    margin: 1px 3px;
}
QSplitter::handle:hover {
    background: #0081db;
}
QSplitter::handle:horizontal {
    width: 5px;
    image: url(${path}/light/svg/horizontal_rule__icon-foreground__rotate-90.svg);
}
QSplitter::handle:horizontal:disabled {
    image: url(${path}/light/svg/horizontal_rule__icon-foreground-disabled__rotate-90.svg);
}
QSplitter::handle:vertical {
    height: 5px;
    image: url(${path}/light/svg/horizontal_rule__icon-foreground.svg);
}
QSplitter::handle:vertical:disabled {
    image: url(${path}/light/svg/horizontal_rule__icon-foreground-disabled.svg);
}
QSplitterHandle::item:hover {}
QAbstractScrollArea {
    selection-background-color: #4ca6e5;
    selection-color: #4d5157;
    margin: 1px;
}
QAbstractScrollArea:disabled {
    selection-background-color: #0081db;
}
QAbstractScrollArea::corner {
    background: transparent;
}
QAbstractScrollArea > .QWidget {
    background: transparent;
}
QAbstractScrollArea > .QWidget > .QWidget {
    background: transparent;
}
QTextEdit, QPlainTextEdit {
    background: #ffffff;
}
QTextEdit:focus,
QTextEdit:selected,
QPlainTextEdit:focus,
QPlainTextEdit:selected {
    border: 1px solid #0081db;
    selection-background-color: #a2d8ff;
}
QTextEdit:!focus,
QPlainTextEdit:!focus {
    $env_patch{"version": ">=5.15.0", "value": "selection-background-color: #e4e6f2"};
}
QTextEdit:!active,
QPlainTextEdit:!active {
    $env_patch{"version": "<5.15.0", "value": "selection-background-color: #e4e6f2"};
}
QAbstractItemView {
    alternate-background-color: #e9ecef;
}
QAbstractItemView::item {
    $env_patch{"version": ">=6.0.0", "value": "border-color: transparent"};
}
QAbstractItemView:selected:!active,
QAbstractItemView:selected:!focus,
QAbstractItemView::item:selected:!active,
QTreeView::branch:selected:!active {
    background: #e4e6f2;
}
QAbstractItemView::item:selected,
QTreeView::branch:selected {
    background: #4ca6e5;
    color: #4d5157;
}
QAbstractItemView::item:!selected:hover,
QTreeView::branch:!selected:hover {
    background: #d3d3d3;
}
QAbstractItemView::item:selected:disabled {
    color: #babdc2;
}
QAbstractItemView QLineEdit,
QAbstractItemView QAbstractSpinBox,
QAbstractItemView QComboBox,
QAbstractItemView QAbstractButton {
    padding: 0;
    margin: 1px;
}
QTreeView::branch {
    border-image: url(${path}/light/svg/vertical_line__guides-stroke-inactive.svg) 0;
}
QTreeView::branch:active {
    border-image: url(${path}/light/svg/vertical_line__icon-foreground.svg) 0;
}
QTreeView::branch:disabled {
    border-image: url(${path}/light/svg/vertical_line__icon-foreground-disabled.svg) 0;
}
QTreeView::branch:has-siblings:adjoins-item,
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: unset;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: unset;
    image: url(${path}/light/svg/chevron_right__icon-foreground.svg);
}
QTreeView::branch:has-children:!has-siblings:closed:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled {
    image: url(${path}/light/svg/chevron_right__icon-foreground-disabled.svg);
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    border-image: unset;
    image: url(${path}/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled  {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QTableView {
    gridline-color: #58595c;
    background: #ffffff;
}
QTableView QTableCornerButton::section {
    margin: 0 1px 1px 0;
    background: #dadce0;
    border-top-left-radius: $radius{2px};
}
QTableView QTableCornerButton::section:pressed {
    background: #4ca6e5;
}
QTableView > QHeaderView{
    background: #ffffff;
}
QHeaderView {
    padding: 0;
    margin: 0;
    border: none;
    border-radius: $radius{0};
}
QHeaderView::section {
    background: #dadce0;
    text-align: left;
    padding: 0 4px;
    border: none;
}
QHeaderView::section:horizontal:on,
QHeaderView::section:vertical:on {
    border-color: #0081db;
}
QHeaderView::section:horizontal:on:disabled,
QHeaderView::section:vertical:on:disabled {
    color: #dadce0;
    border-color: #dadce0;
}
QHeaderView::section:horizontal {
    border-top: 2px solid transparent;
    margin-right: 1px;
}
QHeaderView::section:vertical {
    border-left: 2px solid transparent;
    margin-bottom: 1px;
}
QHeaderView::section:last,
QHeaderView::section:only-one {
    margin: 0;
}
QHeaderView::down-arrow {
    margin: -2px -6px -6px -6px;
    image: url(${path}/light/svg/expand_less__icon-foreground__rotate-180.svg);
}
QHeaderView::down-arrow:disabled {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled__rotate-180.svg);
}
QHeaderView::up-arrow {
    margin: -2px -6px -6px -6px;
    image: url(${path}/light/svg/expand_less__icon-foreground.svg);
}
QHeaderView::up-arrow:disabled {
    image: url(${path}/light/svg/expand_less__icon-foreground-disabled.svg);
}
QCalendarWidget {
    border: none;
}
QCalendarWidget > .QWidget {
    background: #ffffff;
    border-bottom: 1px solid #dadce0;
    border-radius: $radius{4px};
    border-bottom-left-radius: $radius{0};
    border-bottom-right-radius: $radius{0};
}
QCalendarWidget > .QWidget > QWidget {
    padding: 1px;
}
QCalendarWidget > .QWidget > QSpinBox {
    margin-left: 1px;
}
QCalendarWidget > .QWidget > QSpinBox::up-button,
QCalendarWidget > .QWidget > QSpinBox::down-button {
    margin: 1px 3px 1px 1px;
}
QCalendarWidget .QWidget > QToolButton {
    border-radius: $radius{4px};
}
QCalendarWidget > .QWidget > QToolButton::menu-indicator {
    height: 14px;
    width: 14px;
    top: 5px;
    left: 3px;
}
QCalendarWidget > QTableView {
    margin: 0;
    border: none;
    border-radius: $radius{4px};
    border-top-left-radius: $radius{0};
    border-top-right-radius: $radius{0};
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_prevmonth {
    qproperty-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-270.svg);
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_nextmonth {
    qproperty-icon: url(${path}/light/svg/arrow_upward__icon-foreground__rotate-90.svg);
}
QLineEdit,
QAbstractSpinBox {
    border: 1px solid #dadce0;
    padding: 3px 4px;
    min-height: 1em;
    background: rgba(255.000, 255.000, 255.000, 0.000);
    border-radius: $radius{4px};
}
QLineEdit:focus,
QAbstractSpinBox:focus {
    border: 1px solid #0081db;
}
QAbstractSpinBox::up-button,
QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    width: 12px;
    height: 4px;
    padding: 3px;
    border-radius: $radius{4px};
}
QAbstractSpinBox::up-button:hover,
QAbstractSpinBox::down-button:hover {
    background: #e2eafb;
}
QAbstractSpinBox::up-button {
    subcontrol-position: top right;
    margin: 3px 3px 1px 1px;
}
QAbstractSpinBox::up-arrow {
    image: url(${path}/light/svg/arrow_drop_up__icon-foreground.svg);
}
QAbstractSpinBox::up-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__icon-foreground-disabled.svg);
}
QAbstractSpinBox::down-button {
    subcontrol-position: bottom right;
    margin: 1px 3px 3px 1px;
}
QAbstractSpinBox::down-arrow {
    image: url(${path}/light/svg/arrow_drop_up__icon-foreground__rotate-180.svg);
}
QAbstractSpinBox::down-arrow:disabled {
    image: url(${path}/light/svg/arrow_drop_up__icon-foreground-disabled__rotate-180.svg);
}
QDateTimeEdit::drop-down {
    padding-right: 4px;
    width: 16px;
    image: url(${path}/light/svg/calendar_today__icon-foreground.svg);
}
QDateTimeEdit::drop-down:disabled {
    image: url(${path}/light/svg/calendar_today__icon-foreground-disabled.svg);
}
QDateTimeEdit::down-arrow[calendarPopup=true] {
    image: none;
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
    image: url(${path}/light/svg/check__icon-foreground.svg);
}
QMenu::indicator {
    width: 18px;
    background: #c4c7cc;
    margin-left: 3px;
    border-radius: $radius{4px};
}
QCheckBox,
QRadioButton {
    spacing: 8px;
}
QGroupBox::title,
QAbstractItemView::item {
    spacing: 6px;
}
QCheckBox::indicator,
QGroupBox::indicator,
QAbstractItemView::indicator,
QRadioButton::indicator {
    height: 18px;
    width: 18px;
}
QCheckBox::indicator,
QGroupBox::indicator,
QAbstractItemView::indicator {
    image: url(${path}/light/svg/check_box_outline_blank__icon-foreground.svg);
}
QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled,
QAbstractItemView::indicator:unchecked:disabled {
    image: url(${path}/light/svg/check_box_outline_blank__icon-foreground-disabled.svg);
}
QCheckBox::indicator:checked,
QGroupBox::indicator:checked,
QAbstractItemView::indicator:checked {
    image: url(${path}/light/svg/check_box__highlight.svg);
}
QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled,
QAbstractItemView::indicator:checked:disabled {
    image: url(${path}/light/svg/check_box__icon-foreground-disabled.svg);
}
QCheckBox::indicator:indeterminate,
QAbstractItemView::indicator:indeterminate {
    image: url(${path}/light/svg/indeterminate_check_box__highlight.svg);
}
QCheckBox::indicator:indeterminate:disabled,
QAbstractItemView::indicator:indeterminate:disabled {
    image: url(${path}/light/svg/indeterminate_check_box__icon-foreground-disabled.svg);
}
QRadioButton::indicator:unchecked {
    image: url(${path}/light/svg/radio_button_unchecked__icon-foreground.svg);
}
QRadioButton::indicator:unchecked:disabled {
    image: url(${path}/light/svg/radio_button_unchecked__icon-foreground-disabled.svg);
}
QRadioButton::indicator:checked {
    image: url(${path}/light/svg/radio_button_checked__highlight.svg);
}
QRadioButton::indicator:checked:disabled {
    image: url(${path}/light/svg/radio_button_checked__icon-foreground-disabled.svg);
}
QComboBox QAbstractItemView,
QStatusBar > QMenu,
QDateTimeEdit QCalendarWidget QAbstractItemView,
QDateTimeEdit QCalendarWidget .QWidget {
    margin: 0;
    border-radius: $radius{0};
    $env_patch{"version": "<6.0.0", "os": "Darwin", "value": "border-radius: $radius{4px}"};
}
QMenu,
QStatusBar > QMenu {
    $env_patch{"version": "<6.0.0", "os": "Darwin", "value": "border-radius: $radius{8px}"};
}
PlotWidget {
    padding: 0;
}
ParameterTree > .QWidget > .QWidget > .QWidget > QAbstractSpinBox::up-button,
ParameterTree > .QWidget > .QWidget > .QWidget > QAbstractSpinBox::down-button {
    margin: 2px 3px 1px 1px;
    padding: 2px;
}
ParameterTree > .QWidget > .QWidget > .QWidget > QComboBox{
    min-height: 1.2em;
}

"""
