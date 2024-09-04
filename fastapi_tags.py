from fastapi import FastAPI
app = FastAPI(title="MY APP 2")

@app.get("/addition", tags=["Addition"])
async def add_val(a: int, b: int):
    c = a + b
    return {"Value of c" : f"{c}"}