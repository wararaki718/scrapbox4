from sklearn.datasets import load_diabetes, load_iris
from sklearn.linear_model import Ridge, RidgeClassifier
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split


def run_classifier():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )
    print("# classifier dataset")
    print(f"X_train: {X_train.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"X_test : {X_test.shape}")
    print(f"y_test : {y_test.shape}")
    print("")

    model = RidgeClassifier()
    model.fit(X_train, y_train)

    print("# classifier evaluation")
    y_pred = model.predict(X_test)
    print(f"accuracy: {accuracy_score(y_test, y_pred)}")
    print("")


def run_regression():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )
    print("# regressor dataset")
    print(f"X_train: {X_train.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"X_test : {X_test.shape}")
    print(f"y_test : {y_test.shape}")
    print("")

    model = Ridge()
    model.fit(X_train, y_train)

    print("# regressor evaluation")
    y_pred = model.predict(X_test)
    print(f"mse: {mean_squared_error(y_test, y_pred)}")
    print("")


def main():
    run_classifier()
    run_regression()

    print("DONE")


if __name__ == "__main__":
    main()
