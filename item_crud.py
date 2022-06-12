from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Item as ItemModel
from schema import ItemCreate


def get_items(db: Session):
    items = select(ItemModel)
    return db.execute(items).scalars().all()

def create_item(db: Session, item: ItemCreate):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
