"""Test freezing-package."""
import subprocess
from pathlib import Path

import click
import PyInstaller.__main__ as pyinstaller  # type: ignore


class SvgFileNotFoundError(FileNotFoundError):
    """Error raise if cannot open svg file."""

    pass


def _create_app_with_pyinstaller(target: Path) -> Path:
    app_name = "app"
    app_path = Path(__file__).parent.parent.parent / "dist" / app_name
    if app_path.exists():
        app_path.unlink()
    pyinstaller.run(["--clean", "-y", str(target), "-n", app_name, "--onefile"])
    return app_path


def _test_pyinstaller() -> None:
    click.echo("================================")
    click.echo("Building app with PyInstaller...")
    click.echo("================================")
    demo_app_src_path = Path(__file__).parent / "demo_app.py"
    demo_app_path = _create_app_with_pyinstaller(demo_app_src_path)
    result = subprocess.check_output(demo_app_path, stderr=subprocess.STDOUT, encoding="utf-8")
    if result == "":
        click.echo("There is no output from demo app")
        click.secho("Build finished successfully!", fg="green")
        return
    else:
        click.echo("Demo app output:")
        click.echo("----------------")
        click.echo(result)

    if "qt.svg: Cannot open file" in result:
        raise SvgFileNotFoundError("QtSvg module cannot open svg files, because: No such file or directory")
    raise RuntimeError("There is unexpected output")


def _main() -> None:
    _test_pyinstaller()


if __name__ == "__main__":
    _main()
