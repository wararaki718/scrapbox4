from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


def ib_loss(x: torch.Tensor, ib: torch.Tensor) -> torch.Tensor:
    loss = x * ib
    return loss.mean()


class IBLoss(nn.Module):
    def __init__(self, num_classes: int, weight: Optional[torch.Tensor]=None, alpha: float=10000., epsilon: float=0.001):
        super(IBLoss, self).__init__()

        self.alpha = alpha
        self.epsilon = epsilon
        self.weight = weight
        self.num_classes = num_classes

    def forward(self, input: torch.Tensor, target: torch.Tensor, features: torch.Tensor) -> torch.Tensor:
        grads = torch.sum(torch.abs(F.softmax(input, dim=1) - F.one_hot(target, self.num_classes)),1) # N * 1
        ib = grads*features.reshape(-1)
        ib = self.alpha / (ib + self.epsilon)
        return ib_loss(F.cross_entropy(input, target, reduction='none', weight=self.weight), ib)
