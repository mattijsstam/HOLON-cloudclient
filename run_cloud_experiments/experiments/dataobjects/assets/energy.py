from pydantic import BaseModel, Extra

from enum import Enum


class EnergyAsset(BaseModel, extra=Extra.forbid):
    # id: str
    # connection_id: str
    # parent_id: str
    # energy_carriers: list[str]
    pass

# class DefaultEnergyAsset(EnergyAsset):
#     name: str

class AmbientTempTypeEnum(str, Enum):
    air = "AIR"
    ground = "GROUND"