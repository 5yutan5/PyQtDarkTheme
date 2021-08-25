import inspect
from pathlib import Path

import qdarktheme


def get_qdarktheme_root_path() -> Path:
    return Path(inspect.getfile(qdarktheme)).parent
