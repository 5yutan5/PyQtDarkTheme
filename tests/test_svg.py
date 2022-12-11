"""Test for the SVG manager."""
import pytest

from qdarktheme._color import Color
from qdarktheme._icon.svg import Svg


@pytest.mark.parametrize(
    ("rgba", "rotate", "svg_source", "expected_result"),
    [
        ((0, 0, 0, 255), 0, '<svg width="24"></svg>', '<svg fill="#000000" width="24"></svg>'),
        (
            (0, 0, 0, 0),
            0,
            '<svg width="24"></svg>',
            '<svg fill-opacity="0.0" fill="rgb(0,0,0)" width="24"></svg>',
        ),
        (
            (0, 0, 0, 255),
            90,
            '<svg width="24"></svg>',
            '<svg transform="rotate(90, 12, 12)" fill="fill="#000000"" width="24"></svg>',
        ),
    ],
)
def test_svg(mocker, rgba, rotate, svg_source, expected_result):
    """Verify that Svg class build correct SVG."""
    mocker.patch("qdarktheme._icon.svg._svg_resources", return_value={"dummy": svg_source})
    assert str(Svg("dummy").colored(Color.from_rgba(*rgba)).rotate(rotate)) == expected_result


def test_svg_colored_chain():
    """Verify that ``Svg.colored`` chain build correct SVG."""
    svg1 = Svg("arrow_upward").colored(Color.from_hex("#ff0000"))
    svg2 = Svg("arrow_upward").colored(Color.from_hex("#ffffff55")).colored(Color.from_hex("#ff0000"))
    assert str(svg1) == str(svg2)


def test_svg_rotate_chain():
    """Verify that ``Svg.rotate`` chain build correct SVG."""
    svg1 = Svg("arrow_upward").rotate(90)
    svg2 = Svg("arrow_upward").rotate(180).rotate(90)
    assert str(svg1) == str(svg2)
