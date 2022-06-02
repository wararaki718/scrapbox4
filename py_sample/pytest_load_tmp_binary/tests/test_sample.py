import pickle
from pathlib import Path

import pytest

from app.sample import load_binary


@pytest.fixture
def binary_file(tmp_path: Path) -> Path:
    binary_path = tmp_path / "hello.pkl"
    with open(binary_path, "wb") as f:
        pickle.dump("hello", f)
    return Path(binary_path)


def test_load_binary(binary_file: Path):
    text = load_binary(binary_file)
    assert text == "hello"
