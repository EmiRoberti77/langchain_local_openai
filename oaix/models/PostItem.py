from pydantic import BaseModel


class PostItem(BaseModel):
    input: str = None
