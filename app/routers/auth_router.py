from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserRegister, UserLogin, Token, UserResponse
# pyrefly: ignore [missing-import]
from app.services.auth_services import AuthService
from app.database import get_db
router_user = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router_user.post("/signup", response_model=UserResponse, status_code=201)
def create_user(user_data: UserRegister, db:Session = Depends(get_db)):
    return AuthService.registerUser(db,user_data)

@router_user.post("/login", response_model=Token, status_code=200)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Login with JSON body — for API clients (Postman, curl, etc.)"""
    return AuthService.loginUser(db, user)

@router_user.post("/token", response_model=Token, status_code=200)
def token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login with form data — used by Swagger Authorize button."""
    user = UserLogin(username=form_data.username, password=form_data.password)
    return AuthService.loginUser(db, user)


