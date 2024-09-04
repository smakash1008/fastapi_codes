from fastapi import FastAPI
app = FastAPI(title="MY APPLICATION 1")

@app.get('/book/{book_id}', tags=["Book_Details"])
async def get_book(book_id: str):
    books = {
        "1001" : "Chronicles Of Narnia",
        "1002" : "Harry Potter",
        "1003" : "The Ghost",
        "1004" : "Ponniyin Selvan",
        "1005" : "Quantum Physics"
    }
    return books.get(book_id)