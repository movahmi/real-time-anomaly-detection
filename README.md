# Real-Time Anomaly Detection Service

## Overview
This service detects anomalies in real-time using a Machine Learning model built with `IsolationForest`. It provides a RESTful API to classify incoming data points.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/movahmi/real-time-anomaly-detection.git
   cd real-time-anomaly-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

Start the FastAPI server:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API Usage

### Endpoint: `/predict`
- **Method**: POST  
- **Request Body**:
  ```json
  {
    "values": [0.1, 0.5, 0.9]
  }
  ```

- **Response**:
  ```json
  {
    "anomaly": false
  }
  ```

## Folder Structure
```
real-time-anomaly-detection/
├── app.py
├── models/
│   └── anomaly_model.pkl  # Generated automatically
├── requirements.txt
└── README.md
```

## License
This project is open-source and free to use.
        