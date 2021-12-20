from typing import Optional, Tuple

import numpy as np
import torch
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader, WeightedRandomSampler


def _create_loader(is_train: bool, batch_size: int=4, transform: Optional[transforms.Compose]=None, use_sampler: bool=False) -> DataLoader:
    dataset = CIFAR10(
        root="./data",
        train=is_train,
        download=True,
        transform=transform
    )
    if use_sampler:
        target = dataset.targets
        class_sample_count = np.unique(target, return_counts=True)[1]
        print(class_sample_count)
        class_sample_count[0] = 2500
        print(class_sample_count)

        weight = 1. / class_sample_count
        samples_weight = weight[target]
        samples_weight = torch.from_numpy(samples_weight)
        sampler = WeightedRandomSampler(samples_weight, len(samples_weight))
        is_shuffle = False
    else:
        sampler = None
        is_shuffle = True

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=is_shuffle,
        sampler=sampler,
        num_workers=2
    )

def get_cifer_loaders(batch_size: int=4) -> Tuple[DataLoader, DataLoader, Tuple[str]]:
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    train_loader = _create_loader(is_train=True, batch_size=batch_size, transform=transform, use_sampler=True)
    test_loader = _create_loader(is_train=False, batch_size=batch_size, transform=transform)

    class_names = (
        "plain",
        "car",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck"
    )

    return train_loader, test_loader, class_names
