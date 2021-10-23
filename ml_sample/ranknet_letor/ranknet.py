import torch
import torch.nn as nn;


class RankNet(nn.Module):
    def __init__(self, n_input: int, n_output: int=1, n_hidden: int=10) -> None:
        super(RankNet, self).__init__()
        self.linear1 = nn.Linear(n_input, n_hidden)
        self.linear2 = nn.Linear(n_hidden, n_output)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.sigmoid(self.linear1(x))
        x = self.linear2(x)
        return x
