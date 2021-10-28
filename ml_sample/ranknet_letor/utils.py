from typing import Union

import torch

from ranknet import RankNet


def try_gpu(x: Union[torch.Tensor, RankNet]) -> Union[torch.Tensor, RankNet]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x
