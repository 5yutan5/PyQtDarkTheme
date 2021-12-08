"""Module loading QPalette."""
from qdarktheme.qtpy.QtGui import QColor, QPalette

_palette = QPalette()

# base
_palette.setColor(QPalette.ColorRole.WindowText, QColor(228, 231, 235, 255))
_palette.setColor(QPalette.ColorRole.Button, QColor(32, 33, 36, 255))
_palette.setColor(QPalette.ColorRole.Text, QColor(239, 241, 241, 255))
_palette.setColor(QPalette.ColorRole.ButtonText, QColor(138, 180, 247, 255))
_palette.setColor(QPalette.ColorRole.Base, QColor(32, 33, 36, 255))
_palette.setColor(QPalette.ColorRole.Window, QColor(32, 33, 36, 255))
_palette.setColor(QPalette.ColorRole.Highlight, QColor(138, 180, 247, 255))
_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(32, 33, 36, 255))
_palette.setColor(QPalette.ColorRole.Link, QColor(32, 33, 36, 255))
_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(41, 43, 46, 255))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(41, 42, 45, 255))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(228, 231, 235, 255))
_palette.setColor(QPalette.ColorRole.LinkVisited, QColor(197, 138, 248, 255))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(41, 42, 45, 255))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(228, 231, 235, 255))
if hasattr(QPalette.ColorRole, "Foreground"):
    _palette.setColor(QPalette.ColorRole.Foreground, QColor(228, 231, 235, 255))
if hasattr(QPalette.ColorRole, "PlaceholderText"):
    _palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(138, 139, 141, 255))

_palette.setColor(QPalette.ColorRole.Light, QColor(63, 64, 66, 255))
_palette.setColor(QPalette.ColorRole.Midlight, QColor(63, 64, 66, 255))
_palette.setColor(QPalette.ColorRole.Dark, QColor(228, 231, 235, 255))
_palette.setColor(QPalette.ColorRole.Mid, QColor(63, 64, 66, 255))
_palette.setColor(QPalette.ColorRole.Shadow, QColor(63, 64, 66, 255))

# disabled
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(105, 113, 119, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(105, 113, 119, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(63, 64, 66, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(83, 87, 91, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(105, 113, 119, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor(105, 113, 119, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor(105, 113, 119, 255))

# inactive
_palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor(57, 61, 65, 255))

PALETTE = _palette
