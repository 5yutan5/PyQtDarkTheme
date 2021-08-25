import sys

import qdarktheme
from qdarktheme.Qt.QtWidgets import QApplication, QDialog, QLineEdit, QVBoxLayout

app = QApplication(sys.argv)
main_win = QDialog()

# Create lineedit================================
lineedit_normal, lineedit_warning, lineedit_error = QLineEdit(), QLineEdit(), QLineEdit()
lineedit_warning.setProperty("state", "warning")
lineedit_error.setProperty("state", "error")
# ===============================================

lineedit_normal.setPlaceholderText("Normal")
lineedit_warning.setPlaceholderText("Warning")
lineedit_error.setPlaceholderText("Error")

# Setup layout
v_layout = QVBoxLayout(main_win)
v_layout.addWidget(lineedit_normal)
v_layout.addWidget(lineedit_warning)
v_layout.addWidget(lineedit_error)

main_win.setMinimumSize(300, 200)

app.setStyleSheet(qdarktheme.load_stylesheet())
main_win.show()
app.exec()
