"""Module building theme color documentation."""
from __future__ import annotations

import json
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

from qdarktheme.color import Color
from tools.util import get_style_path

_DEFAULT_DARK_COLORS: dict = json.loads((get_style_path() / "colors" / "dark.json").read_bytes())
_DEFAULT_LIGHT_COLORS: dict = json.loads((get_style_path() / "colors" / "light.json").read_bytes())


@dataclass
class _ThemeColor:
    id: str
    default_dark_value: str
    default_light_value: str
    description: str
    image_name: str | None
    inherited_by: list[str] | None = None
    inherits: str | None = None


def _to_hex(base_color: str, color_info: dict[str, float]) -> str:
    color = Color.from_hex(base_color)
    if color_info.get("transparent"):
        color = color.transparent(color_info["transparent"])
    if color_info.get("darken"):
        color = color.darken(color_info["darken"])
    if color_info.get("lighten"):
        color = color.lighten(color_info["lighten"])
    return f"#{color._to_hex()}"


def _parse_theme_color_files() -> dict[str, list[_ThemeColor]]:
    validate_property: dict = json.loads((get_style_path() / "colors" / "validate.json").read_bytes())
    theme_color_properties: dict[str, dict] = validate_property["properties"]
    groups: dict[str, str] = validate_property["groups"]

    theme_colors: dict[str, list[_ThemeColor]] = {group: [] for group in groups.keys()}
    for id, theme_color_property in theme_color_properties.items():
        inherited_theme_color_properties: dict[str, dict] | None = theme_color_property.get(
            "properties"
        )
        if inherited_theme_color_properties is not None:
            # Parse base theme color
            base_color_property = inherited_theme_color_properties.pop("base")
            theme_colors[base_color_property["group"]].append(
                _ThemeColor(
                    id,
                    _DEFAULT_DARK_COLORS[id]["base"],
                    _DEFAULT_LIGHT_COLORS[id]["base"],
                    base_color_property["description"],
                    base_color_property.get("image_name"),
                    list(inherited_theme_color_properties.keys()),
                )
            )
            # Parse inherited theme color
            for (
                inherited_id,
                inherited_theme_color_property,
            ) in inherited_theme_color_properties.items():
                theme_colors[inherited_theme_color_property["group"]].append(
                    _ThemeColor(
                        f"{id}>{inherited_id}",
                        _to_hex(
                            _DEFAULT_DARK_COLORS[id]["base"], _DEFAULT_DARK_COLORS[id][inherited_id]
                        ),
                        _to_hex(
                            _DEFAULT_LIGHT_COLORS[id]["base"], _DEFAULT_LIGHT_COLORS[id][inherited_id]
                        ),
                        inherited_theme_color_property["description"],
                        inherited_theme_color_property.get("image_name"),
                        inherits=id,
                    )
                )
        else:
            # Parse single theme color
            theme_colors[theme_color_property["group"]].append(
                _ThemeColor(
                    id,
                    _DEFAULT_DARK_COLORS[id],
                    _DEFAULT_LIGHT_COLORS[id],
                    theme_color_property["description"],
                    theme_color_property.get("image_name"),
                )
            )
    return theme_colors


def _mk_group_section(title, description) -> str:
    doc_text = title + "\n"
    doc_text += "^" * len(title) + "\n\n"
    doc_text += description + "\n"
    return doc_text


def _mk_color_section(theme_color: _ThemeColor) -> str:
    doc_text = "\n"
    doc_text += f"- ``{theme_color.id}``\n\n"
    doc_text += f"  {theme_color.description}\n\n"
    doc_text += "  .. list-table::\n"
    doc_text += "    :stub-columns: 1\n\n"
    if theme_color.inherits is not None:
        doc_text += "    * - Inherits\n"
        doc_text += "      - " + f"``{theme_color.inherits}``\n"
    if theme_color.inherited_by is not None:
        doc_text += "    * - Inherited by\n"
        doc_text += "      -"
        for inherited_by in theme_color.inherited_by:
            doc_text += f" ``{inherited_by}``"
        doc_text += "\n"
    doc_text += "    * - Default(light)\n"
    doc_text += "      - " + theme_color.default_light_value + "\n"
    doc_text += "    * - Default(dark)\n"
    doc_text += "      - " + theme_color.default_dark_value + "\n"
    if theme_color.image_name is not None:
        doc_text += "    * - View\n"
        doc_text += "      - .. image:: ../../_static/theme_color_api/images/" + theme_color.image_name
        doc_text += "\n"
        doc_text += "            :class:dark-light\n\n"
    return doc_text


def _mk_color_list_section(theme_colors: dict[str, list[_ThemeColor]]) -> str:
    validate_property: dict = json.loads((get_style_path() / "colors" / "validate.json").read_bytes())
    groups: dict[str, str] = validate_property["groups"]
    doc_text = "\n"
    for group_name, group_description in sorted(groups.items()):
        doc_text += _mk_group_section(group_name, group_description)
        for theme_color in theme_colors[group_name]:
            doc_text += _mk_color_section(theme_color)
        doc_text += "\n"
    return doc_text


def _mk_theme_color_doc(doc_template: str, color_list_section: str) -> str:
    return doc_template + color_list_section


def main() -> None:
    """Build theme color documentation."""
    output_path = Path(__file__).parent.parent.parent / "docs/source/reference/theme_color.rst"
    doc_template = resources.read_text("tools.build_theme_color_doc", "theme_color.template.rst")
    theme_colors = _parse_theme_color_files()
    color_list_section = _mk_color_list_section(theme_colors)
    theme_color_doc = _mk_theme_color_doc(doc_template, color_list_section)
    output_path.write_text(theme_color_doc)
