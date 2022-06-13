import logging

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    iris = load_iris()

    X = iris.data
    y = iris.target

    lr = LogisticRegression()
    lr.fit(X, y)
    logger.info("model trained")

    joblib.dump(lr, "batch/models/model.pkl")
    logger.info("model saved.")

    logger.info("DONE")


if __name__ == "__main__":
    main()
