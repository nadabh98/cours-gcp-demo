from fastapi import FastAPI
import os
from sqlalchemy import text
from database import engine

app = FastAPI()
@app.get("/")
def racine():
 return {"message": "API FastAPI en ligne sur Cloud Run"}
@app.get("/sante")
def sante():
 return {"status": "ok"}

@app.get("/etudiants")
def liste_etudiants():
 with engine.connect() as conn:
    resultat = conn.execute(text("SELECT NOW()"))
    return {"heure_serveur": str(resultat.scalar())}
