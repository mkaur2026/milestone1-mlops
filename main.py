from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class Request(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Response(BaseModel):
    prediction: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=Response)
def predict(data: Request):
    x = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    pred = model.predict(x)[0]
    return {"prediction": int(pred)}