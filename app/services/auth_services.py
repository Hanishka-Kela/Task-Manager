from typing import Optional
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import session
from app.schemas import UserCreate, TokenData, Token, UserLogin
from app.repositories.user_repository import UserRepository
from app.core.security import pwd_context,SECRET_KEY,ALGORITHM
from datetime import timedelta, datetime
import jwt

class AuthService:

    @staticmethod
    def registerUser(db:session, user: UserCreate):
        user_in_db = UserRepository.get_user_by_username(db,user.username)
        if user_in_db:
            raise HTTPException(status_code = 400, detail = "User already Exists")

        hashed_password = pwd_context.hash(user.password.encode("utf-8")[:72])
        user_dict = user.model_dump()
        user_dict["hashed_password"] = hashed_password
        del user_dict["password"]
        return UserRepository.create_user(db,user_dict)
            
    @staticmethod
    def verify_password(plain_password:str, hashed_password:str) ->bool:
        return pwd_context.verify(plain_password, hashed_password)

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

    @staticmethod
    def verify_token(token :str) -> TokenData :
        try :
            payload = jwt.decode(token , SECRET_KEY, algorithms = [ALGORITHM])
            username:str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401 , 
                detail="Could Not verify credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )
            return TokenData(username = username)
        
        except jwt.PyJWTError:
            raise HTTPException(status_code = 401,
            detail = "Could Not verify credentials",
            headers={"WWW-Authenticate": "Bearer"})

    @staticmethod
    def loginUser(db:session,user:UserLogin):
        db_user = UserRepository.get_user_by_username(db,user.username)
        truncated = user.password.encode("utf-8")[:72]
        if not db_user or not pwd_context.verify(truncated, db_user.hashed_password):
            raise HTTPException(status_code = 401, detail = "Invalid Credentials")
        token_data = {"sub":db_user.username} 
        access_token = AuthService.create_access_token(data=token_data)
        return {"access_token": access_token, "token_type": "bearer"}
