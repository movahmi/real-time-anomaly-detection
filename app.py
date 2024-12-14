from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

app = FastAPI()

class DataPoint(BaseModel):
    values: list[float]

MODEL_PATH = "models/anomaly_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    default_data = np.random.rand(100, 3)
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(default_data)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

@app.post("/predict")
def predict_anomaly(data: DataPoint):
    try:
        input_array = np.array([data.values])
        prediction = model.predict(input_array)
        return {"anomaly": prediction[0] == -1}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing data: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Real-Time Anomaly Detection Service is running!"}
        