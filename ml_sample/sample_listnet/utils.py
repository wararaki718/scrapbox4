from typing import Tuple
import numpy as np
import torch


def make_dataset(N_train: torch.Tensor, N_valid: torch.Tensor, D: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    ws = torch.randn(D, 1)

    X_train = torch.randn(N_train, D, requires_grad=True)
    X_valid = torch.randn(N_valid, D, requires_grad=True)

    ys_train_score = torch.mm(X_train, ws)
    ys_valid_score = torch.mm(X_valid, ws)

    bins = np.array([-2, -1, 0, 1])
    ys_train_rel = torch.Tensor(
        np.digitize(ys_train_score.clone().detach().numpy(), bins=bins)
    )
    ys_valid_rel = torch.Tensor(
        np.digitize(ys_valid_score.clone().detach().numpy(), bins=bins)
    )

    return X_train.cuda(), X_valid.cuda(), ys_train_rel.cuda(), ys_valid_rel.cuda()


def swapped_pairs(ys_pred: torch.Tensor, ys_target: torch.Tensor) -> torch.Tensor:
    N = ys_target.shape[0]
    swapped = 0

    for i in range(N-1):
        for j in range(i+1, N):
            if ys_target[i] < ys_target[j]:
                if ys_pred[i] > ys_pred[j]:
                    swapped += 1
            elif ys_target[i] > ys_target[j]:
                if ys_pred[i] < ys_pred[j]:
                    swapped += 1
    
    return swapped
