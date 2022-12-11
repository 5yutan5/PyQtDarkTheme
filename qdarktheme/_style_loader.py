"""Module for loading style data for Qt."""
from __future__ import annotations

import json
import shutil
import warnings
from functools import partial

from qdarktheme import __version__, _resources
from qdarktheme._template import filter
from qdarktheme._template.engine import Template
from qdarktheme._util import get_cash_root_path, get_logger

_logger = get_logger(__name__)


def _detect_system_theme(default_theme: str) -> str:
    import darkdetect

    system_theme = darkdetect.theme()
    if system_theme is None:
        _logger.info(f'failed to detect system theme, qdarktheme use "{default_theme}" theme.')
        return default_theme
    return system_theme.lower()


def _color_values(theme: str) -> dict[str, str | dict]:
    try:
        return json.loads(_resources.COLOR_VALUES[theme])
    except KeyError:
        raise ValueError(f'invalid argument, not a dark or light: "{theme}"') from None


def _mix_theme_colors(custom_colors: dict[str, str | dict[str, str]], theme: str) -> dict[str, str]:
    colors = {id: color for id, color in custom_colors.items() if isinstance(color, str)}
    custom_colors_with_theme = custom_colors.get(f"[{theme}]")
    if isinstance(custom_colors_with_theme, dict):
        colors.update(custom_colors_with_theme)
    elif isinstance(custom_colors_with_theme, str):
        raise ValueError(
            "invalid value for argument custom_colors, not a dict type: "
            f'"{custom_colors_with_theme}" of "[{theme}]" key.'
        )
    return colors


def _marge_colors(
    color_values: dict[str, str | dict], custom_colors: dict[str, str | dict[str, str]], theme: str
):
    for color_id, color in _mix_theme_colors(custom_colors, theme).items():
        try:
            parent_key, *child_keys = color_id.split(">")
            color_value = color_values[parent_key]
            if len(child_keys) > 1 or (isinstance(color_value, str) and len(child_keys) != 0):
                raise KeyError

            if isinstance(color_value, str):
                color_values[parent_key] = color
            else:
                child_key = "base" if len(child_keys) == 0 else child_keys[0]
                color_value[child_key]  # Check if child_key exists.
                color_value[child_key] = color
        except KeyError:
            raise KeyError(f'invalid color id for argument custom_colors: "{color_id}".') from None


def load_stylesheet(
    theme: str = "dark",
    corner_shape: str = "rounded",
    custom_colors: dict[str, str | dict[str, str]] | None = None,
    *,
    default_theme: str = "dark",
    border: str | None = None,
) -> str:
    """Load the style sheet which looks like flat design. There are `dark` and `light` theme.

    Args:
        theme: The theme name. There are `dark`, `light` and `auto`.
            If ``auto``, try to detect system theme.
            If failed to detect system theme,
            use the theme set in argument ``default_theme``.
        corner_shape: The corner shape. There are `rounded` and `sharp` shape.
        custom_colors: The custom color map. Overrides the default color for color id you set.
            Also you can customize a specific theme only. See example 6.
        default_theme: The default theme name.
            The theme set by this argument will be used when system theme detection fails.
        border: The corner shape. There are `rounded` and `sharp` shape.
            This argument is deprecated since v1.2.0. Please use `corner_shape` instead.
            This argument override value of argument `corner_shape`.

    Raises:
        ValueError: If the arguments of this method is wrong.
        KeyError: If the color id of custom_colors is wrong.

    Returns:
        The stylesheet string for the given arguments.

    Examples:
        Set stylesheet to your Qt application.

        1. Dark Theme ::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet())
            # or
            app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

        2. Light Theme ::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet("light"))

        3. Automatic detection of system theme ::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet("auto"))

        4. Sharp corner ::

            # Change corner shape to sharp.
            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet(corner_shape="sharp"))

        5. Customize color ::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))

        6. Customize a specific theme only ::

            app = QApplication([])
            app.setStyleSheet(
                qdarktheme.load_stylesheet(
                    theme="auto",
                    custom_colors={
                        "[dark]": {
                            "primary": "#D0BCFF",
                        }
                    },
                )
            )
    """
    if theme == "auto":
        theme = _detect_system_theme(default_theme)
    color_values = _color_values(theme)
    if corner_shape not in ("rounded", "sharp"):
        raise ValueError(f'invalid argument, not a rounded or sharp: "{corner_shape}"')
    if border not in (None, "rounded", "sharp"):
        raise ValueError(f'invalid argument, not a rounded or sharp: "{border}"')
    if border is not None:
        warnings.warn(
            'deprecated argument, "border" is deprecated since v2.0.0. '
            'Please use "corner_shape" instead.',
            FutureWarning,
        )
        corner_shape = border

    if custom_colors is not None:
        _marge_colors(color_values, custom_colors, theme)

    get_cash_root_path(__version__).mkdir(parents=True, exist_ok=True)

    # Build stylesheet
    template = Template(
        _resources.TEMPLATE_STYLESHEET,
        {"color": filter.color, "corner": filter.corner, "env": filter.env, "url": filter.url},
    )
    replacements = dict(color_values, **{"corner-shape": corner_shape})
    return template.render(replacements)


def clear_cache() -> None:
    """Clear the caches in system home path.

    PyQtDarkTheme build the caches of resources in the system home path.
    You can clear the caches by running this method.
    """
    try:
        cache_path = get_cash_root_path(__version__)
        shutil.rmtree(cache_path)
        _logger.info(f"The caches({cache_path}) has been deleted")
    except FileNotFoundError:
        _logger.info("There is no caches")


def load_palette(
    theme: str = "dark",
    custom_colors: dict[str, str | dict[str, str]] | None = None,
    *,
    default_theme: str = "dark",
    for_stylesheet: bool = False,
):
    """Load the QPalette for the dark or light theme.

    Args:
        theme: The theme name. There are `dark`, `light` and `auto`.
            If ``auto``, try to detect system theme.
            If failed to detect system theme,
            use the theme set in argument ``default_theme``.
        custom_colors: The custom color map. Overrides the default color for color id you set.
            Also you can customize a specific theme only. See example 5.
        default_theme: The default theme name.
            The theme set by this argument will be used when system theme detection fails.
        for_stylesheet: If True, only includes colors that cannot be set in stylesheets, such as
            ``link`` and ``placeholder``.

    Raises:
        TypeError: If the arg name of theme is wrong.
        KeyError: If the color id of custom_colors is wrong.

    Returns:
        QPalette: The QPalette for the given theme.

    Examples:
        Set QPalette to your Qt application.

        1. Dark Theme ::

            app = QApplication([])
            app.setPalette(qdarktheme.load_palette())
            # or
            app.setPalette(qdarktheme.load_palette("dark"))

        2. Light Theme ::

            app = QApplication([])
            app.setPalette(qdarktheme.load_palette("light"))

        3. Automatic detection of system theme ::

            app = QApplication([])
            app.setPalette(qdarktheme.load_palette("auto"))

        4. Customize color ::

            app = QApplication([])
            app.setPalette(custom_colors={"primary": "#D0BCFF"})

        5. Customize a specific theme only ::

            app = QApplication([])
            app.setStyleSheet(
                qdarktheme.load_stylesheet(
                    theme="auto",
                    custom_colors={
                        "[dark]": {
                            "primary": "#D0BCFF",
                        }
                    },
                )
            )
    """
    if theme == "auto":
        theme = _detect_system_theme(default_theme)
    color_values = _color_values(theme)
    if custom_colors is not None:
        _marge_colors(color_values, custom_colors, theme)

    mk_template = partial(Template, filters={"color": filter.color, "palette": filter.palette_format})
    return _resources.mk_q_palette(mk_template, color_values, for_stylesheet)


def get_themes() -> tuple[str, ...]:
    """Return available theme names.

    Returns:
        Tuple of available theme names.
    """
    return _resources.THEMES
