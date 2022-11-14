from cloudclient.datamodel.assets.energy import EnergyAsset, AmbientTempTypeEnum
from enum import Enum
from typing import Optional


class StorageAssetTypeEnum(Enum):
    electric_heavy_goods_vehicle = "ELECTRIC_HEAVY_GOODS_VEHICLE"
    electric_vehicle = "ELECTRIC_VEHICLE"
    storage_electric = "STORAGE_ELECTRIC"
    storage_heat = "STORAGE_HEAT"


class StorageAsset(EnergyAsset):
    asset_type: StorageAssetTypeEnum
    stateOfCharge_r: float
    etm_key: Optional[str]


class HeatStorageAsset(StorageAsset):
    capacityHeat_kW: float
    stateOfCharge_r: float
    minTemp_degC: int
    maxTemp_degC: int
    setTemp_degC: int
    lossFactor_WpK: float
    heatCapacity_JpK: float
    ambientTempType: AmbientTempTypeEnum


class ElectricStorageAsset(StorageAsset):
    capacityElectricity_kW: float
    storageCapacity_kWh: float


class VehicleElectricStorageAsset(ElectricStorageAsset):
    energy_consumption_kwhpkm: float


if __name__ == "__main__":

    dummy_data = {
        "asset_type": "ELECTRIC_HEAVY_GOODS_VEHICLE",
        "capacityElectricity_kW": 110,
        "stateOfCharge_r": 1.0,
        "storageCapacity_kWh": 500,
        "energy_consumption_kwhpkm": 1,
    }

    asset = VehicleElectricStorageAsset(**dummy_data)
    import json

    print(json.dumps(json.loads(asset.json()), indent=4))

    # to generate the class diagram
    # pyreverse <filename> -o html
