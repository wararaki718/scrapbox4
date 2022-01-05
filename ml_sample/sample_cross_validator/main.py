import time
from typing import Optional, Union

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold, StratifiedKFold, GroupKFold
from sklearn.linear_model import LogisticRegression



def cross_validation(kf: Union[KFold, StratifiedKFold, GroupKFold], X: np.ndarray, y: np.ndarray, groups: Optional[np.ndarray]=None) -> dict:
    test_scores = []
    fit_times = []
    score_times = []
    for i, (train_indices, valid_indices) in enumerate(kf.split(X, y, groups)):
        X_train, X_valid = X[train_indices], X[valid_indices]
        y_train, y_valid = y[train_indices], y[valid_indices]

        print(f"{i}-th fold:")
        show_data(X_train, y_train)
        show_data(X_valid, y_valid)

        model = LogisticRegression()

        start_tm = time.time()
        model.fit(X_train, y_train)
        fit_tm = time.time() - start_tm

        start_tm = time.time()
        score = model.score(X_valid, y_valid)
        score_tm = time.time() - start_tm

        test_scores.append(score)
        fit_times.append(fit_tm)
        score_times.append(score_tm)
    
    return {
        "fit_time": fit_times,
        "score_times": score_times,
        "test_score": test_scores,
    }


def show_result(result: dict):
    for key, value in result.items():
        print(f"{key}: {value}")
    print()


def show_data(X: np.ndarray, y: np.ndarray):
    print(f"X: {X.shape}")
    print(f"y: {y.shape} (0={y.shape[0]-y.sum()}, 1={y.sum()})")


def main():
    n = 5
    X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, weights=(0.2, 0.8))
    groups = np.random.randint(low=0, high=n, size=y.shape)
    show_data(X, y)
    print()

    print("KFold:")
    result = cross_validation(KFold(n_splits=n), X, y)
    show_result(result)

    print("StratifiedKFold:")
    result = cross_validation(StratifiedKFold(n_splits=n), X, y)
    show_result(result)

    print("GroupKFold:")
    result = cross_validation(GroupKFold(n_splits=n), X, y, groups)
    show_result(result)

    print("DONE")


if __name__ == "__main__":
    main()
