from pydantic import BaseModel

class PrompRequest(BaseModel):
  user:str
  content: str
  engine: str