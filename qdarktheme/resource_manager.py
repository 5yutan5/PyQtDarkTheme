try:
    from typing import Literal
except ImportError:  # Python 3.7 requires typing-extensions.
    from typing_extensions import Literal

import qdarktheme
from qdarktheme.compile import compile_stylesheet
from qdarktheme.Qt.QtCore import QDir
from qdarktheme.Qt.QtGui import QIcon
from qdarktheme.util import get_qdarktheme_root_path


def load_stylesheet(theme: Literal["dark", "light"] = "dark") -> str:
    """Load the style sheet which looks like flat design. There are two themes, dark theme and light theme.


    Parameters
    ----------
    theme : str
        String of theme name. Only `dark` and `light` can be specified., by default dark

    Returns
    -------
    str
        The style sheet string.

    Raises
    ------
    TypeError
        If argument [mode] is not `dark` or `light`.
    FileNotFoundError
        If the qss file fails to load.
    """
    if theme not in ["dark", "light"]:
        raise TypeError(
            "\n==============================================================="
            "\nThe argument [mode] can only be specified as 'dark' or 'light'."
            "\n==============================================================="
        )

    root_path = get_qdarktheme_root_path()

    # Add icon folder path to search path for style sheet.
    QDir.addSearchPath(qdarktheme.__name__, str(root_path))

    stylesheet_file = root_path / "template.qss"
    theme_colormap_file = root_path / "theme" / f"{theme}.json"
    return compile_stylesheet(stylesheet_file, theme_colormap_file)


def get_icon(
    icon_name: Literal[
        "clear",
        "circle",
        "copy_all",
        "dark_mode",
        "favorite_border",
        "flip_to_front",
        "folder_open",
        "home",
        "light_mode",
        "palette",
        "settings",
    ]
) -> QIcon:
    """Creates an icon from the given icon name. See below folder(`qdarktheme/svg/example`) for details on
    available icons.

    Parameters
    ----------
    icon_name : str
        Available icon name.

    Returns
    -------
    QIcon
        QIcon object with the given icon name.
    """

    icon_folder = get_qdarktheme_root_path() / "svg" / "example"
    icon_path = icon_folder / f"{icon_name}_24dp.svg"
    return QIcon(str(icon_path))
