

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World 3"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}