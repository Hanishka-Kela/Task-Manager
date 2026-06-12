from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserLogin, Token
# pyrefly: ignore [missing-import]
from app.services.auth_services import AuthService
from app.database import get_db
router_user = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router_user.post("/signup", response_model=UserCreate,status_code=201)
def create_user(user_data: UserCreate,db:Session = Depends(get_db)):
    return AuthService.registerUser(db,user_data)

@router_user.post("/login", response_model=Token, status_code =200)
def login(user:UserLogin, db: Session = Depends(get_db)):
    return AuthService.loginUser(db , user)


