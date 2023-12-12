from fastapi import APIRouter
from s3.S3Service import S3Service
from utils.JsonResponse import JsonResponse as JR
from utils.Path import Path as p
from utils.Version import Version as V
from utils.HttpCodes import HTTP_Codes as HTTP
from constants import console as out
from constants import ColorWrapper as CR
from models.PostItem import PostItem as PromptItem
from models.UpdateFromS3Item import UpdateFromS3Item as S3Params
from models.UpdateEngineItem import UpdateEngineItem
from AI.AIXEngine import AIXEngine

aix = None
router = APIRouter()


@router.post(p.INPUT)
def input(input: PromptItem):
    inputResponse = aix.prompt(input=input.input)
    return JR.create(HTTP.SUCCESS, inputResponse)


@router.post(p.UPDATE)
def update(updateItem: UpdateEngineItem):
    global aix
    if aix is None:
        out(msg="oaix init process started", color=CR.yellow, reset=True)
        aix = AIXEngine()

    aix.init_engine()
    out(msg="oaix init process completed", color=CR.yellow, reset=True)
    response = aix.init_engine()
    return JR.create(HTTP.SUCCESS, {"client": updateItem, "update_status": response})


@router.post(p.NEWFILE)
def newfile(s3Params: S3Params):
    s3 = S3Service()
    success = s3.copy(s3Params)
    return JR.create(HTTP.SUCCESS, {"success": success, "s3": s3Params})
