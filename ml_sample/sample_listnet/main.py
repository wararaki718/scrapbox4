import torch

from config import Config
from listnet import ListNet
from utils import make_dataset

from train import train
from valid import valid


def main():
    config = Config.load("config.yml")

    X_train, X_valid, y_train, y_valid = make_dataset(config.n_train, config.n_valid, config.n_input)
    print(X_train.shape)
    print(y_train.shape)
    print(X_valid.shape)
    print(y_valid.shape)

    model = ListNet(config.n_input).cuda()
    optimizer = torch.optim.Adam(model.parameters())
    for epoch in range(1, config.n_epochs+1):
        model = train(model, optimizer, X_train, y_train, config.batch_size)
        n_swapped = valid(model, X_valid, y_valid)
        print(f"epoch {epoch:2d}: {n_swapped} swapped.")
    print("DONE")


if __name__ == "__main__":
    main()
