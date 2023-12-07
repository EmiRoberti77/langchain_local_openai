from dotenv import load_dotenv
from constants import console as out
from constants import ColorWrapper as CR
import os

class AIXBase:
  def __init__(self) -> None:
    out(msg='OAIX Base', color=CR.green, reset=True)
    load_dotenv()
    self.__OPENAI_API_KEY__ = os.getenv('OPENAI_API_KEY')

  def AIXVersion(self)->float:
    return 0.2