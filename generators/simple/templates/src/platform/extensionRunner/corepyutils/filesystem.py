"""Utils that deal with the filesystem."""

import os
from contextlib import contextmanager
from pathlib import Path
from typing import Union, Iterator


@contextmanager
def pushd(working_directory: Union[Path, str]) -> Iterator[None]:
    """Change the current working directory for a block of code."""
    cwd = os.getcwd()
    try:
        os.chdir(working_directory)
        yield
    finally:
        os.chdir(cwd)


def find_repo_root() -> Path:
    """We assume the repo root is core.py's parent."""
    path = Path(__file__).resolve()
    if 'core.py' not in str(path):
        raise Exception("core.py not in sight.")

    while path.name != 'core.py':
        path = path.parent
    assert path.name == 'core.py' and path.is_dir()
    return path.parent
