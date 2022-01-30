from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR


def main():
    X, y = load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    estimators = [
        ("rf", RandomForestRegressor()),
        ("svm", LinearSVR())
    ]
    model = StackingRegressor(estimators=estimators, final_estimator=Ridge())
    model.fit(X_train, y_train)

    print(f"score: {model.score(X_test, y_test)}")
    print("DONE")


if __name__ == "__main__":
    main()
