from pydantic import BaseModel


class UpdateEngineItem(BaseModel):
    client: str = None
