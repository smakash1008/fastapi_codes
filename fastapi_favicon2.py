from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI(title="MY APPLICATION 2")

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/favicon.ico", tags=["Favicon 2"])
async def get_icon2():
    return FileResponse("static/favicon.ico")

@app.get("/subtraction", tags=["Subtraction"])
async def sub_val(a: int, b:int):
    c = a - b
    return f"The value of c is {c}."