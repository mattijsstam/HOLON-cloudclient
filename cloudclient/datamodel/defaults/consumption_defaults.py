from cloudclient.datamodel import HeatConsumptionAsset, ElectricConsumptionAsset

Industry_steel_electricity = ElectricConsumptionAsset(
    name="Industry_steel_electricity",
    etm_key="industry_steel_electricity_demand",
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Industry_other_electricity = ElectricConsumptionAsset(
    name="Industry_other_electricity",
    etm_key="industry_other_electricity_demand",
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Logistics_fleet_hgv_E = ElectricConsumptionAsset(
    name="Logistics_fleet_hgv_E",
    etm_key="logistics_fleet_e_hgv",
    asset_type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=6500000,
)
Industry_steel_heat = HeatConsumptionAsset(
    name="Industry_steel_heat",
    etm_key="industry_steel_heat_demand",
    asset_type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=1000000,
)
Industry_other_heat = HeatConsumptionAsset(
    name="Industry_other_heat",
    etm_key="industry_other_heat_demand",
    asset_type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=1000000,
)
House_hot_water = HeatConsumptionAsset(
    name="House_hot_water",
    etm_key="house_hot_water_consumption",
    asset_type="HOT_WATER_CONSUMPTION",
    yearlyDemandHeat_kWh=30,
)
House_other_electricity = ElectricConsumptionAsset(
    name="House_other_electricity",
    etm_key="house_other_electricity_consumption",
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=2479,
)
Office_other_electricity = ElectricConsumptionAsset(
    name="Office_other_electricity",
    etm_key="office_other_electricity_consumption",
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=120000,
)
Store_other_electricity = ElectricConsumptionAsset(
    name="Store_other_electricity",
    etm_key="store_other_electricity_consumption",
    asset_type="OTHER_ELECTRICITY_CONSUMPTION",
    yearlyDemandElectricity_kWh=35000,
)
