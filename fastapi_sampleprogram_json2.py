from fastapi import FastAPI
app = FastAPI()

@app.get("/cityname")
async def get_cityname(city: str):
    return {"City Name": f"{city}"}