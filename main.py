"""
- FastAPI: HTTP API & WebSocket
- AsyncIO & APScheduler: background tasks
- Redis: fast cache / counter
- PostgreSQL: structured logs
- MongoDB: unstructured logs
- Scikit-Learn: toy ML (replaceable with TensorFlow/PyTorch)
- HTTPX: external calls
- Streamlit: dashboard
"""
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import uvicorn

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import httpx

import numpy as np
from sklearn.linear_model import LogisticRegression

import redis
import psycopg2
import pymongo

import streamlit as st
import threading
import time
from datetime import datetime

# ===============================
# Database connections
# ===============================
# Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# PostgreSQL
pg_conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="postgres",
    host="localhost"
)
pg_cursor = pg_conn.cursor()

# MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["godmode"]
mongo_logs = mongo_db["logs"]

# ===============================
# Machine learning
# ===============================
X_train = np.array([[0,1],[1,1],[1,0],[0,0]])
y_train = np.array([1,1,0,0])

ml_model = LogisticRegression()
ml_model.fit(X_train, y_train)

# ===============================
# FastAPI setup
# ===============================
app = FastAPI()

@app.get("/")
async def root():
    msg = f"God Mode Stack API — {datetime.now()}"
    # Store event in MongoDB
    mongo_logs.insert_one({"event": "root_call", "timestamp": datetime.now()})
    return JSONResponse({"message": msg})

@app.get("/predict/")
async def predict_api(f1: int, f2: int):
    pred = ml_model.predict([[f1, f2]])[0]
    # Increment Redis counter
    r.incr("http_predictions")
    # Store in PostgreSQL
    pg_cursor.execute(
        "INSERT INTO predictions (feature1, feature2, prediction) VALUES (%s, %s, %s)",
        (f1, f2, int(pred))
    )
    pg_conn.commit()
    # Also in MongoDB
    mongo_logs.insert_one({"endpoint": "/predict", "data": [f1, f2], "prediction": int(pred)})
    return {"prediction": int(pred)}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        nums = [int(x) for x in data.split(",")]
        pred = ml_model.predict([nums])[0]
        # Increment Redis counter
        r.incr("ws_predictions")
        # Store in PostgreSQL
        pg_cursor.execute(
            "INSERT INTO predictions (feature1, feature2, prediction) VALUES (%s, %s, %s)",
            (nums[0], nums[1], int(pred))
        )
        pg_conn.commit()
        await ws.send_text(f"Prediction: {int(pred)}")

# ===============================
# Background scheduler
# ===============================
scheduler = AsyncIOScheduler()

@scheduler.scheduled_job("interval", seconds=10)
async def periodic_http_call():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://httpbin.org/get")
        print(f"[{datetime.now()}] Periodic call: status {resp.status_code}")
        # Log to MongoDB
        mongo_logs.insert_one({
            "type": "periodic_http_call",
            "status": resp.status_code,
            "time": datetime.now()
        })

scheduler.start()

# ===============================
# Streamlit dashboard
# ===============================
def run_streamlit():
    while True:
        st.title("God Mode Dashboard")
        col1, col2 = st.columns(2)

        http_preds = r.get("http_predictions")
        ws_preds = r.get("ws_predictions")
        http_preds = int(http_preds) if http_preds else 0
        ws_preds = int(ws_preds) if ws_preds else 0

        col1.metric("HTTP Predictions", http_preds)
        col2.metric("WebSocket Predictions", ws_preds)

        st.write("### Redis counters over time (fake example)")
        counts = [http_preds, ws_preds, http_preds+ws_preds]
        st.line_chart(counts)

        st.write("### MongoDB last logs")
        last_logs = list(mongo_logs.find().sort([('_id', -1)]).limit(5))
        for log in last_logs:
            st.json({k:str(v) for k,v in log.items()})
        
        time.sleep(5)

# ===============================
# Run everything together
# ===============================
if __name__ == "__main__":
    # Run Streamlit on a separate thread
    t = threading.Thread(target=lambda: st._run_script(run_streamlit))
    t.start()

    # Run FastAPI (async)
    uvicorn.run(app, host="0.0.0.0", port=8000)
