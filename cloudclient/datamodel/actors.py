from pydantic import BaseModel, Extra
from enum import Enum


class ActorTypeEnum(Enum):
    gridoperator = "GRIDOPERATOR"
    energyholon = "ENERGYHOLON"
    connectionowner = "CONNECTIONOWNER"
    energysupplier = "ENERGYSUPPLIER"


class Actor(BaseModel, extra=Extra.forbid):
    actor_type: ActorTypeEnum
    id: str
    parent_actor: str
