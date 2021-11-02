import torch
import torch.nn as nn


class LR(nn.Module):
    def __init__(self, n_input: int, n_output: int):
        super(LR, self).__init__()
        self.linear = nn.Linear(n_input, n_output)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(self.linear(x))
