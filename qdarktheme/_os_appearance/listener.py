from __future__ import annotations

import darkdetect

from qdarktheme import _os_appearance
from qdarktheme.qtpy.QtCore import QCoreApplication, QEvent, QObject, QThread, Signal


class OSThemeSwitchListener(QThread):
    """Listener to detect to change OS's theme."""

    sig_run = Signal(bool)
    _sig_listen_os_theme = Signal()

    def __init__(self, callable) -> None:
        """Initialize listener."""
        super().__init__()
        self.setProperty("is_running", True)
        self._theme = darkdetect.theme()
        self._accent = _os_appearance.accent()
        self.sig_run.connect(lambda state: self.setProperty("is_running", state))
        self._sig_listen_os_theme.connect(callable)

    def eventFilter(self, q_object: QObject, event: QEvent) -> bool:  # noqa: N802
        """Override QObject.eventFilter.

        This override is for Mac.
        Qt can listen to change OS's theme on only mac and changed QPalette automatically.
        So enable to listen to change OS's theme via palette change event.
        """
        if (
            self.property("is_running")
            and q_object == QCoreApplication.instance()
            and event.type() == QEvent.Type.ApplicationPaletteChange
        ):
            accent = _os_appearance.accent()
            theme = darkdetect.theme()
            if self._theme != theme or self._accent != accent:
                self._theme = theme
                self._accent = accent
                self._sig_listen_os_theme.emit()
                return True
        return super().eventFilter(q_object, event)

    def run(self) -> None:
        """Override QThread.run.

        This override is for except Mac.
        Qt cannot listen to change OS's theme on except Mac.
        Use ``darkdetect.listener`` to detect to change OS's theme.
        """
        darkdetect.listener(
            lambda theme: self.property("is_running") and self._sig_listen_os_theme.emit()
        )

    def kill(self) -> None:
        """Kill thread."""
        self.terminate()
        self.deleteLater()
