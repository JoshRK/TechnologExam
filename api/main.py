from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re
from database import collection_vinyles, collection_dvds
from bson import ObjectId
import subprocess
from fastapi.responses import JSONResponse
import os

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

@app.get("/vinyles/{genre}", response_model=List[Musique])
def lister_vinyles_par_genre(genre: str):
    genre = genre.upper()
    if genre not in ["POP", "RAP", "RNB"]:
        raise HTTPException(status_code=400, detail="Genre invalide (choisir POP, RAP ou RNB)")

    results = list(collection_vinyles.find(
        {"immatriculation": {"$regex": f"/{genre}/"}},  # match par genre dans l'immatriculation
        {"_id": 0}
    ))
    return results

@app.post("/debug/tests")
def run_tests_json():
    tests_dir = os.path.join(os.path.dirname(__file__), "tests")
    try:
        result = subprocess.run(
            ["python", "-m", "unittest", "discover", "-s", tests_dir],
            capture_output=True,
            text=True,
            timeout=15
        )


        output = result.stdout + result.stderr

        match = re.search(r"Ran (\d+) tests? in", output)
        total = int(match.group(1)) if match else 0
        failed = len(re.findall(r"FAIL:", output)) + len(re.findall(r"ERROR:", output))
        passed = total - failed

        return JSONResponse({
            "total": total,
            "passed": passed,
            "failed": failed,
            "status": "OK" if failed == 0 else "FAILED",
            "details": output.strip()[-1000:]
        })

    except subprocess.TimeoutExpired:
        return JSONResponse({"error": "Test timeout"}, status_code=500)
