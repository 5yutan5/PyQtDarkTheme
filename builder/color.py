# ---------------------------------------------------------------------------------------------
#  Copyright (c) Yunosuke Ohsugi. All rights reserved.
#  Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------*/

from __future__ import annotations

import math
from functools import lru_cache


class RGBA:
    def __init__(self, r: float, g: float, b: float, a: float = 1) -> None:
        self._r = min(255, max(0, r))
        self._g = min(255, max(0, g))
        self._b = min(255, max(0, b))
        self._a = max(min(1, a), 0)

    def __str__(self) -> str:
        return f"rgba({self._r:.3f}, {self._g:.3f}, {self._b:.3f}, {self._a:.3f})"

    def __getitem__(self, item: int) -> float:
        return [self._r, self._g, self._b, self._a][item]

    @staticmethod
    @lru_cache()
    def from_hex(color_hex: str) -> RGBA:
        hex_ = color_hex.lstrip("#")
        r, g, b, a = 255, 0, 0, 1
        if len(hex_) == 3:  # RGB format
            r, g, b = [int(char, 16) for char in hex_]
            r, g, b = 16 * r + r, 16 * g + g, 16 * b + b
        if len(hex_) == 4:  # RGBA format
            r, g, b, a = [int(char, 16) for char in hex_]
            r, g, b = 16 * r + r, 16 * g + g, 16 * b + b
            a = (16 * a + a) / 255
        if len(hex_) == 6:  # RRGGBB format
            r, g, b = bytes.fromhex(hex_)
            a = 1
        elif len(hex_) == 8:  # RRGGBBAA format
            r, g, b, a = bytes.fromhex(hex_)
            a = a / 255
        return RGBA(r, g, b, a)

    @staticmethod
    @lru_cache()
    def to_hex(rgba: RGBA) -> str:
        r, g, b, a = rgba
        return f"{math.floor(r):x}{math.floor(g):x}{math.floor(b):x}{math.floor(a*255):02x}"
