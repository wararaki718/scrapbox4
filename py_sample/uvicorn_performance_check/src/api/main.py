from fastapi import FastAPI

from .estimator import IrisEstimator
from .schema import IrisRequest, IrisResponse


app = FastAPI()
estimator = IrisEstimator("api/models/model.pkl")


@app.get("/ping")
def ping() -> str:
    return "ping"

@app.post("/predict", response_model=IrisResponse)
def predict(request: IrisRequest) -> IrisResponse:
    label = estimator.estimate(request)
    return IrisResponse(iris_class=label)
