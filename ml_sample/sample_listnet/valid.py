import torch

from listnet import ListNet
from utils import swapped_pairs


def valid(model: ListNet, X_valid: torch.Tensor, y_valid: torch.Tensor) -> int:
    model.eval()
    with torch.no_grad():
        y_pred = model(X_valid)
        n_swapped = swapped_pairs(y_pred, y_valid)
    return n_swapped
