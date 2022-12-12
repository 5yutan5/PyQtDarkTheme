"""Icon map that overrides standard icons."""
from qdarktheme.qtpy.QtWidgets import QStyle

NEW_STANDARD_ICON_MAP = {
    QStyle.StandardPixmap.SP_ArrowBack: {"id": "arrow_upward", "rotate": 270},
    QStyle.StandardPixmap.SP_ArrowDown: {"id": "arrow_upward", "rotate": 180},
    QStyle.StandardPixmap.SP_ArrowForward: {"id": "arrow_upward", "rotate": 90},
    QStyle.StandardPixmap.SP_ArrowLeft: {"id": "arrow_upward", "rotate": 270},
    QStyle.StandardPixmap.SP_ArrowRight: {"id": "arrow_upward", "rotate": 90},
    QStyle.StandardPixmap.SP_ArrowUp: {"id": "arrow_upward"},
    QStyle.StandardPixmap.SP_BrowserReload: {"id": "refresh"},
    QStyle.StandardPixmap.SP_BrowserStop: {"id": "close"},
    QStyle.StandardPixmap.SP_CommandLink: {"id": "east"},
    QStyle.StandardPixmap.SP_DialogApplyButton: {"id": "check_circle"},
    QStyle.StandardPixmap.SP_DialogCancelButton: {"id": "cancel"},
    QStyle.StandardPixmap.SP_DialogCloseButton: {"id": "close"},
    QStyle.StandardPixmap.SP_DialogDiscardButton: {"id": "delete"},
    QStyle.StandardPixmap.SP_DialogHelpButton: {"id": "help"},
    QStyle.StandardPixmap.SP_DialogNoButton: {"id": "not_interested"},
    QStyle.StandardPixmap.SP_DialogOkButton: {"id": "check"},
    QStyle.StandardPixmap.SP_DialogOpenButton: {"id": "launch"},
    QStyle.StandardPixmap.SP_DialogResetButton: {"id": "cleaning_services"},
    QStyle.StandardPixmap.SP_DialogSaveButton: {"id": "save"},
    QStyle.StandardPixmap.SP_DialogYesButton: {"id": "circle"},
    QStyle.StandardPixmap.SP_DirHomeIcon: {"id": "home"},
    QStyle.StandardPixmap.SP_DockWidgetCloseButton: {"id": "close"},
    QStyle.StandardPixmap.SP_FileDialogBack: {"id": "arrow_upward", "rotate": 270},
    QStyle.StandardPixmap.SP_FileDialogContentsView: {"id": "search"},
    QStyle.StandardPixmap.SP_FileDialogDetailedView: {"id": "list"},
    QStyle.StandardPixmap.SP_FileDialogEnd: {"id": "drive_file_move_rtl"},
    QStyle.StandardPixmap.SP_FileDialogInfoView: {"id": "info"},
    QStyle.StandardPixmap.SP_FileDialogListView: {"id": "grid_view"},
    QStyle.StandardPixmap.SP_FileDialogNewFolder: {"id": "create_new_folder"},
    QStyle.StandardPixmap.SP_FileDialogStart: {"id": "drive_file_move"},
    QStyle.StandardPixmap.SP_FileDialogToParent: {"id": "arrow_upward"},
    QStyle.StandardPixmap.SP_MediaPause: {"id": "pause"},
    QStyle.StandardPixmap.SP_MediaPlay: {"id": "play_arrow"},
    QStyle.StandardPixmap.SP_MediaSeekBackward: {"id": "fast_rewind"},
    QStyle.StandardPixmap.SP_MediaSeekForward: {"id": "fast_forward"},
    QStyle.StandardPixmap.SP_MediaSkipBackward: {"id": "skip_previous"},
    QStyle.StandardPixmap.SP_MediaSkipForward: {"id": "skip_next"},
    QStyle.StandardPixmap.SP_MediaStop: {"id": "stop"},
    QStyle.StandardPixmap.SP_MediaVolume: {"id": "volume_up"},
    QStyle.StandardPixmap.SP_MediaVolumeMuted: {"id": "volume_mute"},
    QStyle.StandardPixmap.SP_MessageBoxQuestion: {"id": "help", "os": ["Darwin", "Linux"]},
    QStyle.StandardPixmap.SP_TitleBarCloseButton: {"id": "close"},
    QStyle.StandardPixmap.SP_TitleBarContextHelpButton: {"id": "question_mark"},
    QStyle.StandardPixmap.SP_TitleBarMaxButton: {"id": "fullscreen"},
    QStyle.StandardPixmap.SP_TitleBarMinButton: {"id": "minimize"},
    QStyle.StandardPixmap.SP_TitleBarNormalButton: {"id": "flip_to_front"},
    QStyle.StandardPixmap.SP_TitleBarShadeButton: {"id": "chevron_right", "rotate": "270"},
    QStyle.StandardPixmap.SP_TitleBarUnshadeButton: {"id": "chevron_right", "rotate": "90"},
    QStyle.StandardPixmap.SP_ToolBarHorizontalExtensionButton: {"id": "double_arrow"},
    QStyle.StandardPixmap.SP_ToolBarVerticalExtensionButton: {"id": "double_arrow", "rotate": 90},
    QStyle.StandardPixmap.SP_TrashIcon: {"id": "delete", "os": ["Windows"]},
    QStyle.StandardPixmap.SP_VistaShield: {"id": "security", "os": ["Darwin", "Linux"]},
}

if hasattr(QStyle.StandardPixmap, "SP_DialogAbortButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogAbortButton] = {"id": "not_interested"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_DialogIgnoreButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogIgnoreButton] = {"id": "visibility_off"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_DialogNoToAllButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogNoToAllButton] = {"id": "close"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_DialogRetryButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogRetryButton] = {"id": "refresh"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_DialogSaveAllButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogSaveAllButton] = {"id": "save"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_DialogYesToAllButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_DialogYesToAllButton] = {"id": "done_all"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_LineEditClearButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_LineEditClearButton] = {"id": "close"}  # type: ignore  # noqa: E501

if hasattr(QStyle.StandardPixmap, "SP_TabCloseButton"):
    NEW_STANDARD_ICON_MAP[QStyle.StandardPixmap.SP_TabCloseButton] = {"id": "close"}  # type: ignore  # noqa: E501
