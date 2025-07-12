from fastapi import FastAPI
from pydantic import BaseModel

# import decimal

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def get_hello() -> dict:
    return {"Hello": "World"}


@app.get("/items")
async def read_items() -> dict:
    return {"items": [{"item1"}, {"item2"}]}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "query string": q}


@app.post("/items")
async def create_item(item: dict) -> dict:
    return {"item", item}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict) -> dict:
    return {"item_id : ", item_id, " was updated"}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int) -> dict:
    return {"item_id :", item_id, " was deleted"}
