from fastapi import FastAPI
app = FastAPI()

@app.get("/message")
async def welcome_message():
    return {"Welcome Message" : "Hello Everyone. Welcome To Chennai."}