from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import torch

from model import LR
from train import train
from valid import valid


def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LR(X.shape[1], len(set(y)))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(1, 10001):
        model = train(model, optimizer, torch.Tensor(X_train), torch.Tensor(y_train).long())
        if epoch % 1000 != 0:
            continue
        print(f"## epoch {epoch:02d}:")
        valid(model, torch.Tensor(X_test), torch.Tensor(y_test).long())
        print(model.linear.weight)
        print("")
    
    print("## sklearn lr:")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print(f"score: {model.score(X_test, y_test)}")
    
    print("DONE")


if __name__ == "__main__":
    main()
