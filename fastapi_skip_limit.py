from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 1")

@app.get("/books", tags=["Limits And Skip"])
async def limit_data(skip: int, limit: int):
    books = [
        {"1001": "Quantum Physics"},
        {"1002": "Organic Chemistry"},
        {"1003": "Harry Potter"},
        {"1004": "Chronicles Of Narnia"},
        {"1005": "Jurassic Park"}
    ]
    return books[skip: skip + limit]