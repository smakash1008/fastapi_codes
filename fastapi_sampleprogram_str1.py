from fastapi import FastAPI
app = FastAPI()

@app.get("/person")
async def welcome_person():
    return "Hello Everyone. Welcome To Chennai..."