from fastapi import FastAPI
app = FastAPI(title="My Application 3")

@app.get("/book/default", tags=["Default Name"])
async def default_name():
    return "Harry Potter"

@app.get("/book/{book_name}", tags=["Book_Name"])
async def book_names(book_name: str):
    return {"Book Name" : f"{book_name}"}