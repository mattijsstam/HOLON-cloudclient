from enum import Enum
from typing import Optional

from cloudclient.datamodel.assets.energy import EnergyAsset


class ConsumptionAssetTypeEnum(Enum):
    electricity_demand = "ELECTRICITY_DEMAND"
    heat_demand = "HEAT_DEMAND"
    hot_water_consumption = "HOT_WATER_CONSUMPTION"
    other_electricity_consumption = "OTHER_ELECTRICITY_CONSUMPTION"


class ConsumptionAsset(EnergyAsset):
    asset_type: ConsumptionAssetTypeEnum
    etm_key: Optional[str]
    name: str


class HeatConsumptionAsset(ConsumptionAsset):
    yearlyDemandHeat_kWh: float


class ElectricConsumptionAsset(ConsumptionAsset):
    yearlyDemandElectricity_kWh: float


class HybridConsumptionAsset(ElectricConsumptionAsset, HeatConsumptionAsset):
    pass


if __name__ == "__main__":

    dummy_data = {
        "asset_type": "HOT_WATER_CONSUMPTION",
        "yearlyDemandHeat_kWh": 30,
    }

    asset = HeatConsumptionAsset(**dummy_data)
    import json

    print(json.dumps(json.loads(asset.json()), indent=4))
