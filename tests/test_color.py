"""Test for the color manager."""
import re

import pytest

from qdarktheme._color import _HSLA, _RGBA, Color


@pytest.mark.parametrize(
    ("hsla", "rgba"),
    [
        ((0, 0, 0, 0), (0, 0, 0, 0)),
        ((0, 0, 0, 1), (0, 0, 0, 1)),
        ((0, 0, 1, 1), (255, 255, 255, 1)),
        ((0, 1, 0.5, 1), (255, 0, 0, 1)),
        ((120, 1, 0.5, 1), (0, 255, 0, 1)),
        ((240, 1, 0.5, 1), (0, 0, 255, 1)),
        ((60, 1, 0.5, 1), (255, 255, 0, 1)),
        ((180, 1, 0.5, 1), (0, 255, 255, 1)),
        ((300, 1, 0.5, 1), (255, 0, 255, 1)),
        ((0, 0, 0.753, 1), (192, 192, 192, 1)),
        ((0, 0, 0.502, 1), (128, 128, 128, 1)),
        ((0, 1, 0.251, 1), (128, 0, 0, 1)),
        ((60, 1, 0.251, 1), (128, 128, 0, 1)),
        ((120, 1, 0.251, 1), (0, 128, 0, 1)),
        ((300, 1, 0.251, 1), (128, 0, 128, 1)),
        ((180, 1, 0.251, 1), (0, 128, 128, 1)),
        ((240, 1, 0.251, 1), (0, 0, 128, 1)),
    ],
)
def test_hsla_from_rgba(hsla, rgba) -> None:
    """Verify that converting from rgba to hsla correctly."""
    assert _HSLA(*hsla).to_rgba() == _RGBA(*rgba)


@pytest.mark.parametrize(
    ("rgba", "hsla"),
    [
        ((0, 0, 0, 0), (0, 0, 0, 0)),
        ((0, 0, 0, 1), (0, 0, 0, 1)),
        ((255, 255, 255, 1), (0, 0, 1, 1)),
        ((255, 0, 0, 1), (0, 1, 0.5, 1)),
        ((0, 255, 0, 1), (120, 1, 0.5, 1)),
        ((0, 0, 255, 1), (240, 1, 0.5, 1)),
        ((255, 255, 0, 1), (60, 1, 0.5, 1)),
        ((0, 255, 255, 1), (180, 1, 0.5, 1)),
        ((255, 0, 255, 1), (300, 1, 0.5, 1)),
        ((192, 192, 192, 1), (0, 0, 0.753, 1)),
        ((128, 128, 128, 1), (0, 0, 0.502, 1)),
        ((128, 0, 0, 1), (0, 1, 0.251, 1)),
        ((128, 128, 0, 1), (60, 1, 0.251, 1)),
        ((0, 128, 0, 1), (120, 1, 0.251, 1)),
        ((128, 0, 128, 1), (300, 1, 0.251, 1)),
        ((0, 128, 128, 1), (180, 1, 0.251, 1)),
        ((0, 0, 128, 1), (240, 1, 0.251, 1)),
    ],
)
def test_rgba_from_hsla(rgba, hsla) -> None:
    """Verify that converting from hsla to rgba correctly."""
    assert _HSLA.from_rgba(_RGBA(*rgba)) == _HSLA(*hsla)


@pytest.mark.parametrize(
    ("hex", "rgba"),
    [
        ("#000000", (0, 0, 0, 1)),
        ("#FFFFFF", (255, 255, 255, 1)),
        ("#FF00FF", (255, 0, 255, 1)),
        ("#C0C0C0", (192, 192, 192, 1)),
        ("#808080", (128, 128, 128, 1)),
        ("#800000", (128, 0, 0, 1)),
        ("#808000", (128, 128, 0, 1)),
        ("#008000", (0, 128, 0, 1)),
        ("#800080", (128, 0, 128, 1)),
        ("#008080", (0, 128, 128, 1)),
        ("#000080", (0, 0, 128, 1)),
        ("#010203", (1, 2, 3, 1)),
        ("#040506", (4, 5, 6, 1)),
        ("#070809", (7, 8, 9, 1)),
        ("#0a0A0a", (10, 10, 10, 1)),
        ("#0b0B0b", (11, 11, 11, 1)),
        ("#0c0C0c", (12, 12, 12, 1)),
        ("#0d0D0d", (13, 13, 13, 1)),
        ("#0e0E0e", (14, 14, 14, 1)),
        ("#0f0F0f", (15, 15, 15, 1)),
        ("#a0A0a0", (160, 160, 160, 1)),
        ("#CFA", (204, 255, 170, 1)),
        ("#CFA8", (204, 255, 170, 0.533)),
    ],
)
def test_rgba_from_hex(hex, rgba) -> None:
    """Verify that converting from hex to rgba correctly."""
    assert Color.from_hex(hex).rgba == _RGBA(*rgba)


@pytest.mark.parametrize(
    "wrong_hex",
    [
        ("#"),
        ("#1"),
        ("#12"),
        ("#12345"),
        ("#1234567"),
        ("#123456789"),
        ("123#"),
        ("#00000g"),
        ("#he00ff"),
    ],
)
def test_color_from_wrong_hex(wrong_hex) -> None:
    """Verify we raise ValueError when using wrong hexadecimal notations."""
    with pytest.raises(
        ValueError,
        match=re.escape(
            f'invalid hex color format: "{wrong_hex}". '
            "Only support following hexadecimal notations: #RGB, #RGBA, #RRGGBB and #RRGGBBAA. "
            "R (red), G (green), B (blue), and A (alpha) are hexadecimal characters "
            "(0-9, a-f or A-F)."
        ),
    ):
        Color.from_hex(wrong_hex)
