from __future__ import annotations

import atexit
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
    from qdarktheme.qtpy.QtCore import QEvent, QObject, Signal

    class ThemeEventFilter(QObject):
        sig_run = Signal(bool)

        def __init__(self) -> None:
            super().__init__()
            self.setProperty("is_running", True)
            self._theme = darkdetect.theme()
            self.sig_run.connect(lambda state: self.setProperty("is_running", state))

        def eventFilter(self, q_object: QObject, event: QEvent) -> bool:  # noqa: N802
            if (
                self.property("is_running")
                and q_object == app
                and event.type() == QEvent.Type.ApplicationPaletteChange
            ):
                theme = darkdetect.theme()
                if self._theme != theme:
                    self._theme = theme
                    _apply_style(app, *args, **kargs)
                    return True
            return super().eventFilter(q_object, event)

    return ThemeEventFilter()


def _create_theme_listener(app, *args, **kargs):
    from qdarktheme.qtpy.QtCore import QThread, Signal

    class ThemeListener(QThread):
        sig_run = Signal(bool)
        _sig_listen_os_theme = Signal(str)

        def __init__(self) -> None:
            super().__init__()
            self.setProperty("is_running", True)
            self.sig_run.connect(lambda state: self.setProperty("is_running", state))
            self._sig_listen_os_theme.connect(
                lambda _: self.property("is_running") and _apply_style(app, *args, **kargs)
            )

        def run(self) -> None:
            darkdetect.listener(self._sig_listen_os_theme.emit)

        def kill(self) -> None:
            self.terminate()
            self.deleteLater()

    listener = ThemeListener()
    atexit.register(listener.kill)

    return listener


def _sync_theme_with_system(app, *args, **kargs) -> None:
    global _listener
    if _listener is not None:
        _listener.sig_run.emit(True)
        return

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
    from qdarktheme.qtpy.QtWidgets import QApplication

    app: QApplication | None = QApplication.instance()
    global _listener
    if not app or not _listener:
        return
    _listener.sig_run.emit(False)


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
    if theme != "auto":
        stop_sync()

    _apply_style(app, additional_qss, theme, corner_shape, custom_colors, default_theme=default_theme)

    if theme == "auto" and darkdetect.theme() is not None:
        _sync_theme_with_system(
            app, additional_qss, theme, corner_shape, custom_colors, default_theme=default_theme
        )
