from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AI.AIXEngine import AIXEngine
from pydantic import BaseModel
import uvicorn

class PostItem(BaseModel):
   input:str = None

app = FastAPI()
aix = AIXEngine()

app.add_middleware(
  CORSMiddleware, 
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get('/')
def home():
  response = {
      "statusCode": 200,
      "body": "emi ai engine",
      "headers": {
          "Access-Control-Allow-Origin": "*", 
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
      }
    }
  return response

@app.get('/version')
def version(): 
    response = {
      "statusCode": 200,
      "body": aix.AIXVersion(),
      "headers": {
          "Access-Control-Allow-Origin": "*", 
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
      }
    }
    return response

@app.post('/input')
def input(input:PostItem):
    print('input', input.input)
    inputResponse = aix.prompt(input=input.input)
    response = {
      "statusCode": 200,
      "body": inputResponse,
      "headers": {
          "Access-Control-Allow-Origin": "*", 
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
      }
    }
    return response
   
   

if __name__ == "__main__":
    uvicorn.run("3:app", host="0.0.0.0", port=8001, reload=True)
