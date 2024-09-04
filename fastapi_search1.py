from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 1")

@app.get("/search1", tags=["Searching The Items..."])
async def search_items(name: str):
    Cars = [
        {"id": 1, "make": "Audi", "year": 2020},
        {"id": 2, "make": "BMW", "year": 2021},
        {"id": 3, "make": "Benz", "year": 2022},
        {"id": 4, "make": "Ford", "year": 2023},
        {"id": 5, "make": "Audi", "year": 2024}
    ]
    final_data = [car for car in Cars if name.lower() in car['make'].lower()]
    return {"Result": final_data}