from typing import Tuple

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import torch

from model import LR
from train import train, train_l1, train_l2
from valid import valid


def get_train_test_data(X: np.ndarray, y: np.ndarray) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return torch.Tensor(X_train), torch.Tensor(X_test), torch.Tensor(y_train).long(), torch.Tensor(y_test).long()


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = get_train_test_data(X, y)

    n_features = X.shape[1]
    n_classes = len(set(y))

    model = LR(n_features, n_classes)
    model_l1 = LR(n_features, n_classes)
    model_l2 = LR(n_features, n_classes)
    model_option = LR(n_features, n_classes)

    learning_rate = 0.0001
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    optimizer_l1 = torch.optim.Adam(model_l1.parameters(), lr=learning_rate)
    optimizer_l2 = torch.optim.Adam(model_l2.parameters(), lr=learning_rate)
    optimizer_option = torch.optim.Adam(model_option.parameters(), lr=learning_rate, weight_decay=0.0001)

    for epoch in range(1, 10001):
        model = train(model, optimizer, X_train, y_train)
        model_l1 = train_l1(model_l1, optimizer_l1, X_train, y_train)
        model_l2 = train_l2(model_l2, optimizer_l2, X_train, y_train)
        model_option = train(model_option, optimizer_option, X_train, y_train)

        if epoch % 1000 != 0:
            continue
        print(f"## epoch {epoch:02d}:")
        accuracy = valid(model, X_test, y_test)
        accuracy_l1 = valid(model_l1, X_test, y_test)
        accuracy_l2 = valid(model_l2, X_test, y_test)
        accuracy_option = valid(model_option, X_test, y_test)
        print(f"accuracy           : {accuracy}")
        print(f"accuracy l1        : {accuracy_l1}")
        print(f"accuracy l2        : {accuracy_l2}")
        print(f"accuracy l2(option): {accuracy_option}")
        print(model.linear.weight)
        print(model.linear.bias)
        print("")
    
    print("## sklearn lr:")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print(f"accuracy   : {model.score(X_test, y_test)}")
    print(model.coef_)
    print(model.intercept_)
    print("")
    print("DONE")


if __name__ == "__main__":
    main()
