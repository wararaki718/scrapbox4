from typing import Union

import torch

from listnet import ListNet


def try_gpu(x: Union[torch.Tensor, ListNet]) -> Union[torch.Tensor, ListNet]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x
