import torch

from model import LR


def valid(model: LR, X: torch.Tensor, y: torch.Tensor) -> float:
    model.eval()
    with torch.no_grad():
        y_pred = model(X)
        _, y_labels = y_pred.max(1)
        correct = y_labels.eq(y).sum().item()

    return correct / y.size(0)
