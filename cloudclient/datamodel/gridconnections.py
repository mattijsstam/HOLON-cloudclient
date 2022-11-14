from pydantic import BaseModel, Extra
from typing import Optional, List
from cloudclient.datamodel.assets import EnergyAsset

from enum import Enum


class GridConnection(BaseModel, extra=Extra.forbid):
    owner_actor: str
    id: str
    capacity_kw: float
    parent_electric: str
    parent_heat: Optional[str]
    assets: Optional[List[EnergyAsset]]


class InsulationLabelEnum(Enum):
    a = "A"
    b = "B"
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    none = "NONE"


class HeatingTypeEnum(Enum):
    gasburner = "GASBURNER"
    gasfired = "GASFIRED"
    heatpump_gaspeak = "HEATPUMP_GASPEAK"
    districtheat = "DISTRICTHEAT"
    heatpump_boilerpeak = "HEATPUMP_BOILERPEAK"
    hydrogenfired = "HYDROGENFIRED"
    none = "NONE"


class BuiltEnvironmentGridConnection(GridConnection):
    insulation_label: InsulationLabelEnum
    heating_type: HeatingTypeEnum


class UtilityGridConnection(GridConnection):
    heating_type: HeatingTypeEnum


class HousingTypeEnum(Enum):
    semidetached = "SEMIDETACHED"
    terraced = "TERRACED"
    detached = "DETACHED"


class HouseGridConnection(BuiltEnvironmentGridConnection):
    grid_type: HousingTypeEnum


class BuildingTypeEnum(Enum):
    store = "STORE"
    office = "OFFICE"
    logistics = "LOGISTICS"


class BuildingGridConnection(BuiltEnvironmentGridConnection):
    grid_type: BuildingTypeEnum


class ProductionEnum(Enum):
    windfarm = "WINDFARM"
    solarfarm = "SOLARFARM"
    gridbattery = "GRIDBATTERY"


class ProductionGridConnection(GridConnection):
    grid_type: ProductionEnum


class IndustryTypeEnum(Enum):
    steel = "STEEL"
    industry_other = "INDUSTRY_OTHER"


class IndustryGridConnection(UtilityGridConnection):
    grid_type: IndustryTypeEnum


class DistrictHeatingTypeEnum(Enum):
    mt = "MT"
    ht = "HT"


class DistrictHeatingGridConnection(UtilityGridConnection):
    district_heating_type: DistrictHeatingTypeEnum
