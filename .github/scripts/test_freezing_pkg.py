"""Test freezing-library."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from enum import Enum
from pathlib import Path

from rich.console import Console

IGNORE_MESSAGES = (
    "Unable to create basic Accelerated OpenGL renderer.",
    "Core Image is now using the software OpenGL renderer. This will be slow.",
)
_console = Console(force_terminal=True)


class _Library(Enum):
    PYINSTALLER = "PyInstaller"
    CX_FREEZE = "cx_Freeze"


class SvgFileNotFoundError(FileNotFoundError):
    """Error raise if cannot open svg file."""

    pass


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="This program test freezing-library.")
    parser.add_argument(
        f"--{_Library.PYINSTALLER.value}",
        help=f"Test {_Library.PYINSTALLER.value}",
        action="store_true",
    )
    parser.add_argument(
        f"--{_Library.CX_FREEZE.value}",
        help=f"Test {_Library.CX_FREEZE.value}",
        action="store_true",
    )
    return parser.parse_args()


def _print_successfull_message() -> None:
    _console.log("Build finished successfully!", style="green")


def _test_freezing_lib(lib: _Library) -> str:
    if lib not in _Library:
        raise RuntimeError(f"invalid library name: {lib}")

    demo_app_src_path = Path(__file__).absolute().parent / "demo_app.py"
    app_name = "app"
    output_path = Path(__file__).absolute().parent.parent.parent / "dist" / lib.value

    _console.log(f"Building app with {lib}...")
    if output_path.exists():
        _console.log(f"Removing {output_path}")
        shutil.rmtree(output_path)
    _console.log(f"Creating {output_path}...")
    output_path.mkdir()

    command = []
    if lib is _Library.PYINSTALLER:
        command = [
            "pyinstaller",
            "--clean",
            "-y",
            str(demo_app_src_path),
            "-n",
            app_name,
            "--distpath",
            str(output_path),
            "--onefile",
        ]
    elif lib is _Library.CX_FREEZE:
        command = [
            "cxfreeze",
            "--target-name",
            app_name,
            "-c",
            str(demo_app_src_path),
            "--target-dir",
            str(output_path),
        ]
    _console.log(f"Running: {command}")

    _console.print()
    _console.print("-------------" + "-" * len(lib.value))
    _console.print(f"Outputs from {lib.value}")
    _console.print("-------------" + "-" * len(lib.value))
    subprocess.run(command)

    _console.print()
    app_path = output_path / app_name
    _console.log(f"Opening {app_path}...")
    result = subprocess.check_output([str(app_path)], stderr=subprocess.STDOUT)
    return result.decode("utf-8")


def _check_output(output: str) -> None:
    if output == "":
        _console.log("There is no output from demo app")
        _print_successfull_message()
        return
    else:
        _console.log("There is some outputs from demo app\n")
        _console.print("----------------")
        _console.print("Demo app outputs")
        _console.print("----------------")
        _console.print(output)

    if "qt.svg: Cannot open file" in output:
        raise SvgFileNotFoundError("QtSvg module cannot open svg files, because: No such file or directory")
    for message in IGNORE_MESSAGES:
        if message in output:
            _console.log(f"Ignore: {message}")
            output = output.replace(message, "")
    result = output.replace("\n", "")
    if result == "":
        _print_successfull_message()
        return
    raise RuntimeError("There is unexpected output")


def _main() -> None:
    args = _parse_args()

    _console.log("Build start", style="yellow")

    if args.PyInstaller:
        output = _test_freezing_lib(_Library.PYINSTALLER)
        _check_output(output)
    else:
        _console.log(f"Skip {_Library.PYINSTALLER.value} test")

    if args.cx_Freeze:
        output = _test_freezing_lib(_Library.CX_FREEZE)
        _check_output(output)
    else:
        _console.log(f"Skip {_Library.CX_FREEZE.value} test")


if __name__ == "__main__":
    _main()
