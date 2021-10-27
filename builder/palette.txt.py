from qdarktheme.qtpy.QtGui import QColor, QPalette

_palette = QPalette()

# base
_palette.setColor(QPalette.ColorRole.WindowText, QColor("$text"))
_palette.setColor(QPalette.ColorRole.Button, QColor("$base"))
_palette.setColor(QPalette.ColorRole.Text, QColor("$text"))
_palette.setColor(QPalette.ColorRole.ButtonText, QColor("$highlight"))
_palette.setColor(QPalette.ColorRole.Base, QColor("$input-line"))
_palette.setColor(QPalette.ColorRole.Window, QColor("$base"))
_palette.setColor(QPalette.ColorRole.Highlight, QColor("$highlight"))
_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("$highlight-text"))
_palette.setColor(QPalette.ColorRole.Link, QColor("$highlight-text"))
_palette.setColor(QPalette.ColorRole.AlternateBase, QColor("$itemview-alternate"))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("$popup"))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("$popup-text"))
_palette.setColor(QPalette.ColorRole.LinkVisited, QColor("$link-visited"))
if hasattr(QPalette.ColorRole, "PlaceholderText"):
    _palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("$placeholder-text"))

# disabled
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor("$text-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor("$text-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor("$button-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor("$highlight-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor("$text-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor("$text-disabled"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor("$text-disabled"))

# inactive
_palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor("$itemview-highlight-inactive"))

PALETTE = _palette
