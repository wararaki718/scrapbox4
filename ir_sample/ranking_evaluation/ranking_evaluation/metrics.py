from collections import Counter
import math

import numpy as np

from sklearn.metrics import ndcg_score


def precision_at_k(y_interactions: np.ndarray, y_score: np.ndarray, k: int=10) -> float:    
    indices = y_score.argsort()[::-1]
    y = y_interactions[indices][:k]
    return y.sum() / k


def recall_at_k(y_interactions: np.ndarray, y_score: np.ndarray, k: int=10) -> float:
    indices = y_score.argsort()[::-1]
    y = y_interactions[indices][:k]
    return y.sum() / y_interactions.sum()


def ndcg_at_k(y_true: np.ndarray, y_score: np.ndarray, k: int=10) -> float:
    return ndcg_score(y_true.reshape(1, -1), y_score.reshape(1, -1), k=k)


def entropy_at_k(y_all_items: np.ndarray, y_pred_items: np.ndarray, k: int=10) -> float:
    k = min(k, y_pred_items.shape[0])
    
    c = Counter(y_pred_items[:k])
    n_total_items = np.unique(y_all_items).shape[0]
    entropy = 0.0
    for cnt in c.values():
        p = cnt / n_total_items
        entropy += (-math.log(p) * p)

    return entropy


def gini_at_k(y_all_items: np.ndarray, y_pred_items: np.ndarray, k: int=10) -> float:
    k = min(k, y_pred_items.shape[0])
    
    c = Counter(y_pred_items[:k])
    n_total_items = np.unique(y_all_items).shape[0]
    n_items = len(c)
    cnts = list(c.values())
    cnts.sort()

    gini = 0.0
    for i, cnt in enumerate(cnts):
        gini += (2 * i - n_items + 1) * cnt
    gini /= (n_items * n_total_items)

    return gini


def map_at_k(y_interactions: np.ndarray, y_scores: np.ndarray, k: int=10) -> float:
    average_precision = 0.0
    weights = np.arange(1, k+1).reshape(1, -1) / k
    for interaction, score in zip(y_interactions, y_scores):
        indices = score.argsort()[::-1]
        y = interaction[indices][:k]
        average_precision += (weights * y).sum() / y.sum()
    
    return average_precision / y_interactions.shape[0]


def mrr_at_k(y_interactions: np.ndarray, y_scores: np.ndarray, k: int=10) -> float:
    mrr = 0.0
    for interaction, score in zip(y_interactions, y_scores):
        indices = score.argsort()[::-1]
        y = interaction[indices][:k]
        for idx, i in enumerate(y, start=1):
            if i > 0:
                mrr += i/idx
                break
    
    return mrr / y_interactions.shape[0]
