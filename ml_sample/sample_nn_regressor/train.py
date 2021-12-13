import torch

from model import NNRegressor


def train(model: NNRegressor, optimizer: torch.optim.Optimizer, X: torch.Tensor, y: torch.Tensor) -> NNRegressor:
    model.train()
    criterion = torch.nn.MSELoss()

    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)

    loss.backward()
    optimizer.step()

    return model
