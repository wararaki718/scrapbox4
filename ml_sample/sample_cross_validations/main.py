import time

import numpy as np
from sklearn.base import BaseEstimator, clone
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import cross_validate, KFold


def crossvalid(model: BaseEstimator, X: np.ndarray, y: np.ndarray, cv: int=3) -> dict:
    result = cross_validate(model, X, y, cv=cv)
    return result


def kfold(model: BaseEstimator, X: np.ndarray, y: np.ndarray, cv: int=3) -> dict:
    kf = KFold(n_splits=cv)
    test_scores = []
    fit_times = []
    score_times = []
    for train_indices, valid_indices in kf.split(X):
        X_train, X_valid = X[train_indices], X[valid_indices]
        y_train, y_valid = y[train_indices], y[valid_indices]
        clone_model = clone(model)

        start_tm = time.time()
        clone_model.fit(X_train, y_train)
        fit_tm = time.time() - start_tm

        start_tm = time.time()
        score = clone_model.score(X_valid, y_valid)
        score_tm = time.time() - start_tm

        test_scores.append(score)
        fit_times.append(fit_tm)
        score_times.append(score_tm)
    
    return {
        "fit_time": fit_times,
        "score_times": score_times,
        "test_score": test_scores,
    }


def show(model_name: str, result: dict):
    print(f"## {model_name}")
    for key, value in result.items():
        print(f"{key}: {value}")
    print()


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    ridge_model = Ridge()
    lasso_model = Lasso()

    result = crossvalid(ridge_model, X, y)
    show("ridge+crossvalid", result)
    
    result = crossvalid(lasso_model, X, y)
    show("lasso+crossvalid", result)

    result = kfold(ridge_model, X, y)
    show("ridge+kfold", result)

    result = kfold(lasso_model, X, y)
    show("lasso+kfold", result)

    print("DONE")


if __name__ == "__main__":
    main()
    