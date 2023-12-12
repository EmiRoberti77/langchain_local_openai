from pydantic import BaseModel


class UpdateFromS3Item(BaseModel):
    Bucket: str = None
    Key: str = None
