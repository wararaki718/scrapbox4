import json
from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--graphpath", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()

    iris = load_iris()
    X = iris.data
    y = iris.target
    labels = iris.target_names.tolist()

    model = LogisticRegression()
    model.fit(X, y)

    y_pred = model.predict(X)
    result = confusion_matrix(y, y_pred)
    data = []
    for target_index, row in enumerate(result):
        for predict_index, value in enumerate(row):
            data.append((labels[target_index], labels[predict_index], value))

    df = pd.DataFrame(data, columns=["target", "predicted", "count"])
    source = df.to_csv(None, header=False, index=False)
    metadata = {
        "outputs": [{
            "type": "confusion_matrix",
            "format": "csv",
            "schema": [
                {"name": "target", "type": "CATEGORY"},
                {"name": "predicted", "type": "CATEGORY"},
                {"name": "count", "type": "NUMBER"}
            ],
            "source": source,
            "storage": "inline",
            "labels": labels
        }]
    }
    args.graphpath.parent.mkdir(parents=True, exist_ok=True)
    args.graphpath.write_text(json.dumps(metadata))

    print("DONE")


if __name__ == "__main__":
    main()
