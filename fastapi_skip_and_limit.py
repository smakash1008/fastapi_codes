from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 1")

books = [
    {"1001": "Quantum Physics"},
    {"1002": "Organic Chemistry"},
    {"1003": "Harry Potter"},
    {"1004": "Chronicles Of Narnia"},
    {"1005": "Jurassic Park"}
]

@app.get("/booklimit", tags=["Book_Details"])
async def book_details(limit: int):
    final_data = books[: limit]
    return final_data

@app.get("/bookskiplimit", tags=["Books"])
async def skip_books(skip: int, limit: int):
    finaldata = books[skip : skip + limit]
    return finaldata

# Beyond Skip All Data:
@app.get("/beyondskip", tags=['Book_Full_Data'])
async def book_full_details(skip: int):
    finaldata1 = books[skip :]
    return finaldata1