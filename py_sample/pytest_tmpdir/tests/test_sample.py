from py._path.local import LocalPath
from pathlib import Path
import pytest

from app.sample import load_texts


@pytest.fixture
def text_dir(tmpdir: LocalPath) -> Path:
    file_dir = tmpdir.mkdir("sub")
    file1 = file_dir.join("hello.txt")
    file1.write("hello")
    file2 = file_dir.join("world.txt")
    file2.write("world")

    return Path(file_dir)


def test_load_texts(text_dir: Path):
    texts = load_texts(text_dir)
    assert texts == "helloworld"
