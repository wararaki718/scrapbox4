import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV


def custom_scoring(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    diff = np.abs(y_true - y_pred).max()
    return np.log1p(diff)


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    params = {
        "alpha": np.linspace(0.1, 1.0, 5)
    }
    grid_search = GridSearchCV(Ridge(), params, scoring=make_scorer(custom_scoring))
    grid_search.fit(X, y)
    
    print(grid_search.best_params_)
    print()

    print(grid_search.best_estimator_)
    print()

    print(grid_search.best_score_)
    print()
    
    print(grid_search.cv_results_)
    
    print("DONE")


if __name__ == "__main__":
    main()
