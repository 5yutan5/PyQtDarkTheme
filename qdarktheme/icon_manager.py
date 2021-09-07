from importlib import resources

from qdarktheme.qtpy.QtGui import QIcon


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
