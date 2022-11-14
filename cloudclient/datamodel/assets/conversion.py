from enum import Enum
from cloudclient.datamodel.assets.energy import EnergyAsset, AmbientTempTypeEnum
from typing import Optional


class ConversionAssetTypeEnum(Enum):
    boiler = "BOILER"
    electrolyser = "ELECTROLYSER"
    gas_burner = "GAS_BURNER"
    heat_delivery_set = "HEAT_DELIVERY_SET"
    heat_pump_air = "HEAT_PUMP_AIR"
    heat_pump_ground = "HEAT_PUMP_GROUND"
    hydrogen_furnace = "HYDROGEN_FURNACE"
    methane_furnace = "METHANE_FURNACE"


class ConversionAsset(EnergyAsset):
    asset_type: ConversionAssetTypeEnum
    eta_r: float
    etm_key: Optional[str]
    name: str


class ElectricCoversionAsset(ConversionAsset):
    capacityElectricity_kW: float


class HeatConversionAsset(ConversionAsset):
    deliveryTemp_degc: float


class ChemicalHeatConversionAsset(HeatConversionAsset):
    capacityHeat_kW: float


class ElectricHeatConversionAsset(HeatConversionAsset):
    capacityElectricity_kW: float


class TransportHeatConversionAsset(ElectricHeatConversionAsset):
    ambientTempType: AmbientTempTypeEnum


class HybridHeatCoversionAsset(
    TransportHeatConversionAsset, ChemicalHeatConversionAsset
):
    pass


if __name__ == "__main__":
    dummy_data = {
        "asset_type": "BOILER",
        "capacityElectricity_kW": 300,
        "eta_r": "0.99",
        "deliveryTemp_degc": 100,
        "ambientTempType": "AIR",
    }

    asset = TransportHeatConversionAsset(**dummy_data)
    import json

    print(json.dumps(json.loads(asset.json()), indent=4))
