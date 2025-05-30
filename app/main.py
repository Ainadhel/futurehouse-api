import os
from fastapi import FastAPI, Header, HTTPException
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

@app.get("/projects")
def list_projects(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")
    return client.projects.list()

@app.get("/projects/{project_id}")
def get_project(project_id: str, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")
    return client.projects.get(project_id)

@app.get("/health")
def healthcheck():
    return {"status": "ok"}
