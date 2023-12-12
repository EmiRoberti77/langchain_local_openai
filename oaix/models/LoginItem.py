from pydantic import BaseModel


class LoginItem(BaseModel):
    user: str = None
    login: str = None
