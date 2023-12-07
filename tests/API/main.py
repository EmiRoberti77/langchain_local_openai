from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from HTTReturn import HTTPReturn
from PromptRequest import PrompRequest
from AIEngine import AIEngine as AI

def configMiddleware():
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
  )

app = FastAPI()
configMiddleware()
ai = AI()

@app.get('/api/v1/version')
def root():
  http_response = HTTPReturn()
  return http_response.httpReturn(200, {"version":"1.0"})

@app.post('/api/v1/aiprompt')
def prompt(req:PrompRequest):
  return ai.prompt(req)
 