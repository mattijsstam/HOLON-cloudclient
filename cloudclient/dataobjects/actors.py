from pydantic import BaseModel, Extra
from enum import Enum

class Actor(BaseModel, extra=Extra.forbid):
    pass



