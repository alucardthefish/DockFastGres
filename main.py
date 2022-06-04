from typing import List
import uvicorn
from fastapi import FastAPI

import os
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import User as ModelUser
from schema import User as SchemaUser
from user_crud import create_user, delete_user, get_user_by_id, get_users, update_user


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/user/", response_model=SchemaUser)
def make_user(user: SchemaUser):
    return create_user(db.session, user)

@app.get("/users/", status_code=200)
def load_users():
    users = get_users(db.session)
    return users

@app.get("/user/{user_id}", response_model=SchemaUser, status_code=200)
def load_user(user_id: int):
    user = get_user_by_id(db.session, user_id)
    return user

@app.put("/user/{user_id}", response_model=SchemaUser, status_code=200)
def modify_user(user_id: int, user_data: SchemaUser):
    return update_user(db.session, user_id, user_data)

@app.delete("/user/{user_id}", response_model=SchemaUser, status_code=200)
def remove_user_by_id(user_id: int):
    was_deleted = delete_user(db.session, user_id)
    return was_deleted


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
