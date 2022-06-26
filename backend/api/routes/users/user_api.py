from fastapi import APIRouter
from backend.app.schema.user_schema import User as UserSchema
from backend.app.crud.user_crud import create_user, get_users, get_user_by_id, update_user, delete_user
from backend import db_session


user_router = APIRouter(prefix="/user")
db = db_session

@user_router.post("/", response_model=UserSchema, tags=["Users"])
def make_user(user: UserSchema):
    return create_user(db.session, user)

@user_router.get("/all", status_code=200, tags=["Users"])
def load_users():
    users = get_users(db.session)
    return users

@user_router.get("/{user_id}", response_model=UserSchema, status_code=200, tags=["Users"])
def load_user(user_id: int):
    user = get_user_by_id(db.session, user_id)
    return user

@user_router.put("/{user_id}", response_model=UserSchema, status_code=200, tags=["Users"])
def modify_user(user_id: int, user_data: UserSchema):
    return update_user(db.session, user_id, user_data)

@user_router.delete("/{user_id}", response_model=UserSchema, status_code=200, tags=["Users"])
def remove_user_by_id(user_id: int):
    was_deleted = delete_user(db.session, user_id)
    return was_deleted
