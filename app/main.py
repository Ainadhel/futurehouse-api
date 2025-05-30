import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from futurehouse_client.simple import run_task  # ✅ import direct
from futurehouse_client.enums import JobNames

app = FastAPI()

API_KEY = os.getenv("API_KEY", "default-api-key")
FUTUREHOUSE_API_KEY = os.getenv("FUTUREHOUSE_API_KEY")
if not FUTUREHOUSE_API_KEY:
    raise RuntimeError("FUTUREHOUSE_API_KEY manquant")

# ---- Endpoint générique pour lancer un job simple ----

class TaskRequest(BaseModel):
    name: str
    query: str

@app.post("/run-task")
def run_task_endpoint(data: TaskRequest, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")

    try:
        job_enum = JobNames[data.name]
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Nom de tâche invalide : {data.name}")

    try:
        result = run_task(  # ✅ appel direct ici
            api_key=FUTUREHOUSE_API_KEY,
            name=job_enum,
            query=data.query
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def healthcheck():
    return {"status": "ok"}
