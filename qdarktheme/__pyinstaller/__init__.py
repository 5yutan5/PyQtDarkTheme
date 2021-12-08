"""Package for PyInstaller hook."""


def get_hook_dirs():
    """The PyInstaller plugin method."""
    from pathlib import Path

    package_folder = Path(__file__).parent
    return [str(package_folder.absolute())]
