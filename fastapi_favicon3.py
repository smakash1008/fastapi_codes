from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI(title="MY APPLICATION 3")

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/favicon.ico", tags=["Favicon 3"])
async def get_icon3():
    return FileResponse("static/favicon.ico")

@app.get("/multiplication", tags=["Multiplication"])
async def mul_val(a: int, b:int):
    c = a * b
    return f"The value of c is {c}."