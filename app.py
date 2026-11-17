from fastapi import FastAPI

from calculator import add, multiply

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Calculator API is running"}


@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    return {"result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply(a, b)
    return {"result": result}
