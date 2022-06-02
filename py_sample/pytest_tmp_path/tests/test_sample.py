from pathlib import Path
from py._path.local import LocalPath

import pytest

from app.sample import load_txt


@pytest.fixture
def text_file(tmp_path: LocalPath) -> Path:
    text_path = tmp_path / "hello.txt"
    text_path.write_text("hello")
    return Path(text_path)


def test_load_txt(text_file: Path):
    text = load_txt(text_file)
    assert text == "hello"
