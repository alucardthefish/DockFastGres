from backend.app.model.user_model import users
from db import db

class User:
    @classmethod
    async def get(cls, id):
        query = users.select().where(users.c.id == id)
        user = await db.fetch_one(query)
        return user

    @classmethod
    async def create(cls, **user):
        query = users.insert().values(**user)
        user_id = await db.execute(query)
        if user_id:
            user = await User.get(user_id)
            return user
        return user_id
