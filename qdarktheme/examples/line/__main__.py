import sys

import qdarktheme
from qdarktheme.qtpy.QtWidgets import QApplication, QDialog, QFrame, QGridLayout, QLabel

app = QApplication(sys.argv)
main_win = QDialog()

# Create line=======================
h_line, v_line = QFrame(), QFrame()
h_line.setProperty("type", "h_line")
v_line.setProperty("type", "v_line")
# ==================================

area1, area2, area3 = QLabel("Area 1"), QLabel("Area 2"), QLabel("Area 3")

# Setup layout
g_layout = QGridLayout(main_win)
g_layout.addWidget(area1, 0, 0)
g_layout.addWidget(h_line, 1, 0)
g_layout.addWidget(area2, 2, 0)
g_layout.addWidget(v_line, 0, 1, 3, 1)
g_layout.addWidget(area3, 0, 2, 3, 1)

main_win.setMinimumSize(300, 200)

app.setStyleSheet(qdarktheme.load_stylesheet())
main_win.show()
app.exec()
