# from oaix.models.UpdateFromS3Item import UpdateFromS3Item
# from oaix.utils.JsonResponse import JsonResponse as JR
# from oaix.utils.Storage import Storage as ST
from aiohttp import ClientError
import boto3
S3 = 's3'
SUCCESS = 'success'

class S3Service:
  def __init__(self) -> None:
    pass


  def copy(self, s3Param:any, dest:str='./')->any:
    try:
      s3Client = boto3.client(S3)
      print(s3Param)
      param = {
        "Bucket":s3Param.Bucket,
        "Key":s3Param.Key
      }
      s3Client.download_file(s3Param.Bucket, s3Param.Key, dest+s3Param.Key)
      return SUCCESS
    except ClientError as e:
      return e
