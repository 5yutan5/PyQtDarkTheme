"""This example demonstrates getting theme color."""
import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication

import qdarktheme

app = QApplication(sys.argv)
dark_palette = qdarktheme.load_palette()
palette = app.palette()
palette.setColor(QPalette.ColorRole.Link, dark_palette.link().color())
