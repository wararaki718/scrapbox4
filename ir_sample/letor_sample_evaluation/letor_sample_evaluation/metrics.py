import math
from collections import Counter

import pandas as pd
from sklearn.metrics import ndcg_score


def ndcg_at_k(df: pd.DataFrame, k: int=10) -> float:
    qids = df.qid.unique()
    score = 0.0

    for qid in qids:
        target = df[df.qid == qid]
        score += ndcg_score(target.label_norm.values.reshape(1, -1), target.pred.values.reshape(1, -1), k=k)
    return score / qids.shape[0]


def map_at_k(df: pd.DataFrame, k: int=10) -> float:
    qids = df.qid.unique()
    score = 0.0

    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        y = target.label_norm.values[indices][:k]
        score += (y.sum()/k)
    
    return score / qids.shape[0]


def recall_at_k(df: pd.DataFrame, k: int=10) -> float:
    qids = df.qid.unique()
    score = 0.0

    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        y = target.label_norm.values[indices][:k]
        score += (y.sum()/target.shape[0])
    
    return score / qids.shape[0]


def mrr_at_k(df: pd.DataFrame, k: int=10) -> float:
    score = 0.0
    qids = df.qid.unique()
    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        y = target.label_norm.values[indices][:k]
        for idx, i in enumerate(y, start=1):
            if i > 0:
                score += i/idx
                break
    
    return score / qids.shape[0]


def count_appeared_docs_at_k(df: pd.DataFrame, k: int=5) -> int:
    qids = df.qid.unique()
    appeared_docs = set()

    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        docs = target.docid.values[indices][:k]
        appeared_docs |= set(docs)
    
    return len(appeared_docs)


def entropy_at_k(df: pd.DataFrame, k: int=5) -> float:
    qids = df.qid.unique()

    total_counts = Counter()
    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        docs = target.docid.values[indices][:k]
        total_counts.update(docs)
    n_total_items = len(total_counts)

    score = 0.0
    for value in total_counts.values():
        if value == 0:
            continue
        p = value / n_total_items
        score += (-math.log(p) * p)
    
    return score
