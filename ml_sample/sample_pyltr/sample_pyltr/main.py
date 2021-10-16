import warnings
from typing import Tuple

import numpy as np
from pyltr.data.letor import read_dataset
from pyltr.metrics import NDCG
from pyltr.models import LambdaMART
from pyltr.models.monitors import ValidationMonitor


warnings.simplefilter("ignore", FutureWarning)


def load(filepath: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    with open(filepath) as f:
        X, y, qids, _ = read_dataset(f)
    return X, y, qids


def main():
    train_path = "dataset/MQ2008/Fold1/train.txt"
    test_path = "dataset/MQ2008/Fold1/test.txt"
    valid_path = "dataset/MQ2008/Fold1/vali.txt"

    X_train, y_train, qid_train = load(train_path)
    X_test, y_test, qid_test = load(test_path)
    X_valid, y_valid, qid_valid = load(valid_path)
    print("data are loaded.")
    
    metric = NDCG(k=10)
    monitor = ValidationMonitor(X_valid, y_valid, qid_valid, metric=metric, stop_after=30)

    model = LambdaMART(
         metric=metric,
        n_estimators=1000,
        learning_rate=0.02,
        max_features=0.5,
        query_subsample=0.5,
        max_leaf_nodes=10,
        min_samples_leaf=64,
        verbose=1,
    )
    model.fit(X_train, y_train, qid_train, monitor=monitor)
    print("finish to train the model")
    
    y_pred = model.predict(X_test)

    y_random = metric.calc_mean_random(qid_test, y_test)
    print(f"random: {y_random}")
    print(f"model : {metric.calc_mean(qid_test, y_test, y_pred)}")

    print("DONE")


if __name__ == "__main__":
    main()
