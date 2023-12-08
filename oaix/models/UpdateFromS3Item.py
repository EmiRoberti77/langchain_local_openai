from pydantic import BaseModel

class UpdateFromS3Item(BaseModel):
  bucket:str = None
  key:str = None