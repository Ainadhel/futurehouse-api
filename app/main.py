import os
from fastapi import FastAPI, Header, HTTPException, Body
from pydantic import BaseModel
from typing import Any, Dict
from futurehouse_client import FutureHouseClient

app = FastAPI()

# Clé API HTTP sécurisée (utilisée dans les headers x-api-key)
API_KEY = os.getenv("API_KEY", "default-api-key")

# Clé API Futurehouse pour authentification SDK
FUTUREHOUSE_API_KEY = os.getenv("FUTUREHOUSE_API_KEY")
if not FUTUREHOUSE_API_KEY:
    raise RuntimeError("La variable d'environnement FUTUREHOUSE_API_KEY est manquante.")

# Création du client FutureHouse
client = FutureHouseClient(api_key=FUTUREHOUSE_API_KEY)

# ---- 🔽 Endpoint générique pour exécuter un job ----

class TaskRequest(BaseModel):
    name: str
    query: str

@app.post("/run-task")
def run_task(data: TaskRequest, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")

    task_data = {
        "name": data.name,   # exemple : "OWL"
        "query": data.query  # exemple : "Has anyone tested..."
    }

    try:
        result = client.tasks.run(task_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---- 🧪 Healthcheck ----

@app.get("/health")
def healthcheck():
    return {"status": "ok"}
