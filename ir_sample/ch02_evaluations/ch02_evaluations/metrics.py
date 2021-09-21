import numpy as np
from numpy.lib.utils import lookfor
from sklearn.metrics import precision_score, recall_score


def precision_at_k(y_true: np.ndarray, y_pred: np.ndarray, k: int=5) -> float:
    assert y_true.shape[0] >= k
    assert y_pred.shape[0] >= k

    return precision_score(y_true[:k], y_pred[:k])

def recall_at_k(y_true: np.ndarray, y_pred: np.ndarray, k: int=5) -> float:
    assert y_true.shape[0] >= k
    assert y_pred.shape[0] >= k

    return recall_score(y_true[:k], y_pred[:k])
