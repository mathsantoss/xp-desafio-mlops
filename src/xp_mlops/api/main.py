from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
# from kedro.framework.context import load_context
from kedro.framework.context import KedroContext
from typing import Any, Iterable
from kedro.framework.session import KedroSession
import pathlib
import joblib



model = joblib.load('notebooks/model.pkl')


app = FastAPI()

class Features(BaseModel):
    feature_0: float
    feature_1: float
    feature_2: float
    feature_3: float
    feature_4: float
    feature_5: float
    feature_6: float
    feature_7: float
    feature_8: float
    feature_9: float
    feature_10: float
    feature_11: float
    feature_12: float

@app.get("/api/health")
def health():
    return {"status": "Estou saudavel"}

@app.post("/api/predict")
def predict(features: Features):
    data = np.array([[features.feature_0, features.feature_1, features.feature_2, features.feature_3,
                      features.feature_4, features.feature_5, features.feature_6, features.feature_7,
                      features.feature_8, features.feature_9, features.feature_10, features.feature_11,
                      features.feature_12]])
    
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
