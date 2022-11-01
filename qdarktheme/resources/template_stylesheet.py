"""Template stylesheet."""

TEMPLATE_STYLESHEET = """
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
    background: {{ background|color }};
    color: {{ foreground|color }};
    selection-color: {{ foreground|color }};
    selection-background-color: {{ primary|color(state="selection.background") }};
}
QWidget:disabled {
    color: {{ foreground|color(state="disabled") }};
    selection-background-color: {{ foreground|color(state="disabledSelectionBackground") }};
    selection-color: {{ foreground|color(state="disabled") }};
}
QWidget {
    backward-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=270) }};
    forward-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=90) }};
    leftarrow-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=270) }};
    rightarrow-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=90) }};
    dialog-ok-icon: {{ foreground|color(state="icon")|url(id="check") }};
    dialog-cancel-icon: {{ foreground|color(state="icon")|url(id="close") }};
    dialog-yes-icon: {{ foreground|color(state="icon")|url(id="check_circle") }};
    dialog-no-icon: {{ foreground|color(state="icon")|url(id="cancel") }};
    dialog-apply-icon: {{ foreground|color(state="icon")|url(id="check") }};
    dialog-reset-icon: {{ foreground|color(state="icon")|url(id="restart_alt") }};
    dialog-save-icon: {{ foreground|color(state="icon")|url(id="save") }};
    dialog-discard-icon: {{ foreground|color(state="icon")|url(id="delete") }};
    dialog-close-icon: {{ foreground|color(state="icon")|url(id="close") }};
    dialog-open-icon: {{ foreground|color(state="icon")|url(id="folder_open") }};
    dialog-help-icon: {{ foreground|color(state="icon")|url(id="help") }};
    filedialog-parent-directory-icon: {{ foreground|color(state="icon")|url(id="arrow_upward") }};
    filedialog-new-directory-icon: {{ foreground|color(state="icon")|url(id="create_new_folder") }};
    titlebar-close-icon: {{ foreground|color(state="icon")|url(id="close") }};
    titlebar-normal-icon: {{ foreground|color(state="icon")|url(id="flip_to_front") }};
}
QCommandLinkButton {
    qproperty-icon: {{ primary|color|url(id="east") }};
}
QCheckBox:!window,
QRadioButton:!window,
QPushButton:!window,
QLabel:!window,
QLCDNumber:!window {
    background: transparent;
}
QMdiSubWindow > QCheckBox:!window,
QMdiSubWindow > QRadioButton:!window,
QMdiSubWindow > QPushButton:!window,
QMdiSubWindow > QLabel:!window,
QMdiSubWindow > QLCDNumber:!window {
    background: {{ background|color }};
}
QMainWindow::separator {
    width: 4px;
    height: 4px;
    background: {{ border|color }};
}
QMainWindow::separator:hover,
QMainWindow::separator:pressed {
    background: {{ primary|color }};
}
QToolTip {
    background: {{ background|color(state="popup") }};
    color: {{ foreground|color }};
}
QSizeGrip {
    width: 0;
    height: 0;
    image: none;
}
QStatusBar {
    background: {{ statusBar.background|color }};
}
QStatusBar::item {
    border: none;
}
QStatusBar QWidget {
    background: transparent;
    padding: 3px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QStatusBar > .QSizeGrip {
    padding: 0;
}
QStatusBar QWidget:hover {
    background: {{ statusBarItem.hoverBackground|color }};
}
QStatusBar QWidget:pressed,
QStatusBar QWidget:checked {
    background: {{ statusBarItem.activeBackground|color }};
}
QCheckBox,
QRadioButton {
    border-top: 2px solid transparent;
    border-bottom: 2px solid transparent;
}
QCheckBox:hover,
QRadioButton:hover {
    border-bottom: 2px solid {{ primary|color }};
}
QGroupBox {
    font-weight: bold;
    margin-top: 8px;
    padding: 2px 1px 1px 1px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
    border: 1px solid {{ border|color }};
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
    padding: 2px;
    border-bottom: 1px solid {{ border|color }};
    background: {{ background|color }};
}
QMenuBar::item {
    background: transparent;
    padding: 4px;
}
QMenuBar::item:selected {
    padding: 4px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
    background: {{ menubar.selectionBackground|color }};
}
QMenuBar::item:pressed {
    padding: 4px;
    margin-bottom: 0;
    padding-bottom: 0;
}
QToolBar {
    padding: 1px;
    font-weight: bold;
    spacing: 2px;
    margin: 1px;
    background: {{ toolbar.background|color }};
}
QToolBar::handle:horizontal {
    width: 20px;
    image: {{ foreground|color(state="icon")|url(id="drag_indicator_horizontal") }};
}
QToolBar::handle:vertical {
    height: 20px;
    image: {{ foreground|color(state="icon")|url(id="drag_indicator_horizontal", rotate=90) }};
}
QToolBar::separator {
    background: {{ border|color }};
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
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QToolBar > QToolButton:hover {
    background: {{ toolbar.hoverBackground|color }};
}
QToolBar > QToolButton:pressed,
QToolBar > QToolButton::menu-button:pressed:!disabled,
QToolBar > QToolButton:checked:!disabled {
    background: {{ toolbar.activeBackground|color }};
}
QToolBar > QToolButton#qt_toolbar_ext_button {
    image: {{ foreground|color(state="icon")|url(id="double_arrow") }};
    {{ |env(value="padding: 0; qproperty-icon: unset", os="Windows")}}
}
QToolBar > QToolButton#qt_toolbar_ext_button:disabled {
    image: {{ foreground|color(state="disabled")|url(id="double_arrow") }};
}
QToolBar > QWidget {
    background: transparent;
}
QMenu {
    background: {{ background|color(state="popup") }};
    padding: 8px 0;
    border: 1px solid {{ border|color }};
}
QMenu::separator {
    margin: 4px 0;
    height: 1px;
    background: {{ border|color }};
}
QMenu::item {
    padding: 4px 28px;
}
QMenu::item:selected {
    background: {{ popupItem.selectionBackground|color }};
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
    image: {{ foreground|color(state="icon")|url(id="chevron_right") }};
}
QMenu::right-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="chevron_right") }};
}
QScrollBar {
    background: {{ scrollbar.background|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
    {{ |env(value="background: transparent", os="Darwin")}}
}
QScrollBar:horizontal {
    height: 14px;
    {{ |env(value="height: 7px;", os="Darwin") }}
}
QScrollBar:vertical {
    width: 14px;
    {{ |env(value="width: 7px;", os="Darwin") }}
}
QScrollBar::handle {
    background: {{ scrollbarSlider.background|color }};
    border-radius: {{ corner-shape|corner(size=3) }}px;
}
QScrollBar::handle:hover {
    background: {{ scrollbarSlider.hoverBackground|color }};
}
QScrollBar::handle:pressed {
    background: {{ scrollbarSlider.activeBackground|color }};
}
QScrollBar::handle:disabled {
    background: {{ scrollbarSlider.disabledBackground|color }};
}
QScrollBar::handle:horizontal {
    min-width: 8px;
    margin: 4px 14px;
    {{ |env(value="margin: 0;", os="Darwin") }}
}
QScrollBar::handle:horizontal:hover {
    margin: 2px 14px;
    {{ |env(value="margin: 0;", os="Darwin") }}
}
QScrollBar::handle:vertical {
    min-height: 8px;
    margin: 14px 4px;
    {{ |env(value="margin: 0;", os="Darwin") }}
}
QScrollBar::handle:vertical:hover {
    margin: 14px 2px;
    {{ |env(value="margin: 0;", os="Darwin") }}
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
    {{ |env(value="width: 0; height: 0; margin: 0", os="Darwin") }}
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
    image: {{ scrollbarSlider.background|color|url(id="arrow_drop_up") }};
}
QScrollBar::right-arrow {
    image: {{ scrollbarSlider.background|color|url(id="arrow_drop_up", rotate=90) }};
}
QScrollBar::down-arrow {
    image: {{ scrollbarSlider.background|color|url(id="arrow_drop_up", rotate=180) }};
}
QScrollBar::left-arrow {
    image: {{ scrollbarSlider.background|color|url(id="arrow_drop_up", rotate=270) }};
}
QScrollBar::up-arrow:hover {
    image: {{ scrollbarSlider.activeBackground|color|url(id="arrow_drop_up") }};
}
QScrollBar::right-arrow:hover {
    image: {{ scrollbarSlider.activeBackground|color|url(id="arrow_drop_up", rotate=90) }};
}
QScrollBar::down-arrow:hover {
    image: {{ scrollbarSlider.activeBackground|color|url(id="arrow_drop_up", rotate=180) }};
}
QScrollBar::left-arrow:hover {
    image: {{ scrollbarSlider.activeBackground|color|url(id="arrow_drop_up", rotate=270) }};
}
QScrollBar::up-arrow:disabled {
    image: {{ scrollbarSlider.disabledBackground|color|url(id="arrow_drop_up") }};
}
QScrollBar::right-arrow:disabled {
    image: {{ scrollbarSlider.disabledBackground|color|url(id="arrow_drop_up", rotate=90) }};
}
QScrollBar::down-arrow:disabled {
    image: {{ scrollbarSlider.disabledBackground|color|url(id="arrow_drop_up", rotate=180) }};
}
QScrollBar::left-arrow:disabled {
    image: {{ scrollbarSlider.disabledBackground|color|url(id="arrow_drop_up", rotate=270) }};
}
QProgressBar {
    text-align: center;
    border: 1px solid {{ border|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QProgressBar::chunk {
    background: {{ primary|color(state="progressBar.background") }};
    border-radius: {{ corner-shape|corner(size=3) }}px;
}
QProgressBar::chunk:disabled {
    background: {{ foreground|color(state="progressBar.disabledBackground") }};
}
QPushButton {
    color: {{ primary|color }};
    border: 1px solid {{ border|color }};
    padding: 4px 8px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QPushButton:flat,
QPushButton:default {
    border: none;
    padding: 5px 9px;
}
QPushButton:default {
    color: {{ background|color }};
    background: {{ primary|color }};
}
QPushButton:hover {
    background: {{ primary|color(state="button.hoverBackground") }};
}
QPushButton:pressed {
    background: {{ primary|color(state="button.activeBackground") }};
}
QPushButton:checked:!disabled {
    background: {{ primary|color(state="button.activeBackground") }};
}
QPushButton:default:hover {
    background: {{ primary|color(state="defaultButton.hoverBackground") }};
}
QPushButton:default:pressed {
    background: {{ primary|color(state="defaultButton.activeBackground") }};
}
QPushButton:default:disabled {
    background: {{ foreground|color(state="defaultButton.disabledBackground") }};
}
QDialogButtonBox QPushButton {
    min-width: 65px;
}
QToolButton {
    background: transparent;
    padding: 5px;
    spacing: 2px;
    border-radius: {{ corner-shape|corner(size=2) }}px;
}
QToolButton:hover {
    background: {{ primary|color(state="button.hoverBackground") }};
}
QToolButton:pressed,
QToolButton:checked:pressed,
QToolButton::menu-button:pressed:!disabled {
    background: {{ primary|color(state="button.activeBackground") }};
}
QToolButton:selected:!disabled,
QToolButton:checked:!disabled {
    background: {{ primary|color(state="button.activeBackground") }};
}
QToolButton::menu-indicator {
    height: 18px;
    width: 18px;
    top: 6px;
    left: 3px;
    image: {{ foreground|color(state="icon")|url(id="expand_less", rotate=180) }};
}
QToolButton::menu-indicator:disabled {
    image: {{ foreground|color(state="disabled")|url(id="expand_less", rotate=180) }};
}
QToolButton::menu-arrow {
    image: unset;
}
QToolButton::menu-button {
    subcontrol-origin: margin;
    border: none;
    width: 17px;
    border-top-right-radius: {{ corner-shape|corner(size=4) }}px;
    border-bottom-right-radius: {{ corner-shape|corner(size=4) }}px;
    image: {{ foreground|color(state="icon")|url(id="expand_less", rotate=180) }};
}
QToolButton::menu-button:disabled {
    image: {{ foreground|color(state="disabled")|url(id="expand_less", rotate=180) }};
}
QToolButton[
{{ |env(value="popupMode=MenuButtonPopup", version="<6.0.0", qt="PySide2") }}
{{ |env(value="popupMode=\\\"1\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="popupMode=MenuButtonPopup", version=">=6.0.0") }}
] {
    padding-right: 1px;
    margin-right: 18px;
    border-top-right-radius: {{ corner-shape|corner(size=0) }};
    border-bottom-right-radius: {{ corner-shape|corner(size=0) }};
}
QComboBox {
    min-height: 1.5em;
    padding: 0 4px;
    background: {{ input.background|color }};
    border: 1px solid {{ border|color(state="input") }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QComboBox:focus,
QComboBox:open {
    border-color: {{ primary|color }};
}
QComboBox::drop-down {
    border: none;
    padding-right: 4px;
}
QComboBox::down-arrow {
    image: {{ foreground|color(state="icon")|url(id="expand_less", rotate=180) }};
}
QComboBox::down-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="expand_less", rotate=180) }};
}
QComboBox::item:selected {
    border: none;
    background: {{ primary|color(state="itemView.selectionBackground") }};
}
QComboBox QAbstractItemView {
    background: {{ background|color(state="popup") }};
    margin: 0;
    border: 1px solid {{ border|color }};
    padding: 2px;
}
QComboBox QAbstractItemView[
{{ |env(value="frameShape=\\\"0\\\"", version="<6.0.0")}}
{{ |env(value="frameShape=NoFrame", version=">=6.0.0") }}
] {
    border-color: {{ border|color }};
}
QSlider {
    padding: 2px 0;
}
QSlider::groove {
    border-radius: {{ corner-shape|corner(size=2) }}px;
}
QSlider::groove:horizontal {
    height: 4px;
}
QSlider::groove:vertical {
    width: 4px;
}
QSlider::sub-page, QSlider::handle {
    background: {{ primary|color }};
}
QSlider::sub-page:disabled,
QSlider::handle:disabled {
    background: {{ foreground|color(state="slider.disabledBackground") }};
}
QSlider::add-page {
    background: {{ foreground|color(state="sliderTrack.inactiveBackground") }};
}
QSlider::handle:hover,
QSlider::handle:pressed {
    background: {{ primary|color(state="sliderHandle.activeBackground") }};
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
    border: 1px solid {{ border|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QTabBar {
    qproperty-drawBase: 0;
}
QTabBar::close-button:selected {
    image: {{ foreground|color(state="icon")|url(id="close") }};
}
QTabBar::close-button:!selected {
    image: {{ foreground|color(state="icon.unfocused")|url(id="close") }};
}
QTabBar::close-button:disabled {
    image: {{ foreground|color(state="disabled")|url(id="close") }};
}
QTabBar::close-button:hover {
    background: {{ tabCloseButton.hoverBackground|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QTabBar::tab {
    padding: 3px;
    border-style: solid;
}
QTabBar::tab:hover,
QTabBar::tab:selected:hover:!disabled {
    background: {{ tab.hoverBackground|color }};
}
QTabBar::tab:selected:!disabled {
    color: {{ primary|color }};
    background: {{ tab.activeBackground|color }};
    border-color: {{ primary|color }};
}
QTabBar::tab:selected:disabled,
QTabBar::tab:only-one:selected:!disabled {
    border-color: {{ border|color }};
}
QTabBar::tab:top {
    border-bottom-width: 2px;
    margin: 3px 6px 0 0;
    border-top-left-radius: {{ corner-shape|corner(size=2) }}px;
    border-top-right-radius: {{ corner-shape|corner(size=2) }}px;
}
QTabBar::tab:bottom {
    border-top-width: 2px;
    margin: 0 6px 3px 0;
    border-bottom-left-radius: {{ corner-shape|corner(size=2) }}px;
    border-bottom-right-radius: {{ corner-shape|corner(size=2) }}px;
}
QTabBar::tab:left {
    border-right-width: 2px;
    margin: 0 0 6px 3px;
    border-top-left-radius: {{ corner-shape|corner(size=2) }}px;
    border-bottom-left-radius: {{ corner-shape|corner(size=2) }}px;
}
QTabBar::tab:right {
    border-left-width: 2px;
    margin-bottom: 6px;
    margin: 0 3px 6px 0;
    border-top-right-radius: {{ corner-shape|corner(size=2) }}px;
    border-bottom-right-radius: {{ corner-shape|corner(size=2) }}px;
}
QTabBar::tab:top:first,
QTabBar::tab:top:only-one,
QTabBar::tab:bottom:first,
QTabBar::tab:bottom:only-one {
    margin-left: 2px;
}
QTabBar::tab:top:last,
QTabBar::tab:top:only-one,
QTabBar::tab:bottom:last,
QTabBar::tab:bottom:only-one {
    margin-right: 2px;
}
QTabBar::tab:left:first,
QTabBar::tab:left:only-one,
QTabBar::tab:right:first,
QTabBar::tab:right:only-one {
    margin-top: 2px;
}
QTabBar::tab:left:last,
QTabBar::tab:left:only-one,
QTabBar::tab:right:last,
QTabBar::tab:right:only-one {
    margin-bottom: 2px;
}
QDockWidget {
    border: 1px solid {{ border|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QDockWidget::title {
    padding: 3px;
    spacing: 4px;
    background: {{ background|color(state="title") }};
}
QDockWidget::close-button,
QDockWidget::float-button {
    border-radius: {{ corner-shape|corner(size=2) }}px;
}
QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background: {{ primary|color(state="button.hoverBackground") }};
}
QDockWidget::close-button:pressed,
QDockWidget::float-button:pressed {
    background: {{ primary|color(state="button.activeBackground") }};
}
QFrame {
    border: 1px solid {{ border|color }};
    padding: 1px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
.QFrame {
    padding: 0;
}
QFrame[
{{ |env(value="frameShape=NoFrame", version="<6.0.0", qt="PySide2") }}
{{ |env(value="frameShape=\\\"0\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="frameShape=NoFrame", version=">=6.0.0") }}
] {
    border-color: transparent;
    padding: 0;
}
.QFrame[
{{ |env(value="frameShape=NoFrame", version="<6.0.0", qt="PySide2") }}
{{ |env(value="frameShape=\\\"0\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="frameShape=NoFrame", version=">=6.0.0") }}
] {
    border: none;
}
QFrame[
{{ |env(value="frameShape=Panel", version="<6.0.0", qt="PySide2") }}
{{ |env(value="frameShape=\\\"2\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="frameShape=Panel", version=">=6.0.0") }}
] {
    border-color: {{ background|color(state="panel") }};
    background: {{ background|color(state="panel") }};
}
QFrame[
{{ |env(value="frameShape=HLine", version="<6.0.0", qt="PySide2") }}
{{ |env(value="frameShape=\\\"4\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="frameShape=HLine", version=">=6.0.0") }}
] {
    max-height: 2px;
    border: none;
    background: {{ border|color }};
}
QFrame[
{{ |env(value="frameShape=VLine", version="<6.0.0", qt="PySide2") }}
{{ |env(value="frameShape=\\\"5\\\"", version="<6.0.0", qt="PyQt5") }}
{{ |env(value="frameShape=VLine", version=">=6.0.0") }}
] {
    max-width: 2px;
    border: none;
    background: {{ border|color }};
}
QLCDNumber {
    min-width: 2em;
    margin: 2px;
}
QToolBox:selected {
    border: 2px solid {{ primary|color }};
}
QToolBox::tab {
    background: {{ background|color(state="title") }};
    border-bottom: 2px solid {{ border|color }};
    border-top-left-radius: {{ corner-shape|corner(size=4) }}px;
    border-top-right-radius: {{ corner-shape|corner(size=4) }}px;
}
QToolBox::tab:selected:!disabled {
    border-bottom: 2px solid {{ primary|color }};
}
QSplitter::handle {
    background: {{ border|color }};
    margin: 1px 3px;
}
QSplitter::handle:hover {
    background: {{ primary|color }};
}
QSplitter::handle:horizontal {
    width: 5px;
    image: {{ foreground|color(state="icon")|url(id="horizontal_rule", rotate=90) }};
}
QSplitter::handle:horizontal:disabled {
    image: {{ foreground|color(state="disabled")|url(id="horizontal_rule", rotate=90) }};
}
QSplitter::handle:vertical {
    height: 5px;
    image: {{ foreground|color(state="icon")|url(id="horizontal_rule") }};
}
QSplitter::handle:vertical:disabled {
    image: {{ foreground|color(state="disabled")|url(id="horizontal_rule") }};
}
QSplitterHandle::item:hover {}
QAbstractScrollArea {
    margin: 1px;
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
QMdiArea {
    qproperty-background: {{ background|color(state="panel") }};
    border-radius: 0;
}
QMdiSubWindow {
    background: {{ background|color }};
    border: 1px solid;
    padding: 0 3px;
}
QMdiSubWindow > QWidget {
    border: 1px solid {{ border|color }};
}
QTextEdit, QPlainTextEdit {
    background: {{ background|color(state="textarea") }};
}
QTextEdit:focus,
QTextEdit:selected,
QPlainTextEdit:focus,
QPlainTextEdit:selected {
    border: 1px solid {{ primary|color }};
    selection-background-color: {{ primary|color(state="textarea.selectionBackground") }};
}
QTextEdit:!focus,
QPlainTextEdit:!focus {
    {{ textarea.inactiveSelectionBackground|color|env(value="selection-background-color: ${}", version=">=5.15.0") }}
}
QTextEdit:!active,
QPlainTextEdit:!active {
    {{ textarea.inactiveSelectionBackground|color|env(value="selection-background-color: ${}", version="<5.15.0") }}
}
QAbstractItemView {
    alternate-background-color: {{ itemView.alternateBackground|color }};
    selection-background-color: {{ primary|color(state="itemView.selectionBackground") }};
}
QTreeView,
QTableView,
QTableView:disabled,
QTreeView:disabled {
    selection-background-color: {{ background|color }};
}
QAbstractItemView::item:selected,
QTreeView::branch:selected {
    background: {{ primary|color(state="itemView.selectionBackground") }};
}
QAbstractItemView::item:selected:!active,
QTreeView::branch:selected:!active {
    background: {{ itemView.inactiveSelectionBackground|color }};
}
QAbstractItemView::item:!selected:hover,
QTreeView::branch:!selected:hover {
    background: {{ itemView.hoverBackground|color }};
}
QAbstractItemView QLineEdit,
QAbstractItemView QAbstractSpinBox,
QAbstractItemView QComboBox,
QAbstractItemView QAbstractButton {
    padding: 0;
    margin: 1px;
}
QTreeView::branch {
    border-image: {{ tree.inactiveIndentGuidesStroke|color|url(id="vertical_line") }} 0;
}
QTreeView::branch:active {
    border-image: {{ tree.indentGuidesStroke|color(state="icon")|url(id="vertical_line") }} 0;
}
QTreeView::branch:has-siblings:adjoins-item,
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: unset;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    border-image: unset;
    image: {{ foreground|color(state="icon")|url(id="chevron_right") }};
}
QTreeView::branch:has-children:!has-siblings:closed:disabled,
QTreeView::branch:closed:has-children:has-siblings:disabled {
    image: {{ foreground|color(state="disabled")|url(id="chevron_right") }};
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    border-image: unset;
    image: {{ foreground|color(state="icon")|url(id="expand_less", rotate=180) }};
}
QTreeView::branch:open:has-children:!has-siblings:disabled,
QTreeView::branch:open:has-children:has-siblings:disabled  {
    image: {{ foreground|color(state="disabled")|url(id="expand_less", rotate=180) }};
}
QTableView {
    gridline-color: {{ itemViewSectionHeader.background|color }};
    background: {{ background|color(state="table") }};
}
QTableView QTableCornerButton::section {
    margin: 0 1px 1px 0;
    background: {{ itemViewSectionHeader.background|color }};
    border-top-left-radius: {{ corner-shape|corner(size=2) }}px;
}
QTableView QTableCornerButton::section:pressed {
    background: {{ primary|color(state="itemView.selectionBackground") }};
}
QTableView > QHeaderView{
    background: {{ background|color(state="table") }};
}
QHeaderView {
    padding: 0;
    margin: 0;
    border: none;
    border-radius: {{ corner-shape|corner(size=0) }};
}
QHeaderView::section {
    text-align: left;
    padding: 0 4px;
    border: none;
    background: {{ itemViewSectionHeader.background|color }};
}
QHeaderView::section:horizontal:on:!disabled,
QHeaderView::section:vertical:on:!disabled {
    border-color: {{ primary|color }};
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
    image: {{ foreground|color(state="icon")|url(id="expand_less", rotate=180) }};
}
QHeaderView::down-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="expand_less", rotate=180) }};
}
QHeaderView::up-arrow {
    margin: -2px -6px -6px -6px;
    image: {{ foreground|color(state="icon")|url(id="expand_less") }};
}
QHeaderView::up-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="expand_less") }};
}
QCalendarWidget {
    border: none;
}
QCalendarWidget > .QWidget {
    background: {{ background|color(state="table") }};
    border-bottom: 1px solid {{ border|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
    border-bottom-left-radius: {{ corner-shape|corner(size=0) }};
    border-bottom-right-radius: {{ corner-shape|corner(size=0) }};
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
    border-radius: {{ corner-shape|corner(size=4) }}px;
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
    border-radius: {{ corner-shape|corner(size=4) }}px;
    border-top-left-radius: {{ corner-shape|corner(size=0) }};
    border-top-right-radius: {{ corner-shape|corner(size=0) }};
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_prevmonth {
    qproperty-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=270) }};
}
QCalendarWidget > .QWidget > QToolButton#qt_calendar_nextmonth {
    qproperty-icon: {{ foreground|color(state="icon")|url(id="arrow_upward", rotate=90) }};
}
QLineEdit,
QAbstractSpinBox {
    padding: 3px 4px;
    min-height: 1em;
    border: 1px solid {{ border|color(state="input") }};
    background: {{ input.background|color }};
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QLineEdit:focus,
QAbstractSpinBox:focus {
    border-color: {{ primary|color }};
}
QAbstractSpinBox::up-button,
QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    width: 12px;
    height: 4px;
    padding: 3px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
}
QAbstractSpinBox::up-button:hover,
QAbstractSpinBox::down-button:hover {
    background: {{ inputButton.hoverBackground|color }};
}
QAbstractSpinBox::up-button {
    subcontrol-position: top right;
    margin: 3px 3px 1px 1px;
}
QAbstractSpinBox::up-arrow {
    image: {{ foreground|color(state="icon")|url(id="arrow_drop_up") }};
}
QAbstractSpinBox::up-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="arrow_drop_up") }};
}
QAbstractSpinBox::down-button {
    subcontrol-position: bottom right;
    margin: 1px 3px 3px 1px;
}
QAbstractSpinBox::down-arrow {
    image: {{ foreground|color(state="icon")|url(id="arrow_drop_up", rotate=180) }};
}
QAbstractSpinBox::down-arrow:disabled {
    image: {{ foreground|color(state="disabled")|url(id="arrow_drop_up", rotate=180) }};
}
QDateTimeEdit::drop-down {
    padding-right: 4px;
    width: 16px;
    image: {{ foreground|color(state="icon")|url(id="calendar_today") }};
}
QDateTimeEdit::drop-down:disabled {
    image: {{ foreground|color(state="disabled")|url(id="calendar_today") }};
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
    image: {{ foreground|color(state="icon")|url(id="check") }};
}
QMenu::indicator {
    width: 18px;
    background: {{ popupItem.checkbox.background|color }};
    margin-left: 3px;
    border-radius: {{ corner-shape|corner(size=4) }}px;
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
    image: {{ foreground|color(state="icon")|url(id="check_box_outline_blank") }};
}
QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled,
QAbstractItemView::indicator:unchecked:disabled {
    image: {{ foreground|color(state="disabled")|url(id="check_box_outline_blank") }};
}
QCheckBox::indicator:checked,
QGroupBox::indicator:checked,
QAbstractItemView::indicator:checked {
    image: {{ primary|color|url(id="check_box") }};
}
QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled,
QAbstractItemView::indicator:checked:disabled {
    image: {{ foreground|color(state="disabled")|url(id="check_box") }};
}
QCheckBox::indicator:indeterminate,
QAbstractItemView::indicator:indeterminate {
    image: {{ primary|color|url(id="indeterminate_check_box") }};
}
QCheckBox::indicator:indeterminate:disabled,
QAbstractItemView::indicator:indeterminate:disabled {
    image: {{ foreground|color(state="disabled")|url(id="indeterminate_check_box") }};
}
QRadioButton::indicator:unchecked {
    image: {{ foreground|color(state="icon")|url(id="radio_button_unchecked") }};
}
QRadioButton::indicator:unchecked:disabled {
    image: {{ foreground|color(state="disabled")|url(id="radio_button_unchecked") }};
}
QRadioButton::indicator:checked {
    image: {{ primary|color|url(id="radio_button_checked") }};
}
QRadioButton::indicator:checked:disabled {
    image: {{ foreground|color(state="disabled")|url(id="radio_button_checked") }};
}
QComboBox QAbstractItemView,
QStatusBar > QMenu,
QDateTimeEdit QCalendarWidget QAbstractItemView,
QDateTimeEdit QCalendarWidget .QWidget {
    margin: 0;
    border-radius: {{ corner-shape|corner(size=0) }};
    {{ corner-shape|corner(size=4)|env(value="border-radius: ${}px;", version="<6.0.0", os="Darwin") }}
}
QMenu,
QStatusBar > QMenu {
    {{ corner-shape|corner(size=8)|env(value="border-radius: ${}px;", version="<6.0.0", os="Darwin") }}
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

"""  # noqa: E501
