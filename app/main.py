from fastapi import FastAPI
from pydantic import BaseModel

from burger import Burger
from elevateur_ventes import EvaluateurVentes
    

app = FastAPI()
evaluateur_ventes = EvaluateurVentes(date="2023-06-01")

class BurgerCreateRequest(BaseModel):
    prix: float
    description: str
    allergenes: list[str]
    cuisson: str
    scoville: int

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API des burgers !"}

@app.post("/burgers")
def creer_burger(burger_request: BurgerCreateRequest):
    burger = Burger(
        prix=burger_request.prix,
        description=burger_request.description,
        allergenes=burger_request.allergenes,
        cuisson=burger_request.cuisson,
        scoville=burger_request.scoville
    )
    evaluateur_ventes.ajouter_burger(burger)
    return {"message": "Burger créé avec succès !"}

@app.get("/burgers/nombre-ventes")
def evaluer_nombre_ventes():
    return {"nombre_ventes": evaluateur_ventes.evaluer_nombre_burgers_vendus()}

@app.get("/burgers/prix-total")
def evaluer_prix_total():
    return {"prix_total": evaluateur_ventes.evaluer_prix_total_ventes()}

@app.get("/burgers/allergenes-journee")
def evaluer_allergenes_journee():
    return {"allergenes_journee": evaluateur_ventes.evaluer_allergenes_journee()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8763)
