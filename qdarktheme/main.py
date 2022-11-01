"""Main file of qdarktheme."""
from __future__ import annotations

import json
import shutil
import warnings
from functools import partial

from qdarktheme import __version__, filter, resources
from qdarktheme.color import Color
from qdarktheme.template_engine import Template
from qdarktheme.util import get_cash_root_path, get_logger

_logger = get_logger(__name__)


def _color_schema(theme: str) -> dict[str, str | dict]:
    try:
        return json.loads(resources.COLOR_SCHEMAS[theme])
    except KeyError:
        raise ValueError(f'invalid argument, not a dark or light: "{theme}"') from None


def _marge_colors(color_schema: dict[str, str | dict], custom_colors: dict[str, str]):
    for color_id, color_format in custom_colors.items():
        if not Color.check_hex_format(color_format):
            raise ValueError(
                f'invalid value for argument custom_colors: "{color_format}". '
                "Only support following hexadecimal notations: #RGB, #RGBA, #RRGGBB and #RRGGBBAA. "
                "R (red), G (green), B (blue), and A (alpha) are hexadecimal characters "
                "(0-9, a-f or A-F)."
            ) from None

        parent_key, *child_key = color_id.split(">")
        try:
            color_info = color_schema[parent_key]
            if len(child_key) == 0:
                if isinstance(color_info, str):
                    color_schema[parent_key] = color_format
                else:
                    color_info["base"] = color_format
            elif len(child_key) == 1:
                color_info = color_schema[parent_key]
                if isinstance(color_info, dict):
                    # Check if child_key is valid.
                    color_info[child_key[0]]
                    color_info[child_key[0]] = color_format
            else:
                raise KeyError
        except KeyError:
            raise KeyError(f'invalid color id for argument custom_colors: "{color_id}".') from None


def load_stylesheet(
    theme: str = "dark",
    corner_shape: str = "rounded",
    custom_colors: dict[str, str] | None = None,
    *,
    border: str | None = None,
) -> str:
    """Load the style sheet which looks like flat design. There are `dark` and `light` theme.

    Args:
        theme: The name of the theme. There are `dark` and `light` theme.
        corner_shape: The corner shape. There are `rounded` and `sharp` shape.
        custom_colors: The custom color map. Overrides the default color for color id you set.
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

        3. Sharp corner ::

            # Change corner shape to sharp.
            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet(corner_shape="sharp"))

        4. Customize color ::

            app = QApplication([])
            app.setStyleSheet(qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"}))
    """
    color_schema = _color_schema(theme)
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

    get_cash_root_path(__version__).mkdir(parents=True, exist_ok=True)

    if custom_colors is not None:
        _marge_colors(color_schema, custom_colors)

    # Build stylesheet
    template = Template(
        resources.TEMPLATE_STYLESHEET,
        {"color": filter.color, "corner": filter.corner, "env": filter.env, "url": filter.url},
    )
    replacements = dict(color_schema, **{"corner-shape": corner_shape})
    return template.render(replacements)


def clear_cache() -> None:
    """Clear the caches in system home path.

    PyQtDarkTheme build the caches of resources in the system home path.
    You can clear the caches by running this method.
    """
    try:
        shutil.rmtree(get_cash_root_path(__version__))
        _logger.info(f"The caches({get_cash_root_path(__version__)}) has been deleted")
    except FileNotFoundError:
        _logger.info("There is no caches")


def load_palette(theme: str = "dark", custom_colors: dict[str, str] | None = None):
    """Load the QPalette for the dark or light theme.

    Args:
        theme: The name of the theme. Available theme are `dark` and `light`.
        custom_colors: The custom color map. Overrides the default color for color id you set.

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

        3. Customize color ::

            app = QApplication([])
            app.setPalette(custom_colors={"primary": "#D0BCFF"})
    """
    color_schema = _color_schema(theme)
    if custom_colors is not None:
        _marge_colors(color_schema, custom_colors)

    mk_template = partial(Template, filters={"color": filter.color, "palette": filter.palette_format})
    return resources.mk_q_palette(mk_template, color_schema)


def get_themes() -> tuple[str, ...]:
    """Return available theme names.

    Returns:
        Tuple of available theme names.
    """
    return resources.THEMES
