from pydantic import BaseModel, Extra
from typing import Optional, List
from assets import EnergyAsset

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


class HeatingTypeEnum(Enum):
    gasburner = "GASBURNER"
    gasfired = "GASFIRED"
    heatpump_gaspeak = "HEATPUMP_GASPEAK"
    districtheat = "DISTRICTHEAT"
    heatpump_boilerpeak = "HEATPUMP_BOILERPEAK"
    hydrogenfired = "HYDROGENFIRED"
    none = "NONE"


class BuiltEnvironment(GridConnection):
    insulation_label: InsulationLabelEnum
    heating_type: HeatingTypeEnum


class Utility(GridConnection):
    heating_type: HeatingTypeEnum


class HousingTypeEnum(Enum):
    semidetached = "SEMIDETACHED"
    terraced = "TERRACED"
    detached = "DETACHED"


class House(BuiltEnvironment):
    housing_type: HousingTypeEnum


class BuildingTypeEnum(Enum):
    store = "STORE"
    office = "OFFICE"


class Building(BuiltEnvironment):
    building_type: BuildingTypeEnum


class ProductionSiteEnum(Enum):
    windfarm = "WINDFARM"
    solarfarm = "SOLARFARM"


class ProductionSite(GridConnection):
    grid_type: ProductionSiteEnum


class IndustryTypeEnum(Enum):
    steel = "STEEL"
    industry_other = "INDUSTRY_OTHER"


class Industry(Utility):
    industry_type: IndustryTypeEnum


class DistrictHeatingTypeEnum(Enum):
    mt = "MT"
    ht = "HT"


class DistrictHeating(Utility):
    district_heating_type: DistrictHeatingTypeEnum
