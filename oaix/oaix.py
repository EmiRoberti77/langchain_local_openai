from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AI.AIXEngine import AIXEngine
from models.PostItem import PostItem as PromptItem
from models.UpdateFromS3Item import UpdateFromS3Item as S3Params
from models.UpdateEngineItem import UpdateEngineItem
from s3.S3Service import S3Service
from utils.JsonResponse import JsonResponse as JR
from utils.Path import Path as p
from utils.Version import Version as V
from utils.HttpCodes import HTTP_Codes as HTTP
from constants import console as out
from constants import ColorWrapper as CR

import uvicorn

app = FastAPI()
aix = None
emi = None

app.add_middleware(
  CORSMiddleware, 
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get(p.HOME)
def home():
  return JR.create(HTTP.SUCCESS, V().toJson())


@app.get(p.VERSION)
def version(): 
    return JR.create(HTTP.SUCCESS, V().toJson())


@app.post(p.INPUT)
def input(input:PromptItem):
    inputResponse = aix.prompt(input=input.input)
    return JR.create(HTTP.SUCCESS, inputResponse)


@app.post(p.UPDATE)
def update(updateItem:UpdateEngineItem):   
    response = aix.init_engine()
    return JR.create(HTTP.SUCCESS, {"client":updateItem, "update_status":response})



@app.post(p.NEWFILE)
def newfile(s3Params:S3Params):
    s3 = S3Service()
    success = s3.copy(s3Params)
    return JR.create(HTTP.SUCCESS, {"success":success, "s3":s3Params})



@app.on_event("startup")
async def startup_event():   
    global aix 
    out(msg='oaix init process started', color=CR.yellow, reset=True)
    aix = AIXEngine() 
    aix.init_engine()
    out(msg='oaix init process completed', color=CR.yellow, reset=True)
   
   
if __name__ == "__main__":
    uvicorn.run("oaix:app", host="0.0.0.0", port=8001, reload=True)
    
    
