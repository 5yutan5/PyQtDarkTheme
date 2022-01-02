"""Test freezing-package."""
import shutil
import subprocess
from pathlib import Path

import PyInstaller.__main__ as pyinstaller  # type: ignore
from rich.console import Console

IGNORE_MESSAGES = (
    "Unable to create basic Accelerated OpenGL renderer.",
    "Core Image is now using the software OpenGL renderer. This will be slow.",
)
_console = Console(force_terminal=True)


class SvgFileNotFoundError(FileNotFoundError):
    """Error raise if cannot open svg file."""

    pass


def _print_successfull_message() -> None:
    _console.log("Build finished successfully!", style="green")


def _test_freezing_pkg(pkg_name: str) -> str:
    if pkg_name not in ["PyInstaller", "cx_Freeze"]:
        raise RuntimeError(f"invalid package name: {pkg_name}")

    demo_app_src_path = Path(__file__).absolute().parent / "demo_app.py"
    app_name = "app"
    output_path = Path(__file__).absolute().parent.parent.parent / "dist" / pkg_name

    _console.log(f"Building app with {pkg_name}...")
    if output_path.exists():
        _console.log(f"Removing {output_path}")
        shutil.rmtree(output_path)
    _console.log(f"Creating {output_path}...")
    output_path.mkdir()

    _console.print()
    _console.print("------------------------")
    _console.print(f"Outputs from {pkg_name}")
    _console.print("------------------------")
    if pkg_name == "PyInstaller":
        command = [
            "--clean",
            "-y",
            str(demo_app_src_path),
            "-n",
            app_name,
            "--distpath",
            str(output_path),
            "--onefile",
        ]
        _console.log(f"Run: {command}")
        pyinstaller.run(command)
    elif pkg_name == "cx_Freeze":
        command = [
            "poetry",
            "run",
            "cxfreeze",
            "--target-name",
            app_name,
            "-c",
            str(demo_app_src_path),
            "--target-dir",
            str(output_path),
        ]
        _console.log(f"Run: {command}")
        subprocess.run(command)

    _console.print()
    app_path = output_path / app_name
    _console.log(f"Opening {app_path}...")
    return subprocess.check_output([str(app_path)], stderr=subprocess.STDOUT, encoding="utf-8")


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
    _console.log("Build start", style="yellow")
    for pkg_name in ["PyInstaller"]:
        output = _test_freezing_pkg(pkg_name)
        _check_output(output)


if __name__ == "__main__":
    _main()
