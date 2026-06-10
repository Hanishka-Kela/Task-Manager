from sqlalchemy.orm import Session
from app.models import User

class UserRepositoy:
    @staticmethod
    def create_user(db:Session, user_data:dict):
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    @staticmethod
    def get_user_by_username(db:Session, username:str):
        return db.query(User).filter(User.username==username).first()
