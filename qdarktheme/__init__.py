# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

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
    from importlib import resources

    from qdarktheme.compile import compile_stylesheet

    if theme not in ["dark", "light"]:
        raise TypeError("The argument [mode] can only be specified as 'dark' or 'light'.") from None

    with resources.path("qdarktheme", "template.qss") as stylesheet_file:
        with resources.path("qdarktheme.theme", f"{theme}.json") as theme_colormap_file:
            return compile_stylesheet(stylesheet_file, theme_colormap_file)
