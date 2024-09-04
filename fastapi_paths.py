from fastapi import FastAPI
app = FastAPI(title="My Application 1")

@app.get("/book/{book_id}", tags=["Book_Details"])
async def book_details(book_id: int):
    return f"The Book Id is {book_id}."