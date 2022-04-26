"""Utility methods for tools."""
from __future__ import annotations

import inspect
from pathlib import Path

from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

import tools


def get_project_root_path() -> Path:
    """Return the project root path.

    Returns:
        Project root path.
    """
    return Path(inspect.getfile(tools)).parent.parent


def _walk_directory(directory: Path, tree: Tree, ignore_hiddenfile: bool, level: int | None) -> None:
    """Recursively build a Tree with directory contents.

    See https://github.com/willmcgugan/rich/blob/master/examples/tree.py.
    """
    if level is not None and level <= 0:
        raise ValueError("tree: Invalid level, must be greater than 0.")
    # Sort dirs first then by filename
    paths = sorted(
        directory.iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if ignore_hiddenfile and path.name.startswith("."):
            continue

        show_dir_contents = True
        if level is not None and level <= 1:
            show_dir_contents = False

        if path.is_dir() and show_dir_contents:
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: {escape(path.name)}",
                style=style,
                guide_style=style,
            )
            _level = None if level is None else level - 1
            _walk_directory(path, branch, ignore_hiddenfile, _level)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            if path.suffix == ".py":
                icon = "🐍 "
            elif path.is_dir():
                icon = "📂 "
            else:
                icon = "📄 "
            tree.add(Text(icon) + text_filename)


def get_file_tree(directory: Path, ignore_hiddenfile: bool = False, level: int | None = None) -> Tree:
    """Return tree object of directory.

    Args:
        directory: Root directory.
        ignore_hiddenfile: If set to True, ignore hidden files.
        level: Max display depth of the directory tree.

    Returns:
        Tree: The tree object of rich lib.
    """
    tree = Tree(
        f":open_file_folder: {directory}",
        guide_style="bold bright_blue",
    )
    _walk_directory(Path(directory), tree, ignore_hiddenfile, level)
    return tree
