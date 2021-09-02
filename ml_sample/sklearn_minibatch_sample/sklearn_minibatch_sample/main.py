import numpy as np
from numpy.random import f
from sklearn.linear_model import SGDRegressor


def init_mini_batch(X: np.ndarray, y: np.ndarray, chunksize: int) -> tuple:
    start = 0
    while start < X.shape[0]:
        X_batch = X[start: start+chunksize, :]
        y_batch = y[start: start+chunksize]
        yield X_batch, y_batch
        start += chunksize


def main():
    n_samples = 128
    n_features = 5
    rng = np.random.RandomState(42)

    y = rng.randn(n_samples)
    X = rng.randn(n_samples, n_features)

    batch_size = 16
    model = SGDRegressor(max_iter=1000)
    
    batch_iter = init_mini_batch(X, y, batch_size)
    for X_batch, y_batch in batch_iter:
        model.partial_fit(X_batch, y_batch)
    
    y_pred = model.predict(X)
    print(y_pred.shape)
    print("DONE")


if __name__ == "__main__":
    main()
