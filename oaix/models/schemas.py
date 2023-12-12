from pydantic import BaseModel


class User(BaseModel):
    user: str = None
    password: str = None
    token: str = None
