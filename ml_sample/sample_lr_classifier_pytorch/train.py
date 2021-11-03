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


def train_l1(model: LR, optimizer: torch.optim.Optimizer, X: torch.Tensor, y: torch.Tensor, alpha: float=0.15) -> LR:
    model.train()
    criterion = torch.nn.CrossEntropyLoss()

    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)

    l1_norm = sum(w.abs().sum() for w in model.parameters())
    loss = loss + alpha * l1_norm

    loss.backward()
    optimizer.step()

    return model


def train_l2(model: LR, optimizer: torch.optim.Optimizer, X: torch.Tensor, y: torch.Tensor, alpha: float=0.0001) -> LR:
    model.train()
    criterion = torch.nn.CrossEntropyLoss()

    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)

    l2_norm = sum(w.pow(2.0).sum() for w in model.parameters())
    loss = loss + alpha * l2_norm

    loss.backward()
    optimizer.step()

    return model
