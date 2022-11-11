from pydantic import BaseModel, Extra
from typing import Optional

from enum import Enum


class GridConnection(BaseModel, extra=Extra.forbid):
    owner_actor: str
    capacity_kw: float
    parent_electric: Optional[float]
    parent_heat: Optional[float]
    id: str


class Household(GridConnection):
    pass


class ProductionSiteEnum(Enum):
    windfarm = "WINDFARM"
    solarfarm = "SOLARFARM"

class ProductionSite(asdf):
    grid_type : ProductionSiteEnum
    pass


class AFDF(asdf):
    pass


class AFDF(asdf):
    pass


class AFDF(asdf):
    pass


class AFDF(asdf):
    pass
