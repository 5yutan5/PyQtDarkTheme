from importlib import resources

from qdarktheme.compile import compile_stylesheet
from qdarktheme.qtpy.QtGui import QIcon


def load_stylesheet(theme: str = "dark") -> str:
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
        raise TypeError("The argument [mode] can only be specified as 'dark' or 'light'.")

    with resources.path("qdarktheme", "template.qss") as stylesheet_file:
        with resources.path("qdarktheme.theme", f"{theme}.json") as theme_colormap_file:
            return compile_stylesheet(stylesheet_file, theme_colormap_file)


def get_icon(icon_name: str) -> QIcon:
    """Creates an icon from `qdarktheme/svg/example`. See below folder(`qdarktheme/svg/example`) for details on
    available icons.

    Parameters
    ----------
    icon_name : str
        Available icon name: "clear", "circle", "copy_all", "dark_mode", "favorite_border", "flip_to_front",
        "folder_open", "home", "light_mode", "palette", "settings",

    Returns
    -------
    QIcon
        QIcon object with the given icon name.
    """
    with resources.path("qdarktheme.svg.example", f"{icon_name}_24dp.svg") as icon_path:
        return QIcon(str(icon_path))
