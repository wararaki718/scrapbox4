from pathlib import Path
from py._path.local import LocalPath

import pandas as pd
import pytest

from app.sample import load_binary


@pytest.fixture
def binary_file(tmp_path: LocalPath) -> Path:
    binary_path = tmp_path / "hello.pkl"
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    df.to_pickle(binary_path)
    return Path(binary_path)


def test_load_binary(binary_file: Path):
    df = load_binary(binary_file)
    expected_df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    assert df.equals(expected_df)
