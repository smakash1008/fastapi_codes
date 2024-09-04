from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI(title="MY APPLICATION 1")

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/favicon.ico", tags=["Favicon 1"])
async def get_icon1():
    return FileResponse("static/favicon.ico")

@app.get("/addition", tags=["Addition"])
async def add_val(a: int, b:int):
    c = a + b
    return f"The value of c is {c}."