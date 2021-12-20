from collections import defaultdict
from typing import Tuple

import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from loss import IBLoss
from model import NNModel
from utils import try_gpu


def train(model: NNModel, train_loader: DataLoader, class_names: Tuple[str], n_epochs: int=2) -> NNModel:
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    train_image_counts = defaultdict(int)
    model.train()
    for epoch in range(1, n_epochs+1):
        running_loss = 0.0
        for i, data in enumerate(train_loader, 1):
            inputs, labels = data

            optimizer.zero_grad()

            outputs, _ = model(try_gpu(inputs))
            loss = criterion(outputs, try_gpu(labels))
            loss.backward()

            optimizer.step()

            running_loss += loss.item()
            if i % 2000 == 0:
                print(f"[{epoch}, {i}] loss: {running_loss/2000:.3f}")
                running_loss = 0.0
            
            for label in labels:
                train_image_counts[class_names[label]] += 1
    
    print()
    for name, total in train_image_counts.items():
        print(f"{name}: {total}")
    
    return model


def train_ibloss(model: NNModel, train_loader: DataLoader, class_names: Tuple[str], n_epochs: int=2) -> NNModel:
    criterion = IBLoss(len(class_names))
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    train_image_counts = defaultdict(int)
    model.train()
    for epoch in range(1, n_epochs+1):
        running_loss = 0.0
        for i, data in enumerate(train_loader, 1):
            inputs, labels = data
            inputs = try_gpu(inputs)
            labels = try_gpu(labels)

            optimizer.zero_grad()

            outputs, features = model(inputs)
            loss = criterion(outputs, labels, features)
            loss.backward()

            optimizer.step()

            running_loss += loss.item()
            if i % 2000 == 0:
                print(f"[{epoch}, {i}] loss: {running_loss/2000:.3f}")
                running_loss = 0.0
            
            for label in labels:
                train_image_counts[class_names[label]] += 1
    
    print()
    for name, total in train_image_counts.items():
        print(f"{name}: {total}")
    
    return model
