from fastapi import FastAPI
app = FastAPI(title="My Application 2")

@app.get("/book/{book_id}/{book_name}", tags=["Book_Details"])
async def book_details(book_id: int, book_name: str):
    return {"Book ID": f"{book_id}", "Book Name": f"{book_name}"}

