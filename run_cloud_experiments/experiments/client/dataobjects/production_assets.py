from energy_asset import EnergyAsset
from enum import Enum


class ProductionAssetTypeEnum(Enum):
    photovoltaic = "PHOTOVOLTAIC"
    windmill = "WINDMILL"


class ProductionAsset(EnergyAsset):
    asset_type: ProductionAssetTypeEnum
    alias: str


class ElectricProductionAsset(ProductionAsset):
    capacityElectricity_kW: float


class HeatProductionAsset(ProductionAsset):
    capacityHeat_kW: float


class HybridProductionAsset(ElectricProductionAsset, HeatProductionAsset):
    pass


if __name__ == "__main__":

    dummy_data = {
        "asset_type": "HOT_WATER_CONSUMPTION",
        "yearlyDemandHeat_kWh": 30,
    }

    asset = ElectricProductionAsset(**dummy_data)
    import json

    print(json.dumps(json.loads(asset.json()), indent=4))
