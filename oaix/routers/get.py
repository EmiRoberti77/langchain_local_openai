from fastapi import APIRouter
from utils.JsonResponse import JsonResponse as JR
from utils.Path import Path as p
from utils.Version import Version as V
from utils.HttpCodes import HTTP_Codes as HTTP

router = APIRouter()


@router.get(p.HOME)
def home():
    return JR.create(HTTP.SUCCESS, V().toJson())


@router.get(p.VERSION)
def version():
    return JR.create(HTTP.SUCCESS, V().toJson())
