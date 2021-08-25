from qdarktheme.Qt.QtWidgets import (
    QComboBox,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QGridLayout,
    QLabel,
    QStyledItemDelegate,
    QTextEdit,
    QToolButton,
    QWidget,
)
from qdarktheme.resource_manager import get_icon


class FlexiblePopupCombobox(QComboBox):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)
        delegate = QStyledItemDelegate(parent)
        self.setItemDelegate(delegate)

    def showPopup(self) -> None:
        width = self.view().sizeHintForColumn(0) + 20
        self.view().setMinimumWidth(width)
        super().showPopup()


class UI:
    def setup_ui(self, win: QWidget) -> None:
        # Attribute
        self.combobox_theme = FlexiblePopupCombobox()
        self.textedit_stylesheet = QTextEdit()
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.StandardButton.Close | QDialogButtonBox.StandardButton.Ok)
        self.label_stylesheet_info = QLabel()
        self.tool_button_copy_all = QToolButton()

        self.folder_dialog = QFileDialog(win)

        # Setup widget
        win.setWindowTitle("Template Creator")
        self.combobox_theme.addItems(["Light Theme", "Dark Theme"])
        self.combobox_theme.setCurrentIndex(1)
        self.textedit_stylesheet.setReadOnly(True)
        self.textedit_stylesheet.setUndoRedoEnabled(False)
        self.textedit_stylesheet.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textedit_stylesheet.setMinimumHeight(300)
        self.label_stylesheet_info.setText(
            "Copy and paste the dark theme stylesheet shown below "
            "into the stylesheet property of the top-level widget."
        )
        self.buttonbox.button(QDialogButtonBox.StandardButton.Ok).setText("Create")
        self.tool_button_copy_all.setIcon(get_icon("copy_all"))
        self.tool_button_copy_all.setToolTip("Copy All")

        # self.folder_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.folder_dialog.setFileMode(QFileDialog.FileMode.Directory)

        # Setup qss
        self.buttonbox.button(QDialogButtonBox.StandardButton.Close).setProperty("type", "text")
        self.buttonbox.button(QDialogButtonBox.StandardButton.Ok).setProperty("type", "contained")

        # Layout
        g_layout_textedit = QGridLayout()
        g_layout_textedit.addWidget(self.tool_button_copy_all, 0, 1)
        g_layout_textedit.setColumnStretch(0, 1)
        g_layout_textedit.setRowStretch(1, 1)
        self.textedit_stylesheet.setLayout(g_layout_textedit)

        f_layout = QFormLayout(win)
        f_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        f_layout.addRow("Theme:", self.combobox_theme)
        f_layout.addRow("Style Sheet:", self.label_stylesheet_info)
        f_layout.addWidget(self.textedit_stylesheet)
        f_layout.addWidget(self.buttonbox)
