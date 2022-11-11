from consumption import HeatConsumptionAsset, ElectricConsumptionAsset

Industry_steel_electricity = ElectricConsumptionAsset(
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Industry_other_electricity = ElectricConsumptionAsset(
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Logistics_fleet_hgv_E = ElectricConsumptionAsset(
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=6500000,
)
Industry_steel_heat = HeatConsumptionAsset(
    asset_type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=1000000,
)
Industry_other_heat = HeatConsumptionAsset(
    asset_type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=1000000,
)
House_hot_water = HeatConsumptionAsset(
    asset_type="HOT_WATER_CONSUMPTION",
    yearlyDemandHeat_kWh=30,
)
House_other_electricity = ElectricConsumptionAsset(
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=2479,
)
Office_other_electricity = ElectricConsumptionAsset(
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=120000,
)
Store_other_electricity = ElectricConsumptionAsset(
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=35000,
)
