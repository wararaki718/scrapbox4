import math
from collections import Counter

import numpy as np
import pandas as pd


def _dcg1(rels: np.ndarray) -> float:
    score = rels[0]
    for i in range(1, rels.shape[0]):
        score += rels[i] / np.log2(i + 1)
    return score


def _dcg2(rels: np.ndarray) -> float:
    score = 0.0
    for i, rel in enumerate(rels):
        score += (2 ** rel - 1) / np.log2(i + 2)
    return score


def ndcg_at_k(df: pd.DataFrame, k: int=10, dcg_type: int=2) -> float:
    qids = df.qid.unique()
    score = 0.0

    if dcg_type == 1:
        _dcg = _dcg1
    else:
        _dcg = _dcg2

    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        dcg = _dcg(target.label_norm.values[indices][:k])

        indices = target.label_norm.values.argsort()[::-1]
        idcg = _dcg(target.label_norm.values[indices][:k])
        if math.isclose(dcg, 0.0) or math.isclose(idcg, 0.0):
            continue
        score += (dcg / idcg)
    
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
    n_total_items = sum(total_counts.values())

    score = 0.0
    for value in total_counts.values():
        if value == 0:
            continue
        p = value / n_total_items
        score += (-math.log2(p) * p)
    
    return score


def gini_at_k(df: pd.DataFrame, k: int=5) -> float:
    qids = df.qid.unique()

    total_counts = Counter()
    for qid in qids:
        target = df[df.qid == qid]
        indices = target.pred.values.argsort()[::-1]
        docs = target.docid.values[indices][:k]
        total_counts.update(docs)
    
    score = 0
    cnt = 0
    for i in range(qids.shape[0]):
        for j in range(i+1, qids.shape[0]):
            score += abs(total_counts[qids[i]] - total_counts[qids[j]])
            cnt += 1
    score /= cnt
    score /= 2*(sum(total_counts.values())/len(total_counts))
                
    return score
