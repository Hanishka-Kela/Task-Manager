from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.user_repository import UserRepository

SECRET_KEY = "tasktracker"
ALGORITHM = "HS256"
TOKEN_EXPIRES = 30

pwd_context = CryptContext(schemes=['bcrypt'], 
                           deprecated="auto",
                           bcrypt__truncate_error=False)

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_current_user(token:str = Depends(OAuth2_scheme), db:Session = Depends(get_db)):
    from app.services.auth_services import AuthService
    token_data = AuthService.verify_token(token)
    if token_data is None or token_data.username is None:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    user = UserRepository.get_user_by_username(db, username=token_data.username)

    if user is None:
        raise HTTPException(status_code=401 , detail = "Invalid Credentials", headers= {"WWW-Authenticate": "Bearer"})
    return user