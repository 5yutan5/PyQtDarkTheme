"""Module setting up ui of mdi window."""
from qdarktheme.qtpy.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMdiArea,
    QMdiSubWindow,
    QPushButton,
    QSplitter,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class MdiUI:
    """The ui class of mdi window."""

    def _make_mdi_area_test_widget(self, enable_tab_mode=False):
        # Widgets
        container = QWidget()
        mdi_area = QMdiArea()
        label_test_name = QLabel()
        cascade_button = QPushButton("Cascade")
        new_button = QPushButton("Add new")
        tiled_button = QPushButton("Tiled")

        # Setup widgets
        if enable_tab_mode:
            mdi_area.setViewMode(QMdiArea.ViewMode.TabbedView)
            label_test_name.setText("QMdiArea(QMdiArea.viewMode = TabbedView)")
        else:
            label_test_name.setText("QMdiArea(QMdiArea.viewMode = SubWindowView)")

        def add_new_sub_window():
            sub_win = QMdiSubWindow(container)
            sub_win_main_widget = QWidget(sub_win)
            v_layout = QVBoxLayout(sub_win_main_widget)
            v_layout.addWidget(QTextEdit("Sub window"))

            sub_win.setWidget(sub_win_main_widget)
            mdi_area.addSubWindow(sub_win)
            sub_win.show()

        add_new_sub_window()
        new_button.pressed.connect(add_new_sub_window)
        cascade_button.pressed.connect(mdi_area.cascadeSubWindows)
        tiled_button.pressed.connect(mdi_area.tileSubWindows)
        new_button.setDefault(True)

        # Layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(new_button)
        h_layout.addWidget(cascade_button)
        h_layout.addWidget(tiled_button)

        v_main_layout = QVBoxLayout(container)
        v_main_layout.addWidget(label_test_name)
        v_main_layout.addLayout(h_layout)
        v_main_layout.addWidget(mdi_area)
        return container

    def setup_ui(self, win: QWidget) -> None:
        """Set up ui."""
        # Widgets
        splitter = QSplitter()

        # Setup widgets
        mdi_area = self._make_mdi_area_test_widget()
        mdi_area_with_tab = self._make_mdi_area_test_widget(enable_tab_mode=True)

        # Layout
        splitter.addWidget(mdi_area)
        splitter.addWidget(mdi_area_with_tab)

        main_layout = QVBoxLayout(win)
        main_layout.addWidget(splitter)
