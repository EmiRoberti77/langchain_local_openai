from fastapi import APIRouter
from fastapi.params import Depends
from utils.Path import Path as p
from models import schemas
from models.models import User
from utils.JsonResponse import JsonResponse as JR
from utils.HttpCodes import HTTP_Codes as HTTP
from database.database import engine, SessionLocal
from models.models import Base
from sqlalchemy.orm import Session

router = APIRouter()
Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(p.ALL_USERS)
def all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return JR.create(HTTP.SUCCESS, users)


@router.get(p.GET_USER)
def get_user(id, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    return JR.create(HTTP.SUCCESS, user)


@router.post(p.ADD_USER)
def add_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = User(name=request.user,
                    password=request.password, token=request.token)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JR.create(HTTP.SUCCESS, request)
