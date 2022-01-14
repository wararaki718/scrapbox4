from tempfile import NamedTemporaryFile

import pandas as pd
from sklearn.datasets import load_iris

from loader import DataLoader


def main():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    print("chunking:")
    with NamedTemporaryFile(mode="wt") as f:
        df.to_csv(f, index=False)
        f.seek(0)

        loader = DataLoader(f.name)
        for batch in loader:
            print(batch.shape)
    print()

    print("DONE")


if __name__ == "__main__":
    main()
