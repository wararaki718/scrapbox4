import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.experimental import enable_halving_search_cv
from sklearn.linear_model import Ridge
from sklearn.model_selection import HalvingGridSearchCV


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    params = {
        "alpha": np.linspace(0.1, 1.0, 5)
    }
    grid_search = HalvingGridSearchCV(Ridge(), params)
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
