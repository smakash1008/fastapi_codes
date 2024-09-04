from fastapi import FastAPI
app = FastAPI(title="MY APP 1")

@app.get("/calculation")
async def calculation(a: int, b: int):
    c = a + b
    return f"The value of c after addition is {c}."