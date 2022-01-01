"""Test freezing-package."""
import subprocess
from pathlib import Path
from time import sleep

import click
import PyInstaller.__main__ as pyinstaller  # type: ignore

IGNORE_MESSAGES = (
    "Unable to create basic Accelerated OpenGL renderer.",
    "Core Image is now using the software OpenGL renderer. This will be slow.",
)


class SvgFileNotFoundError(FileNotFoundError):
    """Error raise if cannot open svg file."""

    pass


def _print_successfull_message() -> None:
    click.secho("Build finished successfully!", fg="green")


def _create_app_with_pyinstaller(target: Path) -> Path:
    app_name = "app"
    app_path = Path(__file__).parent.parent.parent / "dist" / app_name
    if app_path.exists():
        app_path.unlink()
    pyinstaller.run(["--clean", "-y", str(target), "-n", app_name, "--onefile"])
    return app_path


def _test_pyinstaller() -> str:
    click.echo("================================")
    click.echo("Building app with PyInstaller...")
    click.echo("================================")
    demo_app_src_path = Path(__file__).parent / "demo_app.py"
    demo_app_path = _create_app_with_pyinstaller(demo_app_src_path)
    return subprocess.check_output([str(demo_app_path)], stderr=subprocess.STDOUT, encoding="utf-8")


def _check_output(output: str) -> None:
    if output == "":
        click.echo("There is no output from demo app")
        _print_successfull_message()
        return
    else:
        click.echo("----------------")
        click.echo("Demo app outputs")
        click.echo("----------------")
        click.echo(output)

    if "qt.svg: Cannot open file" in output:
        sleep(0.5)
        raise SvgFileNotFoundError("QtSvg module cannot open svg files, because: No such file or directory")
    for ignore_image in IGNORE_MESSAGES:
        if ignore_image in output:
            click.echo(f"Ignore: {ignore_image}")
            output = output.replace(ignore_image, "")
    result = output.replace("\n", "")
    if result == "":
        _print_successfull_message()
        return
    sleep(0.5)
    raise RuntimeError("There is unexpected output")


def _main() -> None:
    click.echo("Build start")
    output = _test_pyinstaller()
    _check_output(output)


if __name__ == "__main__":
    _main()
