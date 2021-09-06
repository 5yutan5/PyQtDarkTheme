from qdarktheme.designer_supporter.template import TemplateGenerator, convert_stylesheet_for_designer
from qdarktheme.designer_supporter.ui import UI
from qdarktheme.qtpy.QtCore import Slot
from qdarktheme.qtpy.QtWidgets import QApplication, QDialog
from qdarktheme.resource_manager import load_stylesheet


class MainDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self._ui = UI()
        self._ui.setup_ui(self)
        self._theme = "dark"
        self._setup()

    def _setup(self) -> None:
        self._ui.combobox_theme.currentIndexChanged.connect(self._toggle_theme)
        self._ui.tool_button_copy_all.clicked.connect(self._copy_all)
        self._ui.buttonbox.accepted.connect(self._create_template)
        self._ui.buttonbox.rejected.connect(self._quit)

        self._toggle_theme()

    @Slot()  # type: ignore
    def _create_template(self) -> None:
        if not self._ui.folder_dialog.exec():
            return
        folder_path = self._ui.folder_dialog.selectedFiles()[0]
        template_generator = TemplateGenerator(folder_path, self._theme)
        template_generator.generate()

    @Slot()  # type: ignore
    def _quit(self) -> None:
        self.close()

    @Slot()  # type: ignore
    def _toggle_theme(self) -> None:
        self._theme = "dark" if self._ui.combobox_theme.currentText() == "Dark Theme" else "light"
        stylesheet = load_stylesheet(self._theme)
        stylesheet_for_designer = convert_stylesheet_for_designer(stylesheet)
        self._ui.textedit_stylesheet.setText(stylesheet_for_designer)

        textedit_width = int(self._ui.textedit_stylesheet.document().idealWidth() + 1)
        textedit_width += self._ui.textedit_stylesheet.contentsMargins().left()
        textedit_width += self._ui.textedit_stylesheet.contentsMargins().right()
        textedit_width += self._ui.textedit_stylesheet.verticalScrollBar().width()

        self._ui.textedit_stylesheet.setMinimumWidth(textedit_width if textedit_width < 700 else 700)

    @Slot()  # type: ignore
    def _copy_all(self) -> None:
        QApplication.clipboard().setText(self._ui.textedit_stylesheet.toPlainText())
