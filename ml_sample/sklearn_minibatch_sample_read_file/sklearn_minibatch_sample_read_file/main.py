from tempfile import NamedTemporaryFile
from typing import Generator

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor

from loader import Loader


def main():
    n_samples = 128
    n_features = 5
    batch_size = 16

    model = SGDRegressor(max_iter=1000)
    with NamedTemporaryFile(mode="wt") as f:
        rng = np.random.RandomState(42)

        y = rng.randn(n_samples, 1)
        X = rng.randn(n_samples, n_features)
        columns = [f"X_{i}" for i in range(n_features)] + ["y"]
        pd.DataFrame(np.hstack([X, y]), columns=columns).to_csv(f.name, index=False)

        filepath = f.name
        loader = Loader(filepath, batch_size)
    
        for (X, y) in loader:
            model.partial_fit(X, y)
        
        y_pred = model.predict(X)
        print(y_pred.shape)
    print("DONE")


if __name__ == "__main__":
    main()
