from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re
from database import collection_vinyles, collection_dvds
from bson import ObjectId

app = FastAPI()

class Musique(BaseModel):
    titre: str
    artiste: str
    immatriculation: str

def immatriculation_valide(musique: Musique) -> bool:
    pattern = r"^([A-Z]{2})/(\d{3})/(RAP|POP|RNB)/(\d{4})$"
    match = re.match(pattern, musique.immatriculation)
    if not match:
        return False
    initiales, duree, genre, identifiant = match.groups()
    if initiales != ''.join([n[0].upper() for n in musique.artiste.split()[:2]]):
        return False
    if not (60 < int(duree) < 300):
        return False
    if "6" in identifiant:
        return False
    return True

@app.post("/vinyles")
def ajouter_vinyle(musique: Musique):
    if not immatriculation_valide(musique):
        raise HTTPException(status_code=400, detail="Immatriculation invalide")
    collection_vinyles.insert_one(musique.dict())
    return {"message": "Ajouté en base MongoDB"}

@app.get("/vinyles", response_model=List[Musique])
def lister_vinyles():
    results = list(collection_vinyles.find({}, {'_id': 0}))
    return results

@app.get("/dvds", response_model=List[Musique])
def lister_cds():
    results = list(collection_dvds.find({}, {'_id': 0}))
    return results