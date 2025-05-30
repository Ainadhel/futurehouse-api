from fastapi import FastAPI, Header, HTTPException
from futurehouse.client import FuturehouseClient

app = FastAPI()
client = FuturehouseClient()  # Ajuste avec des clés si besoin

import os

API_KEY = os.getenv("API_KEY", "default-api-key")

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