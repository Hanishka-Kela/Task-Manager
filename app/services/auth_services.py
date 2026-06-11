from typing import Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import session
from app.schemas import UserCreate
from app. repositories import UserRepository
from app.core.security import pwd_context,SECRET_KEY,ALGORITHM
from datetime import timedelta, datetime
import jwt

class AuthSevice:

    @staticmethod
    def registerUser(db:session, user: UserCreate):
        user_in_db = UserRepository.get_user_by_username(db,user.username)
        if user_in_db:
            raise HTTPException(status_code = 400, detail = "User already Exists")

        hashed_password = pwd_context.hash(user.password)
        user_dict = user.model_dump()
        user_dict["password"] = hashed_password
        return UserRepository.UserCreate(db,user_dict)
            
    @staticmethod
    def verify_password(plain_password:str, hashed_password:str) ->bool:
        return pwd_context.verfy(plain_password, hashed_password)

    @staticmethod
    def get_pwd_hash(password:str) ->str:
        return pwd_context.hash(password)
    
    @staticmethod
    def create_access_token(data:dict, expires_delta: Optional[timedelta] = None) ->str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() +timedelta(minutes=30)
        
        to_encode.update({"exp":expire})
        encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM )
        return encoded_jwt 

    
        
            
