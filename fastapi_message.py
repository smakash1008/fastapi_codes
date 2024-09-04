from fastapi import FastAPI
app = FastAPI()

@app.get("/greeting")
async def greeting_message(message: str):
    return {"Welcome Message" : f"{message}"}