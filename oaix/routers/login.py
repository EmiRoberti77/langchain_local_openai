from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from datetime import datetime, timedelta
from utils.Path import Path as p
from models.schemas import TokenData, LoginPostItem as LoginRequest
from models.models import User
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database.database import get_db
from utils.JsonResponse import JsonResponse as JR
from utils.HttpCodes import HTTP_Codes as HTTP
from models.schemas import ResponseUser
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
INVALID_TOKEN = 'invalid token'

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")


def generate_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


@router.post(p.LOGIN)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == request.name).first()
    if not user:
        return JR.create(HTTP.NOT_FOUND, {"message": F"{request.name} not found"})
    if not pwd_context.verify(request.password, user.password):
        return JR.create(HTTP.NOT_FOUND, {"message": F"{request.name} invalid password"})

    access_token = generate_token(data={"sub": user.name})
    return JR.create(HTTP.SUCCESS, {"access_token": access_token, "token_type": "bearer"})


def get_current_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail=INVALID_TOKEN
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, access_token=[ALGORITHM])
        name: str = payload.get('sub')
        if name is None:
            raise credentials_exception

        token_data = TokenData(name=name)
        return name
    except JWTError as e:
        raise credentials_exception
