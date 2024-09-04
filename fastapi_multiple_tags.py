from fastapi import FastAPI
app = FastAPI(title="MY APP 3")

@app.get("/add", tags=["Addition"])
async def add(a: int, b: int):
    c = a + b
    return {"Value Of c" : f"{c}"}

@app.get("/sub", tags=["Subtraction"])
async def sub(d: int, e: int):
    f = d - e
    return f"The value of f after subtraction is {f}."