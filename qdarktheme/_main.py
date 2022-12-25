from __future__ import annotations

import atexit
import os
import platform

import darkdetect

from qdarktheme._style_loader import load_palette, load_stylesheet

_listener = None
_proxy_style = None


def _apply_style(app, additional_qss: str | None, **kargs) -> None:
    from qdarktheme._proxy_style import QDarkThemeStyle

    stylesheet = load_stylesheet(**kargs)
    if additional_qss is not None:
        stylesheet += additional_qss
    app.setStyleSheet(stylesheet)

    app.setPalette(
        load_palette(
            kargs["theme"],
            kargs["custom_colors"],
            for_stylesheet=True,
            default_theme=kargs["default_theme"],
        )
    )

    global _proxy_style
    if _proxy_style is None:
        _proxy_style = QDarkThemeStyle()
        app.setStyle(_proxy_style)


def _sync_theme_with_system(app, callback) -> None:
    from qdarktheme._os_appearance import listener

    global _listener
    if _listener is not None:
        _listener.sig_run.emit(True)
        return

    _listener = listener.OSThemeSwitchListener(callback)

    if platform.system() == "Darwin":
        app.installEventFilter(_listener)
    else:
        atexit.register(_listener.kill)
        _listener.start()


def enable_hi_dpi() -> None:
    """Allow to HiDPI.

    This function must be set before instantiation of QApplication..
    For Qt6 bindings, HiDPI “just works” without using this function.
    """
    from qdarktheme.qtpy.QtCore import Qt
    from qdarktheme.qtpy.QtGui import QGuiApplication

    if hasattr(Qt.ApplicationAttribute, "AA_UseHighDpiPixmaps"):
        QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)  # type: ignore
    if hasattr(Qt.ApplicationAttribute, "AA_EnableHighDpiScaling"):
        QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)  # type: ignore
    if hasattr(Qt, "HighDpiScaleFactorRoundingPolicy"):
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )


def stop_sync() -> None:
    """Stop sync with system theme."""
    from qdarktheme.qtpy.QtCore import QCoreApplication

    app = QCoreApplication.instance()
    global _listener
    if not app or not _listener:
        return
    _listener.sig_run.emit(False)


def setup_theme(
    theme: str = "dark",
    corner_shape: str = "rounded",
    custom_colors: dict[str, str | dict[str, str]] | None = None,
    additional_qss: str | None = None,
    *,
    default_theme: str = "dark",
) -> None:
    """Apply the theme which looks like flat design to the Qt App completely.

    This function applies the complete style to your Qt application. If the argument theme is ``auto``,
    try to listen to changes to the OS's theme and switch the application theme accordingly.

    Args:
        theme: The theme name. There are `dark`, `light` and `auto`.
            If ``auto``, try to sync with your OS's theme and accent (accent is only on Mac).
            If failed to detect OS's theme, use the default theme set in argument ``default_theme``.
            When primary color(``primary``) or primary child colors
            (such as ``primary>selection.background``) are set to custom_colors,
            disable to sync with the accent.
        corner_shape: The corner shape. There are `rounded` and `sharp` shape.
        custom_colors: The custom color map. Overrides the default color for color id you set.
            Also you can customize a specific theme only. See example 5.
        additional_qss: Additional stylesheet text. You can add your original stylesheet text.
        default_theme: The default theme name.
            The theme set by this argument will be used when system theme detection fails.

    Raises:
        ValueError: If the argument is wrong.
        KeyError: If the color id of custom_colors is wrong.

    Returns:
        The stylesheet string for the given arguments.

    Examples:
        Set stylesheet to your Qt application.

        1. Setup style and sync to system theme ::

            app = QApplication([])
            qdarktheme.setup_theme()

        2. Use Dark Theme ::

            app = QApplication([])
            qdarktheme.setup_theme("dark")

        3. Sharp corner ::

            # Change corner shape to sharp.
            app = QApplication([])
            qdarktheme.setup_theme(corner_shape="sharp")

        4. Customize color ::

            app = QApplication([])
            qdarktheme.setup_theme(custom_colors={"primary": "#D0BCFF"})

        5. Customize a specific theme only ::

            app = QApplication([])
            qdarktheme.setup_theme(
                theme="auto",
                custom_colors={
                    "[dark]": {
                        "primary": "#D0BCFF",
                    }
                },
            )
    """
    from qdarktheme.qtpy.QtCore import QCoreApplication

    app = QCoreApplication.instance()
    if not app:
        raise Exception("setup_theme() must be called after instantiation of QApplication.")
    if theme != "auto":
        stop_sync()
    app.setProperty("_qdarktheme_use_setup_style", True)

    def callback():
        _apply_style(
            app,
            additional_qss,
            theme=theme,
            corner_shape=corner_shape,
            custom_colors=custom_colors,
            default_theme=default_theme,
        )

    callback()

    if theme == "auto" and darkdetect.theme() is not None:
        _sync_theme_with_system(app, callback)
