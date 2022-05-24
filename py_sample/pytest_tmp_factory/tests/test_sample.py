from pathlib import Path
import pytest

from app.sample import load_txt


@pytest.fixture
def text_file(tmp_path: Path) -> Path:
    text_path = tmp_path / "hello.txt"
    text_path.write_text("hello")
    return text_path


def test_load_txt(text_file: Path):
    text = load_txt(text_file)
    assert text == "hello"
