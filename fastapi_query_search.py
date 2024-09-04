from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 2")

fruits = [
    {"id": 1, "name": "apple"},
    {"id": 2, "name": "orange"},
    {"id": 3, "name": "mango"},
    {"id": 4, "name": "grapes"},
    {"id": 5, "name": "strawberry"}
]

@app.get("/search", tags=["Search The Item."])
async def search_items(name: str):
    result = [fruit for fruit in fruits if name.lower() in fruit['name'].lower()]
    return result