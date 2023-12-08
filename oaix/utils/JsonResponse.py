class JsonResponse:
  @staticmethod
  def create(statusCode=int, body=object):
    response = {
      "statusCode": statusCode,
      "body": body,
      "headers": {
          "Access-Control-Allow-Origin": "*", 
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range",
          "Access-Control-Expose-Headers": "Content-Length,Content-Range",
      }
    }
    return response