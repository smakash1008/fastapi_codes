from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="MY APPLICATION 2")

class Animals(BaseModel):
    sno: int
    name: str
    category: str
    count: int

@app.post("/animals/", tags=["Animals Details"])
async def animals_details(animal: Animals):
    return f"The Animal name is {animal.name} and the animal category is {animal.category} and the number of animals present is {animal.count}..."