from fastapi import FastAPI

from .module import plus

app = FastAPI()


@app.get("/ping")
def ping():
    return f"ping {plus(1, 1)}"
