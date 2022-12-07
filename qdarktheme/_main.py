from __future__ import annotations

import os
import platform

import darkdetect

from qdarktheme._style_loader import load_palette, load_stylesheet

_listener = None


def _apply_style(app, additional_qss: str | None, *args, **kargs) -> None:
    stylesheet = load_stylesheet(*args, **kargs)
    if additional_qss is not None:
        stylesheet += additional_qss
    app.setStyleSheet(stylesheet)

    app.setPalette(load_palette(args[0], args[2], for_stylesheet=True, **kargs))


def _create_theme_event_filter(app, *args, **kargs):
    from qdarktheme.qtpy.QtCore import QEvent, QObject

    class ThemeEventFilter(QObject):
        _theme = None

        def eventFilter(self, q_object: QObject, event: QEvent) -> bool:  # noqa: N802
            if q_object != app:
                return super().eventFilter(q_object, event)
            theme = darkdetect.theme()
            if event.type() == QEvent.Type.ApplicationPaletteChange and self._theme != theme:
                self._theme = theme
                _apply_style(app, *args, **kargs)
                return True
            return False

    return ThemeEventFilter()


def _create_theme_listener(app, *args, **kargs):
    from qdarktheme.qtpy.QtCore import QThread, Signal

    class ThemeListener(QThread):
        sig_change_theme = Signal(str)

        def __init__(self) -> None:
            super().__init__()
            self.sig_change_theme.connect(lambda _: _apply_style(app, *args, **kargs))

        def run(self) -> None:
            darkdetect.listener(self.sig_change_theme.emit)

    return ThemeListener()


def _sync_theme_with_system(app, *args, **kargs) -> None:
    global _listener
    if platform.system() == "Darwin":
        _listener = _create_theme_event_filter(app, *args, **kargs)
        app.installEventFilter(_listener)
    else:
        _listener = _create_theme_listener(app, *args, **kargs)
        _listener.start()


def _enable_hi_dpi(app) -> None:
    from qdarktheme.qtpy.QtCore import Qt

    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore
    if hasattr(Qt.ApplicationAttribute, "AA_EnableHighDpiScaling"):
        app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)  # type: ignore
    if hasattr(Qt, "HighDpiScaleFactorRoundingPolicy"):
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
        app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


def stop_sync() -> None:
    """Stop sync with system theme."""
    from qdarktheme.qtpy.QtCore import QThread
    from qdarktheme.qtpy.QtWidgets import QApplication

    app: QApplication | None = QApplication.instance()
    global _listener
    if not app or not _listener:
        return

    if isinstance(_listener, QThread):
        _listener.terminate()
        _listener.deleteLater()
    else:
        app.removeEventFilter(_listener)
        _listener.deleteLater()
    _listener = None


def setup_style(
    theme: str = "auto",
    corner_shape: str = "rounded",
    custom_colors: dict[str, str | dict[str, str]] | None = None,
    additional_qss: str | None = None,
    *,
    default_theme: str = "dark",
    high_dpi: bool = True,
) -> None:
    """Apply the style which looks like flat design to the Qt App completely.

    This function doesn't only set the Qt stylesheet,
    it applies the complete style to your Qt application using QPalette etc.
    Also if theme is ``auto``, try to listen to changes to the OS's color scheme and switch to a
    matching theme accordingly.

    Args:
        theme: The theme name. There are `dark`, `light` and `auto`.
            If ``auto``, try to sync with system theme.
            If failed to detect system theme,
            use the theme set in argument ``default_theme``.
        corner_shape: The corner shape. There are `rounded` and `sharp` shape.
        custom_colors: The custom color map. Overrides the default color for color id you set.
            Also you can customize a specific theme only. See example 5.
        additional_qss: Additional stylesheet text. You can add your original stylesheet text.
        default_theme: The default theme name.
            The theme set by this argument will be used when system theme detection fails.
        high_dpi: If ``True``, enable HiDPI.
            For Qt6 bindings, this functionally “just works” without having to set ``True``.


    Raises:
        ValueError: If the argument is wrong.
        KeyError: If the color id of custom_colors is wrong.

    Returns:
        The stylesheet string for the given arguments.

    Examples:
        Set stylesheet to your Qt application.

        1. Setup style and sync to system theme ::

            app = QApplication([])
            qdarktheme.setup_style()

        2. Use Dark Theme ::

            app = QApplication([])
            qdarktheme.setup_style("dark")

        3. Sharp corner ::

            # Change corner shape to sharp.
            app = QApplication([])
            qdarktheme.setup_style(corner_shape="sharp")

        4. Customize color ::

            app = QApplication([])
            qdarktheme.setup_style(custom_colors={"primary": "#D0BCFF"})

        5. Customize a specific theme only ::

            app = QApplication([])
            qdarktheme.setup_style(
                theme="auto",
                custom_colors={
                    "[dark]": {
                        "primary": "#D0BCFF",
                    }
                },
            )
    """
    from qdarktheme.qtpy.QtWidgets import QApplication

    app: QApplication | None = QApplication.instance()
    if not app:
        raise Exception("setup_style() must be called after instantiation of QApplication.")
    if high_dpi:
        _enable_hi_dpi(app)
    if theme != "auto" or _listener is not None:
        stop_sync()

    _apply_style(app, additional_qss, theme, corner_shape, custom_colors, default_theme=default_theme)

    if theme == "auto":
        _sync_theme_with_system(
            app, additional_qss, theme, corner_shape, custom_colors, default_theme=default_theme
        )
