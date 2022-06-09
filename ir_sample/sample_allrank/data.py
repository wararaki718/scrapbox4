from typing import Tuple

import numpy as np


def generate_dummies(n_queries: int=100,
                     n_results: int=20,
                     n_labels: int=5,
                     n_features: int=20) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    X = np.random.randn(n_queries * n_results, n_features)
    y = np.maximum(0, ((X+1)/2).mean(axis=-1)*n_labels).astype(np.int32)
    qid = np.repeat(np.arange(0, n_queries), n_results)
    return X, y, qid
