from qdarktheme import load_stylesheet
from qdarktheme.examples.widget_gallery.ui.main_ui import UI
from qdarktheme.qtpy.QtCore import Slot
from qdarktheme.qtpy.QtWidgets import QApplication, QColorDialog, QFileDialog, QMainWindow
from qdarktheme.icon_manager import get_icon


class WidgetGallery(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._ui = UI()
        self._ui.setup_ui(self)
        self._setup()

    def _setup(self) -> None:
        self._ui.action_change_home_window.triggered.connect(self._change_home_win)
        self._ui.action_change_dock_window.triggered.connect(self._change_dock_win)
        self._ui.action_open_folder.triggered.connect(self._open_file_dialog)
        self._ui.action_open_color_dialog.triggered.connect(self._open_color_dialog)
        self._ui.action_enable.triggered.connect(self._enable)
        self._ui.action_disable.triggered.connect(self._disable)
        self._ui.action_toggle_theme.triggered.connect(self._toggle_theme)

    @Slot()  # type: ignore  <- Fix pyi file problem of PySide6
    def _open_file_dialog(self) -> None:
        QFileDialog.getOpenFileName(self, "Open File", options=QFileDialog.Option.DontUseNativeDialog)

    @Slot()  # type: ignore
    def _open_color_dialog(self) -> None:
        QColorDialog.getColor(parent=self, options=QColorDialog.ColorDialogOption.DontUseNativeDialog)

    @Slot()  # type: ignore
    def _change_home_win(self) -> None:
        self._ui.stack_widget.setCurrentIndex(0)
        self._ui.action_change_home_window.setChecked(True)
        self._ui.action_change_dock_window.setChecked(False)

    @Slot()  # type: ignore
    def _change_dock_win(self) -> None:
        self._ui.stack_widget.setCurrentIndex(1)
        self._ui.action_change_home_window.setChecked(False)
        self._ui.action_change_dock_window.setChecked(True)

    @Slot()  # type: ignore
    def _enable(self) -> None:
        self._ui.central_window.centralWidget().setEnabled(True)
        self._ui.action_enable.setEnabled(False)
        self._ui.action_disable.setEnabled(True)
        self.statusBar().showMessage("Enable")

    @Slot()  # type: ignore
    def _disable(self) -> None:
        self._ui.central_window.centralWidget().setEnabled(False)
        self._ui.action_enable.setEnabled(True)
        self._ui.action_disable.setEnabled(False)
        self.statusBar().showMessage("Disable")

    @Slot()  # type: ignore
    def _toggle_theme(self) -> None:
        if self._ui.action_toggle_theme.text() == "Change to a dark theme":
            self._ui.action_toggle_theme.setIcon(get_icon("dark_mode"))
            self._ui.action_toggle_theme.setText("Change to a light theme")
            q_app: QApplication = QApplication.instance()
            q_app.setStyleSheet(load_stylesheet("dark"))
        else:
            self._ui.action_toggle_theme.setIcon(get_icon("light_mode"))
            self._ui.action_toggle_theme.setText("Change to a dark theme")
            q_app: QApplication = QApplication.instance()
            q_app.setStyleSheet(load_stylesheet("light"))
