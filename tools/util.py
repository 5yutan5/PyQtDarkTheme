"""Utility methods for tools."""
from __future__ import annotations

import inspect
from pathlib import Path

import tools


def get_project_root_path() -> Path:
    """Return the project root path.

    Returns:
        Project root path.
    """
    return Path(inspect.getfile(tools)).parent.parent


def get_style_path() -> Path:
    """Return the style root path."""
    return Path(__file__).parent.parent / "style"
