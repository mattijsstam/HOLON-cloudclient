from pydantic import BaseModel, Extra
from enum import Enum


class ActorTypeEnum(Enum):
    gridoperator = "GRIDOPERATOR"
    energyholon = "ENERGYHOLON"
    connectionowner = "CONNECTIONOWNER"
    energysupplier = "ENERGYSUPPLIER"


class SubTypeEnum(Enum):
    commercial = "commercial"
    energysupplier = "energysupplier"
    holon = "holon"
    gridoperator = "gridoperator"


class Actor(BaseModel, extra=Extra.forbid):
    actor_type: ActorTypeEnum
    id: str
    parent_actor: str
    subtype: str
