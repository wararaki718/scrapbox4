from sklearn.metrics import accuracy_score
import torch

from model import LR

def valid(model: LR, X: torch.Tensor, y: torch.Tensor):
    model.eval()
    with torch.no_grad():
        y_pred = model(X)
        _, y_labels = torch.max(y_pred, 1)

        accuracy = accuracy_score(y.detach().numpy(), y_labels.detach().numpy())
        print(f"accuracy: {accuracy}")
