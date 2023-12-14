from fastapi import APIRouter
from fastapi.params import Depends
from utils.Path import Path as p
from models import schemas
from models.models import User
from utils.JsonResponse import JsonResponse as JR
from utils.HttpCodes import HTTP_Codes as HTTP
from database.database import engine, SessionLocal
from models.models import Base
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database.database import get_db
from routers.login import get_current_user

router = APIRouter()
Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get(p.ALL_USERS)
def all_users(db: Session = Depends(get_db), create_user: User = Depends(get_current_user)):
    users = db.query(User).all()
    return JR.create(HTTP.SUCCESS, users)


@router.get(p.GET_USER)
def get_user(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).first()
    return JR.create(HTTP.SUCCESS, schemas.ResponseUser(name=user.name, password=user.password))


@router.post(p.ADD_USER)
def add_user(request: schemas.User, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    hashed_password = pwd_context.hash(request.password)
    new_user = User(name=request.name,
                    password=hashed_password, token=request.token)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JR.create(HTTP.SUCCESS, schemas.ResponseUser(name=new_user.name))


@router.delete(p.DELETE_USER)
def delete_user(id, db: Session = Depends(get_db), create_user: User = Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).delete(
        synchronize_session=False)
    db.commit()
    return JR.create(HTTP.SUCCESS, user)
