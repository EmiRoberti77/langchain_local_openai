from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AI.AIXEngine import AIXEngine
from models.PostItem import PostItem as PromptItem
from models.UpdateFromS3Item import UpdateFromS3Item as S3Params
from utils.JsonResponse import JsonResponse as JR
from utils.Path import Path as p
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
  JR.create(200, {'engine':'oaix'})


@app.get(p.VERSION)
def version(): 
    return JR.create(200, aix.AIXVersion())


@app.post(p.INPUT)
def input(input:PromptItem):
    print('input', input.input)
    inputResponse = aix.prompt(input=input.input)
    return JR.create(200, inputResponse)


@app.post(p.UPDATE)
def update(s3Params:S3Params):   
    print('input', s3Params.bucket, s3Params.key)
    response = aix.init_engine()
    body = {
       "s3":s3Params,
       "engine_restart":response,
    }
    return JR.create(200, body)

@app.on_event("startup")
async def startup_event():   
    global aix 
    out(msg='oaix init process started', color=CR.yellow, reset=True)
    aix = AIXEngine() 
    aix.init_engine()
    out(msg='oaix init process completed', color=CR.yellow, reset=True)
   
if __name__ == "__main__":
    uvicorn.run("3:app", host="0.0.0.0", port=8001, reload=True)
    
    
