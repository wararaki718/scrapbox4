import joblib

import numpy as np
from .schema import IrisRequest


class IrisEstimator:
    def __init__(self, model_path: str):
        self._model = joblib.load(model_path)
        self._rename_map = ["setora", "versicolor", "virginica"]
    
    def estimate(self, iris: IrisRequest) -> str:
        x = np.array([[
            iris.sepal_length,
            iris.sepal_width,
            iris.petal_length,
            iris.petal_width
        ]])
        y_pred = self._model.predict(x)
        label = self._rename_map[y_pred[0]]
        return label
