from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="MY APPLICATION 3")

class Cars(BaseModel):
    id: int
    make: str
    color: str
    year: int

car_data = {}

@app.post("/cars/", tags=["Car Details"])
async def car_details_post(car: Cars):
    car_data[car.id] = car
    return car_data