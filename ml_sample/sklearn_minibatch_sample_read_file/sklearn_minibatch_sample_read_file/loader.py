from typing import Optional, Tuple

import numpy as np
import pandas as pd


class Loader:
    def __init__(self, filepath: str, chunksize: Optional[int] = None):
        self._chunksize = chunksize
        self._filepath = filepath


    def __iter__(self) -> Tuple[np.ndarray]:
        chunks = pd.read_csv(self._filepath, iterator=True, chunksize=self._chunksize)

        for chunk in chunks:
            y = chunk["y"].values
            X = chunk.drop("y", axis=1).values
            yield (X, y)
