from __future__ import annotations

import json
import re
from functools import lru_cache

from qdarktheme import _resources
from qdarktheme._color import Color


@lru_cache()
def _svg_resources() -> dict[str, str]:
    return json.loads(_resources.SVG_RESOURCES)


class Svg:
    """Class to manage SVG."""

    _SVG_FILL_RE = re.compile(r'fill=".*?"')
    _SVG_FILL_OPACITY_RE = re.compile(r'fill-opacity=".*?"')
    _SVG_TRANSFORM_RE = re.compile(r'transform=".*?"')

    def __init__(self, id: str) -> None:
        """Initialize svg manager."""
        self._id = id
        self._color = None
        self._rotate = None
        self._source = _svg_resources()[self._id]

    def __str__(self) -> str:
        """Return the svg source code."""
        return self._source

    def colored(self, color: Color) -> Svg:
        """Add or change svg color."""
        svg_tiny_color_formats = color.to_svg_tiny_color_format().split(" ")
        if len(svg_tiny_color_formats) == 2:
            new_svg_color, new_svg_opacity = svg_tiny_color_formats
        else:
            new_svg_color = svg_tiny_color_formats[0]
            new_svg_opacity = None

        current_svg_color = Svg._SVG_FILL_RE.search(self._source)
        current_svg_opacity = Svg._SVG_FILL_OPACITY_RE.search(self._source)

        # Add or change SVG color.
        if current_svg_color is None:
            self._source = self._source.replace("<svg ", f"<svg {new_svg_color} ")
        else:
            self._source = self._source.replace(current_svg_color.group(), new_svg_color)

        # Add or change SVG opacity.
        if new_svg_opacity is not None and current_svg_opacity is None:
            self._source = self._source.replace("<svg ", f"<svg {new_svg_opacity} ")
        elif new_svg_opacity is not None and current_svg_opacity is not None:
            self._source = self._source.replace(current_svg_opacity.group(), new_svg_opacity)

        # Remove SVG opacity
        if new_svg_opacity is None and current_svg_opacity is not None:
            self._source = self._source.replace(" " + current_svg_opacity.group(), "")
        return self

    def rotate(self, rotate: int) -> Svg:
        """Rotate svg."""
        if rotate == 0:
            return self

        current_svg_transform = Svg._SVG_TRANSFORM_RE.search(self._source)
        new_svg_transform = f'transform="rotate({rotate}, 12, 12)"'
        if current_svg_transform is None:
            self._source = self._source.replace("<svg ", f"<svg {new_svg_transform} ")
        else:
            self._source = self._source.replace(current_svg_transform.group(), new_svg_transform)

        return self
