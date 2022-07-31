from backend.app.model.item_model import items
from db import db

class Item:
    @classmethod
    async def get(cls, id):
        query = items.select().where(items.c.id == id)
        item = await db.execute(query)
        return item

    @classmethod
    async def create(cls, **item):
        query = items.insert().values(**item)
        item_id = await db.execute(query)
        return item_id
