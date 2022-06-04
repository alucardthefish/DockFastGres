from typing import List
import uvicorn
from fastapi import FastAPI

import os
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import User as ModelUser
from schema import User as SchemaUser
from sqlalchemy.orm import Session
from user_crud import get_user_by_id, get_users


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user

@app.get("/users/", status_code=200)
def load_users():
    users = get_users(db.session)
    return users

@app.get("/user/{user_id}", response_model=SchemaUser, status_code=200)
def load_user(user_id: int):
    user = get_user_by_id(db.session, user_id)
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
