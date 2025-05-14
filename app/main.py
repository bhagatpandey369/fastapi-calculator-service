from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.calculator import add, subtract, multiply, divide

import os


class CalculationRequest(BaseModel):
    a: float
    b: float


app = FastAPI()
PORT = os.getenv("PORT", 8000)


@app.post("/add")
def calculate_add(req: CalculationRequest):
    return {"result": add(req.a, req.b)}


@app.post("/subtract")
def calculate_subtract(req: CalculationRequest):
    return {"result": subtract(req.a, req.b)}


@app.post("/multiply")
def calculate_multiply(req: CalculationRequest):
    return {"result": multiply(req.a, req.b)}


@app.post("/divide")
def calculate_divide(req: CalculationRequest):
    try:
        result = divide(req.a, req.b)
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
