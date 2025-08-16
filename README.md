
# 🚀 God Mode Stack - All In One Python Monolith

<img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python" />
<img src="https://img.shields.io/badge/FastAPI-API-green" alt="FastAPI" />
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red" alt="Streamlit" />
<img src="https://img.shields.io/badge/Redis-Cache-critical" alt="Redis" />
<img src="https://img.shields.io/badge/PostgreSQL-Data-important" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/MongoDB-Logs-success" alt="MongoDB" />

---

## 🌟 What is this?

**everything you need for a data-driven API + AI backend + real-time dashboard in a single Python file.**

✅ FastAPI for REST & WebSocket  
✅ AsyncIO + APScheduler for background tasks  
✅ Scikit-learn ML for predictions (swap in TensorFlow / PyTorch anytime)  
✅ Redis for blazing-fast counters  
✅ PostgreSQL for structured logs  
✅ MongoDB for flexible event logging  
✅ HTTPX for external API calls  
✅ Streamlit for a live dashboard

> 🚀 **Single monolithic `main.py` file.**  
> Copy, run, done. Extreme power, zero boilerplate.

---

## ⚙️ Tech Stack Overview

| Layer           | Tech / Lib               | Description                          |
|-----------------|--------------------------|--------------------------------------|
| 🖥️ API          | **FastAPI**              | HTTP API & WebSocket endpoints       |
| 🔄 Async Tasks  | **asyncio + APScheduler**| Schedule periodic jobs               |
| 🧠 ML           | **scikit-learn**         | Toy model (replace w/ TF or Torch)   |
| ⚡ Cache        | **Redis**                | Real-time counters                   |
| 🗄️ SQL Data    | **PostgreSQL**           | Store structured predictions         |
| 📂 NoSQL Logs  | **MongoDB**              | Store JSON events / logs             |
| 🌐 Ext. APIs   | **HTTPX**                | External HTTP integrations           |
| 📊 Dashboard   | **Streamlit**            | Real-time dashboard UI               |

---

## 🚀 Quickstart

### ⚡ 1. Clone and Install

```bash
git clone https://github.com/umutkayash/ecommercerealtime
cd ecommercerealtime
````

Or manually:

```bash
pip install fastapi uvicorn[standard] numpy scikit-learn redis psycopg2-binary pymongo apscheduler httpx streamlit
```

---

### 🗄️ 2. Make sure your infra is up

* **Redis** (default `localhost:6379`)
* **PostgreSQL** (default `localhost:5432`)

  ```sql
  CREATE DATABASE testdb;
  \c testdb
  CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    feature1 INT,
    feature2 INT,
    prediction INT
  );
  ```
* **MongoDB** (default `localhost:27017`)

---

### 🚀 3. Run it

```bash
python main.py
```

* **FastAPI:** `http://localhost:8000`
* **Streamlit dashboard:** `http://localhost:8501`

---

## 🛠️ Usage

### 📬 REST API

* **Root:**
  `GET /`
  ➡ Returns JSON greeting, logs to MongoDB

* **Prediction:**
  `GET /predict/?f1=1&f2=0`
  ➡ Runs ML model, stores in Redis + Postgres + Mongo

### 🔌 WebSocket

Connect to:
`ws://localhost:8000/ws`

Send:

```
1,0
```

Receives prediction in real time.

### 🧭 Dashboard

Visit `http://localhost`

* See Redis counters for HTTP & WS predictions
* View MongoDB logs
* Tiny line charts updating

---

## 🔥 Features

* ✅ **Monolithic design** — one file to rule them all
* ✅ Realtime API + ML inference
* ✅ Background tasks (calls external API every 10s, logs results)
* ✅ Observability: all API hits logged to MongoDB
* ✅ Realtime counters with Redis
* ✅ Full historical log in PostgreSQL
* ✅ Streamlit dashboard

---

## 🎯 Future

* 🔐 JWT / OAuth2 authentication
* 📈 Swap sklearn with TensorFlow / PyTorch
* 🚀 Docker Compose with Redis, Postgres, Mongo
* 🕵️ Prometheus + Grafana metrics
* 🔥 Webhooks for external notifications
* 🎥 Use Sora (OpenAI video) to visualize workflows 😄

---

## 🏆 License

MIT — go build your empire.
