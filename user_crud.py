from sqlalchemy.orm import Session
from models import User
from schema import User as UserSchema


def create_user(db: Session, user: UserSchema):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter_by(id=id).first()

def update_user(db: Session, user_id: int, user: UserSchema):
    user_exists: User = get_user_by_id(db, user_id)
    if user_exists:
        user_exists.first_name = user.first_name
        user_exists.last_name = user.last_name
        user_exists.age = user.age
        db.add(user_exists)
        db.commit()
    return user_exists

def delete_user(db: Session, user_id: int):
    user_exists: User = get_user_by_id(db, user_id)
    if user_exists:
        db.delete(user_exists)
        db.commit()
    return user_exists
