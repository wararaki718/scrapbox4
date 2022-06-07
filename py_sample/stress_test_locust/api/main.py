from fastapi import FastAPI


app = FastAPI()

@app.get("/hello")
def hello() -> str:
    return "hello"

@app.get("/world")
def world() -> str:
    return "world"
