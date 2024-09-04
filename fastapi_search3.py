from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 2")

@app.get("/search3", tags=["Search The Animals..."])
async def animals_search(animalsname: str, categoryname: str):
    Animals = [
        {"sno": 1, "animals": "Lion", "category": "Land"},
        {"sno": 2, "animals": "Tiger", "category": "Land"},
        {"sno": 3, "animals": "Cheetah", "category": "Land"},
        {"sno": 4, "animals": "Whale", "category": "Water"},
        {"sno": 5, "animals": "Eagle", "category": "Air"}
    ]
    animal_data = [animal for animal in Animals if animalsname.lower() in animal['animals'].lower() and categoryname.lower() in animal['category'].lower()]
    return {"Results": animal_data}