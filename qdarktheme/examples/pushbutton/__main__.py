import sys

import qdarktheme
from qdarktheme.Qt.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
main_win = QDialog()

# Create pushbutton==========================================
push_button_outlined_normal = QPushButton("Normal")
push_button_outlined_toggle = QPushButton("Toggle")
push_button_contained_normal = QPushButton("Normal")
push_button_contained_toggle = QPushButton("Toggle")
push_button_text_normal = QPushButton("Normal")
push_button_text_toggle = QPushButton("Toggle")

push_button_outlined_normal.setProperty("type", "outlined")
push_button_outlined_toggle.setProperty("type", "outlined")
push_button_contained_normal.setProperty("type", "contained")
push_button_contained_toggle.setProperty("type", "contained")
push_button_text_normal.setProperty("type", "text")
push_button_text_toggle.setProperty("type", "text")
# ===========================================================

push_button_outlined_toggle.setCheckable(True)
push_button_outlined_toggle.setChecked(True)
push_button_contained_toggle.setCheckable(True)
push_button_contained_toggle.setChecked(True)
push_button_text_toggle.setCheckable(True)
push_button_text_toggle.setChecked(True)

# Create label
group_outlined = QGroupBox("Outlined")
group_contained = QGroupBox("Contained")
group_text = QGroupBox("Text")

# Setup layout
v_layout_outlined = QVBoxLayout()
v_layout_outlined.addWidget(push_button_outlined_normal)
v_layout_outlined.addWidget(push_button_outlined_toggle)
group_outlined.setLayout(v_layout_outlined)

v_layout_contained = QVBoxLayout()
v_layout_contained.addWidget(push_button_contained_normal)
v_layout_contained.addWidget(push_button_contained_toggle)
group_contained.setLayout(v_layout_contained)

v_layout_text = QVBoxLayout()
v_layout_text.addWidget(push_button_text_normal)
v_layout_text.addWidget(push_button_text_toggle)
group_text.setLayout(v_layout_text)

h_layout_main = QHBoxLayout(main_win)
h_layout_main.addWidget(group_outlined)
h_layout_main.addWidget(group_contained)
h_layout_main.addWidget(group_text)

main_win.setMinimumSize(300, 200)

app.setStyleSheet(qdarktheme.load_stylesheet())
main_win.show()
app.exec()
