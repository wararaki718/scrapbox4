from typing import Tuple

import numpy as np
from sklearn.datasets import fetch_20newsgroups


def load_news() -> Tuple[np.ndarray, np.ndarray]:
    texts = fetch_20newsgroups(
        subset="train",
        categories=["comp.graphics", "sci.med"],
        shuffle=True,
        random_state=42
    )
    X = texts.data
    y = texts.target

    return (X, y)
