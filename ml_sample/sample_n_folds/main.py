from sklearn.datasets import load_diabetes
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import KFold


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target
    print(X.shape)
    print()

    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_model = RidgeCV(cv=cv)
    cv_model.fit(X, y)
    print("cv_model:")
    print(f"best_score_: {cv_model.best_score_}")
    print(f"score      : {cv_model.score(X, y)}")
    print()

    model = RidgeCV()
    model.fit(X, y)
    print("model:")
    print(f"score: {model.score(X, y)}")
    print()

    print("DONE")


if __name__ == "__main__":
    main()
