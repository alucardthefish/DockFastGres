from fastapi import APIRouter
from backend.app.schema.item_schema import Item as ItemSchema, ItemCreate
from backend.app.crud.item_crud import Item


item_router = APIRouter(prefix="/item")


@item_router.post("/", response_model=ItemSchema, tags=["Items"])
async def create_item(item: ItemCreate):
    item_id = await Item.create(**item.dict())
    return {"item_id": item_id}

@item_router.get("/all", tags=["Items"])
async def get_item(item_id: int):
    item = await Item.get(item_id)
    return item
