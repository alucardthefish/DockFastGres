from fastapi import APIRouter
from backend.app.schema.user_schema import User as UserSchema
from backend.app.crud.user_crud import User


user_router = APIRouter(prefix="/user")

@user_router.post("/", response_model=UserSchema, tags=["Users"])
async def create_user(user: UserSchema):
    user_id = await User.create(**user.dict())
    return {"user_id": user_id}

@user_router.get("/{user_id}", response_model=UserSchema, status_code=200, tags=["Users"])
async def get_user(user_id: int):
    user = await User.get(user_id)
    return user
