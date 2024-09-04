# FastAPI Post - Create The Data.

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="MY APPLICATION 1")

class Books(BaseModel):
    id: int
    name: str
    author: str
    year: int

@app.post("/books/", tags=["Book_Details"])
async def book_details(book: Books):
    return book
