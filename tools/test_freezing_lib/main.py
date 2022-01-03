"""Test freezing-library."""
from __future__ import annotations

import argparse
import shutil
import subprocess
from enum import Enum
from pathlib import Path

from rich.console import Console, Group, RenderableType
from rich.panel import Panel
from rich.text import Text

from tools.util import get_file_tree, get_project_root_path

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
    output_path = get_project_root_path() / "dist" / lib.value

    _console.log(f"Building app with {lib} ...")
    if output_path.exists():
        _console.log(f"Removing {output_path}")
        shutil.rmtree(output_path)
    _console.log(f"Creating {output_path} ...")
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


def main() -> int:
    """The main method of this package."""
    args = _parse_args()
    pass_count, error_count, skip_count = 0, 0, 0
    dist_path = get_project_root_path() / "dist"
    errors: dict[str, Exception] = {}

    _console.log("Freezing-lib test session start", style="yellow")

    if not dist_path.exists():
        _console.log(f"Creating {dist_path} ...")

    for library in _Library:
        if not getattr(args, library.value):
            # if library.value not in (args.PyInstaller, args.cx_Freeze):
            _console.log(f"Skip {library.value} test")
            skip_count += 1
            continue

        try:
            output = _test_freezing_lib(library)
            _check_output(output)
        except Exception as e:
            _console.print_exception()
            errors[library.value] = e
            error_count += 1
        else:
            pass_count += 1

    # Create report
    report: list[RenderableType] = []
    report.append(
        Panel(
            f"{error_count} failed, {pass_count} passed, {skip_count} skipped",
            style="green" if error_count == 0 else "red",
        )
    )

    if error_count != 0:
        error_report: list[RenderableType] = []
        for lib_name, error in errors.items():
            error_report.append(f"{lib_name}\n{len(lib_name)*'-'}")
            error_report.append(f"{error}\n")
        report.append(Panel(Group(*error_report), title="FAILURES", style="red"))

    report.append(Panel(get_file_tree(dist_path, level=3), title=f"Contents of {dist_path}"))

    _console.print(
        Panel(
            renderable=Group(*report),
            title=Text("Test summary info"),
        )
    )

    if error_count != 0:
        return 1
    return 0
