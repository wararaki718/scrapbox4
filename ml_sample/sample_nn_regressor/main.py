from typing import Tuple

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import torch

from model import NNRegressor
from train import train
from valid import valid


def get_train_test_data(X: np.ndarray, y: np.ndarray) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return torch.Tensor(X_train), torch.Tensor(X_test), torch.Tensor(y_train), torch.Tensor(y_test)


def main():
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    X_train, X_test, y_train, y_test = get_train_test_data(X, y)
    n_features = X.shape[1]

    model = NNRegressor(n_features, 1)

    learning_rate = 0.0001
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(1, 10001):
        model = train(model, optimizer, X_train, y_train)

        if epoch % 1000 != 0:
            continue
        print(f"## epoch {epoch:02d}:")
        mse_score = valid(model, X_test, y_test)
        print(f"r2 score: {mse_score}")
        print("")

    print("DONE")


if __name__ == "__main__":
    main()
