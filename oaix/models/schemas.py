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


class LoginPostItem(BaseModel):
    name: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: Optional[str] = None
