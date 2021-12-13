import torch
from sklearn.metrics import mean_squared_error

from model import NNRegressor


def valid(model: NNRegressor, X: torch.Tensor, y_true: torch.Tensor) -> float:
    model.eval()
    with torch.no_grad():
        y_pred = model(X)
        score = mean_squared_error(
            y_true.detach().cpu().numpy(),
            y_pred.detach().cpu().numpy()
        )
        
    return score
