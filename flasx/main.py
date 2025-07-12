from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_hello() -> dict:
    return {"Hello" : "World"}

