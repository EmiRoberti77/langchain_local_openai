from aiohttp import ClientError
import boto3
import os

S3 = "s3"
SUCCESS = "success"
NEWS = "news"


class S3Service:
    def __init__(self) -> None:
        pass

    def __copyDest__(self, newFileName: str) -> str:
        wd = os.getcwd()
        return os.path.join(wd, NEWS, newFileName)

    def copy(self, s3Param: any) -> any:
        try:
            s3Client = boto3.client(S3)
            param = {"Bucket": s3Param.Bucket, "Key": s3Param.Key}
            s3Client.download_file(
                s3Param.Bucket, s3Param.Key, self.__copyDest__(s3Param.Key)
            )
            return SUCCESS
        except ClientError as e:
            return e
