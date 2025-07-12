from fastapi import FastAPI, APIRouter
from . import routers

app = FastAPI()
app.include_router(routers.router)


@app.get("/")
def get_hello() -> dict:
    return {"Hello": "World"}
