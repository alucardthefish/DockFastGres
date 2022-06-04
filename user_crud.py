from sqlalchemy.orm import Session
from models import User


def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter_by(id=id).first()