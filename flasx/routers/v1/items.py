from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/items", tags=["items"])


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@router.get("", summary="Get all items")
async def read_items() -> list[Item]:
    return [
        Item(name="Badminton racket", price=2069.00, is_offer=True),
        Item(name="Badminton racket", price=2069.00, is_offer=True),
        Item(name="Badminton racket", price=2069.00, is_offer=True),
    ]


@router.get("/{item_id}", summary="Get an item by ID")
async def read_item(item_id: int, page: int = 1, size_per_page: int = 50) -> Item:
    return Item(name="Badminton racket", price=2069.00, is_offer=True)


@router.post("", summary="Create an item")
async def create_item(item: Item) -> Item:
    return item


@router.put("/{item_id}", summary="Update an item by ID")
async def update_item(item_id: int, item: Item) -> Item:
    return item


@router.delete("/{item_id}", summary="Delete an item by ID")
async def delete_item(item_id: int) -> dict:
    return {"item_id :", item_id, " was deleted"}
