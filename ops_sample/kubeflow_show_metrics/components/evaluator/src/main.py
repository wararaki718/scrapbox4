import json
import random
from argparse import ArgumentParser, Namespace


def get_parser() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--metricspath", type=str)

    return parser.parse_args()


def main():
    parser = get_parser()

    accuracy = random.random()
    precision = random.random()
    recall = random.random()
    
    metrics = {
        "metrics": [
            {"name": "accuracy-score", "numberValue": accuracy, "format": "PERCENTAGE"},
            {"name": "precision-score", "numberValue": precision, "format": "PERCENTAGE"},
            {"name": "recall-score", "numberValue": recall, "format": "PERCENTAGE"},
        ]
    }

    with open(parser.metricspath, "w") as f:
        json.dump(metrics, f)
