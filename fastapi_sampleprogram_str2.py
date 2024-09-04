from fastapi import FastAPI
app = FastAPI()

@app.get("/city")
async def cityname(city: str):
    return f"Hello Everyone. Welcome To {city}."