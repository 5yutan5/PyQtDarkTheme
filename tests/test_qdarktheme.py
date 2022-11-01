"""Tests for the main program."""
import re

import pytest

import qdarktheme


@pytest.mark.parametrize(
    ("theme", "corner_shape", "custom_colors"),
    [
        # Test theme and corner_shape
        ("dark", "rounded", None),
        ("dark", "sharp", None),
        # Test theme, corner_shape and custom_colors
        ("dark", "rounded", {}),
        ("dark", "rounded", {"foreground": "#112233"}),
        ("dark", "sharp", {"foreground": "#112233"}),
        ("dark", "rounded", {"foreground>icon": "#112233"}),
        ("dark", "rounded", {"input.background": "#112233"}),
        # Test color code
        ("dark", "rounded", {"foreground": "#112"}),
        ("dark", "rounded", {"foreground": "#11223344"}),
        ("dark", "rounded", {"foreground": "#1122"}),
    ],
)
def test_load_stylesheet(theme, corner_shape, custom_colors) -> None:
    """Verify that the function `load_stylesheet()` runs successfully when using various arguments."""
    qdarktheme.load_stylesheet(theme, corner_shape, custom_colors)


def test_load_stylesheet_with_border() -> None:
    """Verify that the function `load_stylesheet()` runs successfully when using border arguments."""
    qdarktheme.load_stylesheet(border="sharp")


def test_load_stylesheet_with_wrong_theme() -> None:
    """Verify we raise ValueError when using wrong theme name."""
    with pytest.raises(ValueError, match='invalid argument, not a dark or light: "wrong_value"'):
        qdarktheme.load_stylesheet("wrong_value")


def test_load_stylesheet_with_wrong_corner_shape() -> None:
    """Verify we raise ValueError when using wrong corner shape name."""
    with pytest.raises(ValueError, match='invalid argument, not a rounded or sharp: "wrong_value"'):
        qdarktheme.load_stylesheet(corner_shape="wrong_value")


def test_load_stylesheet_with_wrong_border() -> None:
    """Verify we raise ValueError when using wrong border name."""
    with pytest.raises(ValueError, match='invalid argument, not a rounded or sharp: "wrong_value"'):
        qdarktheme.load_stylesheet(border="wrong_value")


def test_load_stylesheet_with_deprecation_border() -> None:
    """Verify we raise FutureWarning when using deprecated border argument."""
    with pytest.warns(FutureWarning):
        qdarktheme.load_stylesheet(border="sharp")


def test_load_stylesheet_with_wrong_custom_colors() -> None:
    """Verify we raise ValueError when using wrong custom colors."""
    with pytest.raises(
        ValueError,
        match=re.escape(
            'invalid value for argument custom_colors: "wrong color code". '
            "Only support following hexadecimal notations: #RGB, #RGBA, #RRGGBB and #RRGGBBAA. "
            "R (red), G (green), B (blue), and A (alpha) are hexadecimal characters (0-9, a-f or A-F)."
        ),
    ):
        qdarktheme.load_stylesheet(custom_colors={"input.background": "wrong color code"})

    with pytest.raises(KeyError, match='invalid color id for argument custom_colors: "wrong key".'):
        qdarktheme.load_stylesheet(custom_colors={"wrong key": "#121212"})

    with pytest.raises(
        KeyError, match='invalid color id for argument custom_colors: "background>wrong child key".'
    ):
        qdarktheme.load_stylesheet(custom_colors={"background>wrong child key": "#121212"})

    with pytest.raises(
        KeyError, match='invalid color id for argument custom_colors: "background>wrong key>wrong key".'
    ):
        qdarktheme.load_stylesheet(custom_colors={"background>wrong key>wrong key": "#121212"})


def test_clear_cache() -> None:
    """Verify `clear_cache()`."""
    qdarktheme.load_stylesheet()
    qdarktheme.clear_cache()
    # Test function when there is no cache.
    qdarktheme.clear_cache()


def test_get_themes() -> None:
    """Verify `get_themes()` works.

    get_themes() is not called from other functions, so it should be tested.
    """
    qdarktheme.get_themes()
