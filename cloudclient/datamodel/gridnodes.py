from pydantic import BaseModel, Extra
from typing import Optional

from enum import Enum


class GridNode(BaseModel, extra=Extra.forbid):
    owner_actor: str
    id: str
    capacity_kw: float
    parent: Optional[str]


class ElectricGridTypeEnum(Enum):
    msls = "MSLS"
    hsms = "HSMS"


class ElectricGridNode(GridNode):
    grid_type: ElectricGridTypeEnum


class HeatGridTypeEnum(Enum):
    mt = "MT"
    ht = "HT"


class HeatGridNode(GridNode):
    grid_type: HeatGridTypeEnum
