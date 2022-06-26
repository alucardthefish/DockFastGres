from fastapi import APIRouter
from backend import db_session
from backend.app.schema.item_schema import Item as ItemSchema, ItemCreate
from backend.app.crud.item_crud import create_item, get_items


item_router = APIRouter(prefix="/item")
db = db_session


@item_router.post("/", response_model=ItemSchema, tags=["Items"])
def make_item(item: ItemCreate):
    return create_item(db.session, item)

@item_router.get("/all", tags=["Items"])
def load_items():
    return get_items(db.session)
