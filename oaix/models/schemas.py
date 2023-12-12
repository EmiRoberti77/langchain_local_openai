from pydantic import BaseModel


class User(BaseModel):
    name: str = None
    password: str = None
    token: str = None
