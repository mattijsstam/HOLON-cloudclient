from cloudclient.datamodel import (
    HeatStorageAsset,
    ElectricStorageAsset,
    VehicleElectricStorageAsset,
)

House_battery = ElectricStorageAsset(
    name="House_battery",
    asset_type="STORAGE_ELECTRIC",
    capacityElectricity_kW=10,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=50,
)
House_heatmodel_A = HeatStorageAsset(
    name="House_heatmodel_A",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=50,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_B = HeatStorageAsset(
    name="House_heatmodel_B",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=60,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_C = HeatStorageAsset(
    name="House_heatmodel_C",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=70,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_D = HeatStorageAsset(
    name="House_heatmodel_D",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=80,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_E = HeatStorageAsset(
    name="House_heatmodel_E",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=90,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_F = HeatStorageAsset(
    name="House_heatmodel_F",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_G = HeatStorageAsset(
    name="House_heatmodel_G",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=100.0,
    stateOfCharge_r=0.5,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=110,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
EV = VehicleElectricStorageAsset(
    name="EV",
    asset_type="ELECTRIC_VEHICLE",
    capacityElectricity_kW=11,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=50,
    energy_consumption_kwhpkm=0.2,
)
District_Heating_heat_buffer_HT_S = HeatStorageAsset(
    name="District_Heating_heat_buffer_HT_S",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    stateOfCharge_r=0.75,
    minTemp_degC=10,
    maxTemp_degC=90,
    setTemp_degC=70,
    lossFactor_WpK=300,
    heatCapacity_JpK=10000000000.0,
    ambientTempType="GROUND",
)
District_Heating_network_HT_S = HeatStorageAsset(
    name="District_Heating_network_HT_S",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    stateOfCharge_r=1.0,
    minTemp_degC=70,
    maxTemp_degC=100,
    setTemp_degC=90,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="GROUND",
)
District_Heating_network_MT_S = HeatStorageAsset(
    name="District_Heating_network_MT_S",
    asset_type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    stateOfCharge_r=1.0,
    minTemp_degC=60,
    maxTemp_degC=80,
    setTemp_degC=70,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="GROUND",
)
Grid_battery_1MW = ElectricStorageAsset(
    name="Grid_battery_1MW",
    asset_type="STORAGE_ELECTRIC",
    capacityElectricity_kW=1000,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=1000,
)
EHGV = VehicleElectricStorageAsset(
    name="EHGV",
    asset_type="ELECTRIC_HEAVY_GOODS_VEHICLE",
    capacityElectricity_kW=110,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=500,
    energy_consumption_kwhpkm=1,
)
Grid_battery_10MWh = ElectricStorageAsset(
    name="Grid_battery_10MWh",
    asset_type="STORAGE_ELECTRIC",
    capacityElectricity_kW=2000,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=10000,
)
