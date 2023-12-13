from pydantic import BaseModel
from typing import Optional
PROTECTED = '********'


class User(BaseModel):
    name: str = None
    password: str = None
    token: str = None


class ResponseUser(BaseModel):
    name: str
    password: Optional[str] = PROTECTED

    class Config:
        orm_mode = True
