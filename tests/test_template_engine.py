"""Tests for the template engine."""
import pytest

from qdarktheme._template.engine import Template


@pytest.mark.parametrize(
    ("text_with_placeholder", "replacements", "filters", "expected_result"),
    [
        ("{{ background }}", {"background": "red"}, {}, "red"),
        ("background-color: {{ background }};", {"background": "red"}, {}, "background-color: red;"),
        (
            "border: {{ size }}px {{ style }} {{ background }};",
            {"size": "2", "style": "solid", "background": "grey"},
            {},
            "border: 2px solid grey;",
        ),
        # Test without placeholder
        ("background: blue;", {"background": "red"}, {}, "background: blue;"),
        # Test int
        ("{{ 100 }}", {}, {}, "100"),
        # Test float
        ("{{ 0.5 }}", {}, {}, "0.5"),
        # Test filter
        ("{{ size|filter }}", {"size": "5"}, {"filter": lambda a: f"{a}px"}, "5px"),
        # Test chan filters
        (
            "{{ size|filter1|filter2 }}",
            {"size": "5"},
            {"filter1": lambda a: f"{a}px", "filter2": lambda a: f"{a};"},
            "5px;",
        ),
    ],
)
def test_template_engine(text_with_placeholder, replacements, filters, expected_result) -> None:
    """Verify template engine runs without error when using various arguments."""
    assert Template(text_with_placeholder, filters).render(replacements) == expected_result


@pytest.mark.parametrize(
    ("text_with_placeholder", "replacements"),
    [
        ("{{ background }}", {}),
        ("{{ background }}", {"border": "#FFFFFF"}),
        ("background-color: {{ background }};", {"border": "#FFFFFF"}),
    ],
)
def test_template_engine_wrong_replacements(text_with_placeholder, replacements) -> None:
    """Verify we raise AssertionError when using wrong replacements."""
    with pytest.raises(AssertionError):
        Template(text_with_placeholder, {}).render(replacements)
