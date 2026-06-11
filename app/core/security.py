from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

SECRET_KEY = "tasktracker"
ALGORITHM = "HS256"
TOKEN_EXPIRES = 30

pwd_context = CryptContext(schemes=['bcrypt'], 
                           deprecated = "auto")

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    