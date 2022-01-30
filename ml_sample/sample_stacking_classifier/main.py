from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC


def main():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    estimators = [
        ("rf", RandomForestClassifier()),
        ("svc", LinearSVC())
    ]

    model = StackingClassifier(estimators=estimators, final_estimator=RidgeClassifier())
    model.fit(X_train, y_train)

    print(f"score: {model.score(X_test, y_test)}")
    print("DONE")


if __name__ == "__main__":
    main()
