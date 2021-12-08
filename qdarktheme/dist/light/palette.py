"""Module loading QPalette."""
from qdarktheme.qtpy.QtGui import QColor, QPalette

_palette = QPalette()

# base
_palette.setColor(QPalette.ColorRole.WindowText, QColor(77, 81, 87, 255))
_palette.setColor(QPalette.ColorRole.Button, QColor(248, 249, 250, 255))
_palette.setColor(QPalette.ColorRole.Text, QColor(77, 81, 87, 255))
_palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 129, 219, 255))
_palette.setColor(QPalette.ColorRole.Base, QColor(248, 249, 250, 255))
_palette.setColor(QPalette.ColorRole.Window, QColor(248, 249, 250, 255))
_palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 129, 219, 255))
_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(248, 249, 250, 255))
_palette.setColor(QPalette.ColorRole.Link, QColor(248, 249, 250, 255))
_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(233, 236, 239, 255))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255, 255))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(77, 81, 87, 255))
_palette.setColor(QPalette.ColorRole.LinkVisited, QColor(102, 0, 152, 255))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255, 255))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(77, 81, 87, 255))
if hasattr(QPalette.ColorRole, "Foreground"):
    _palette.setColor(QPalette.ColorRole.Foreground, QColor(77, 81, 87, 255))
if hasattr(QPalette.ColorRole, "PlaceholderText"):
    _palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(105, 106, 108, 255))

_palette.setColor(QPalette.ColorRole.Light, QColor(218, 220, 224, 255))
_palette.setColor(QPalette.ColorRole.Midlight, QColor(218, 220, 224, 255))
_palette.setColor(QPalette.ColorRole.Dark, QColor(77, 81, 87, 255))
_palette.setColor(QPalette.ColorRole.Mid, QColor(218, 220, 224, 255))
_palette.setColor(QPalette.ColorRole.Shadow, QColor(218, 220, 224, 255))

# disabled
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(186, 189, 194, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(186, 189, 194, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(218, 220, 224, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(218, 220, 224, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(186, 189, 194, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor(186, 189, 194, 255))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor(186, 189, 194, 255))

# inactive
_palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor(228, 230, 242, 255))

PALETTE = _palette
