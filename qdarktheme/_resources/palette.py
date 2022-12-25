"""Module loading QPalette."""
from __future__ import annotations

from functools import partial

from qdarktheme._template.engine import Template


def q_palette(mk_template: partial[Template], color_map: dict[str, str | dict], for_stylesheet: bool):
    """Generate QPalette."""
    from qdarktheme.qtpy.QtGui import QColor, QPalette

    def _mk_q_color(text: str):
        template = mk_template(text)
        color_format = template.render(color_map)
        return QColor(color_format)

    palette = QPalette()

    if not for_stylesheet:
        # base
        palette.setColor(QPalette.ColorRole.WindowText, _mk_q_color("{{ foreground|color|palette }}"))
        palette.setColor(
            QPalette.ColorRole.Button, _mk_q_color("{{ treeSectionHeader.background|color|palette }}")
        )
        palette.setColor(QPalette.ColorRole.ButtonText, _mk_q_color("{{ primary|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Base, _mk_q_color("{{ background|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Window, _mk_q_color("{{ background|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Highlight, _mk_q_color("{{ primary|color|palette }}"))
        palette.setColor(
            QPalette.ColorRole.HighlightedText, _mk_q_color("{{ background|color|palette }}")
        )
        palette.setColor(
            QPalette.ColorRole.AlternateBase,
            _mk_q_color("{{ list.alternateBackground|color|palette }}"),
        )
        palette.setColor(
            QPalette.ColorRole.ToolTipBase, _mk_q_color('{{ background|color(state="popup")|palette }}')
        )
        palette.setColor(QPalette.ColorRole.ToolTipText, _mk_q_color("{{ foreground|color|palette }}"))
        if hasattr(QPalette.ColorRole, "Foreground"):
            palette.setColor(
                QPalette.ColorRole.Foreground,  # type: ignore
                _mk_q_color("{{ foreground|color|palette }}"),
            )

        palette.setColor(QPalette.ColorRole.Light, _mk_q_color("{{ border|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Midlight, _mk_q_color("{{ border|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Dark, _mk_q_color("{{ background|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Mid, _mk_q_color("{{ border|color|palette }}"))
        palette.setColor(QPalette.ColorRole.Shadow, _mk_q_color("{{ border|color|palette }}"))

        # disabled
        palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.WindowText,
            _mk_q_color('{{ foreground|color(state="disabled")|palette }}'),
        )
        palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.ButtonText,
            _mk_q_color('{{ foreground|color(state="disabled")|palette }}'),
        )
        palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.Highlight,
            _mk_q_color('{{ foreground|color(state="disabledSelectionBackground")|palette }}'),
        )
        palette.setColor(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.HighlightedText,
            _mk_q_color('{{ foreground|color(state="disabled")|palette }}'),
        )

        # inactive
        palette.setColor(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.Highlight,
            _mk_q_color('{{ primary|color(state="list.inactiveSelectionBackground")|palette }}'),
        )
        palette.setColor(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.HighlightedText,
            _mk_q_color("{{ foreground|color|palette }}"),
        )

    palette.setColor(
        QPalette.ColorRole.Text, _mk_q_color('{{ foreground|color(state="icon")|palette }}')
    )
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.Text,
        _mk_q_color('{{ foreground|color(state="disabled")|palette }}'),
    )
    palette.setColor(QPalette.ColorRole.Link, _mk_q_color("{{ primary|color|palette }}"))
    palette.setColor(QPalette.ColorRole.LinkVisited, _mk_q_color("{{ linkVisited|color|palette }}"))
    if hasattr(QPalette.ColorRole, "PlaceholderText"):
        palette.setColor(
            QPalette.ColorRole.PlaceholderText,
            _mk_q_color('{{ foreground|color(state="input.placeholder")|palette }}'),
        )

    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.Link,
        _mk_q_color('{{ foreground|color(state="disabledSelectionBackground")|palette }}'),
    )
    palette.setColor(
        QPalette.ColorGroup.Disabled,
        QPalette.ColorRole.LinkVisited,
        _mk_q_color('{{ foreground|color(state="disabled")|palette }}'),
    )

    return palette
