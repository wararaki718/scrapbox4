from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    # gird search
    gs_params = {
        "alpha": [0.1, 0.5, 1.0, 1.5, 2.0]
    }
    gs_estimator = GridSearchCV(Ridge(), gs_params)
    gs_estimator.fit(X, y)
    print(gs_estimator.best_params_)

    # randomized search
    rs_params = {
        "alpha": [0.1, 0.5, 1.0, 1.5, 2.0]
    }
    rs_estimator = RandomizedSearchCV(Ridge(), rs_params)
    rs_estimator.fit(X, y)
    print(rs_estimator.best_params_)

    print("DONE")


if __name__ == "__main__":
    main()
