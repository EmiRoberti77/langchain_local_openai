import json
from PromptRequest import PrompRequest

class HTTPReturn:  
  def httpReturn(self, status:int, body:str | PrompRequest) -> str:
    if isinstance(body, PrompRequest):
      body = body.model_dump()


    return {
        "isBase64Encoded": False,
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE",  
            "Access-Control-Allow-Headers": "Content-Type,Authorization" 
        },
        "body": json.dumps(body)
    }