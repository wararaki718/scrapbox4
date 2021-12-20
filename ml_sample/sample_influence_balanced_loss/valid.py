from typing import Dict, Tuple

import torch
from torch.utils.data import DataLoader

from model import NNModel
from utils import try_gpu


def valid(model: NNModel, test_loader: DataLoader) -> float:
    correct = 0
    total = 0

    model.eval()
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            images = try_gpu(images)
            labels = try_gpu(labels)

            outputs, _ = model(images)

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    print(f"accuracy ({total} images): {correct/total}")

    return correct / total


def valid_each_class(model: NNModel, test_loader: DataLoader, class_names: Tuple[str]) -> Dict[str, float]:
    correct_preds = {name: 0 for name in class_names}
    total_preds = {name: 0 for name in class_names}

    model.eval()
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            images = try_gpu(images)
            labels = try_gpu(labels)
            outputs, _ = model(images)

            _, predictions = torch.max(outputs.data, 1)
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_preds[class_names[label]] += 1
                total_preds[class_names[label]] += 1
    
    accuracies = {}
    for name, correct in correct_preds.items():
        total = total_preds[name]
        accuracy = float(correct) / total
        print(f"accuracy ({name}, {total} images): {accuracy}")
        accuracies[name] = accuracy
    
    return accuracies
