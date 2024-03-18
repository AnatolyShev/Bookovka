import jwt
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database import get_db, db_dependency
from starlette import status
import random
from schemas import Token, UserBase
from models import User, Basket
from jose import JWTError

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = "1super_sain_secret_key1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

def authentificate_user(email: str, password: str, db: db_dependency):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authentificate_user(form_data.username , form_data.password, db) # под полем form_data.username подразумевается user.email
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(user.email, user.id, timedelta(minutes=20))

    return {'token': token, 'user_id': user.id}
    
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]): #oauth2_bearer
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        user_id: int = payload.get('id')
        if email is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'email': email, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')

@router.post("/register")
async def register_user(user: UserBase, db: db_dependency):
    # Проверяем, существует ли пользователь с таким email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User already registered')
    # Создаем нового пользователя
    new_user = User(email=user.email, password=bcrypt_context.hash(user.password) , name=user.name, is_superuser=user.is_superuser)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    _user = db.query(User).filter(User.email == user.email).first()
    db_basket = Basket(user_id=_user.id)
    db.add(db_basket)
    db.commit()    
    db.refresh(db_basket)
    return {"message": "User registered successfully"}
