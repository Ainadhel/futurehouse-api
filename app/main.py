import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from futurehouse_client.tasks import run_task

app = FastAPI()

# Clé API HTTP sécurisée
API_KEY = os.getenv("API_KEY", "default-api-key")

# Clé API Futurehouse
FUTUREHOUSE_API_KEY = os.getenv("FUTUREHOUSE_API_KEY")
if not FUTUREHOUSE_API_KEY:
    raise RuntimeError("FUTUREHOUSE_API_KEY manquant")

# ----- Endpoint générique de tâche -----

class TaskRequest(BaseModel):
    name: str
    query: str

@app.post("/run-task")
def run_task_endpoint(data: TaskRequest, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")

    try:
        result = run_task(
            api_key=FUTUREHOUSE_API_KEY,
            name=data.name,
            query=data.query
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----- Healthcheck -----

@app.get("/health")
def healthcheck():
    return {"status": "ok"}
