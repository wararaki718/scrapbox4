import torch

from model import LR


def train(model: LR, optimizer: torch.optim.Optimizer, X: torch.Tensor, y: torch.Tensor) -> LR:
    model.train()
    criterion = torch.nn.CrossEntropyLoss()

    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)

    loss.backward()
    optimizer.step()

    return model
