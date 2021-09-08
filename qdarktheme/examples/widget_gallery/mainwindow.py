import qdarktheme
from qdarktheme.examples.widget_gallery.ui.main_ui import UI
from qdarktheme.qtpy.QtCore import Slot
from qdarktheme.qtpy.QtWidgets import QApplication, QColorDialog, QFileDialog, QMainWindow


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
        for action in self._ui.actions_theme:
            action.triggered.connect(self._change_theme)

    @Slot()
    def _open_file_dialog(self) -> None:
        QFileDialog.getOpenFileName(self, "Open File", options=QFileDialog.Option.DontUseNativeDialog)

    @Slot()
    def _open_color_dialog(self) -> None:
        QColorDialog.getColor(parent=self, options=QColorDialog.ColorDialogOption.DontUseNativeDialog)

    @Slot()
    def _change_home_win(self) -> None:
        self._ui.stack_widget.setCurrentIndex(0)
        self._ui.action_change_home_window.setChecked(True)
        self._ui.action_change_dock_window.setChecked(False)

    @Slot()
    def _change_dock_win(self) -> None:
        self._ui.stack_widget.setCurrentIndex(1)
        self._ui.action_change_home_window.setChecked(False)
        self._ui.action_change_dock_window.setChecked(True)

    @Slot()
    def _enable(self) -> None:
        self._ui.central_window.centralWidget().setEnabled(True)
        self._ui.action_enable.setEnabled(False)
        self._ui.action_disable.setEnabled(True)
        self.statusBar().showMessage("Enable")

    @Slot()
    def _disable(self) -> None:
        self._ui.central_window.centralWidget().setEnabled(False)
        self._ui.action_enable.setEnabled(True)
        self._ui.action_disable.setEnabled(False)
        self.statusBar().showMessage("Disable")

    @Slot()
    def _change_theme(self) -> None:
        theme = self.sender().text()
        QApplication.instance().setStyleSheet(qdarktheme.load_stylesheet(theme))
