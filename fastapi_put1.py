# FastAPI PUT - Update The Data.

from fastapi import FastAPI, HTTPException
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

@app.get("/cars/{car_id}", tags=["Car Data Retrieval"])
async def get_car_details(car_id: int):
    if car_id not in car_data:
        raise HTTPException(status_code=404,detail="Item Not Found")
    car_detail = car_data.get(car_id)
    return car_detail

@app.put("/cars/{car_id}", tags=["Update The Car Data"])
async def update_car_data(car_id: int, updatedcardetails: Cars):
    car_data[car_id] = updatedcardetails
    return car_data
