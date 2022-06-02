from pathlib import Path

import pandas as pd


def load_binary(binary_path: Path) -> pd.DataFrame:
    return pd.read_pickle(binary_path)
