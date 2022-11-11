from cloudclient.datamodel import (
    ElectricCoversionAsset,
    ChemicalHeatConversionAsset,
    TransportHeatConversionAsset,
)

House_heatpump_MT_S = TransportHeatConversionAsset(
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=4,
    eta_r=0.5,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_M = TransportHeatConversionAsset(
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_L = TransportHeatConversionAsset(
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=11,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_gas_burner = ChemicalHeatConversionAsset(
    asset_type="GAS_BURNER",
    capacityHeat_kW=30,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

House_DH_heatdeliveryset = ChemicalHeatConversionAsset(
    asset_type="HEAT_DELIVERY_SET",
    capacityHeat_kW=10,
    eta_r=0.99,
    deliveryTemp_degc=90,
)

Electrolyser = ElectricCoversionAsset(
    asset_type="ELECTROLYSER",
    capacityElectricity_kW=100,
    eta_r=0.6,
)

DH_gas_burner_S = ChemicalHeatConversionAsset(
    asset_type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

DH_heat_pump_HT_S = TransportHeatConversionAsset(
    asset_type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degc=90,
    ambientTempType="GROUND",
)

DH_boiler_L = ChemicalHeatConversionAsset(
    asset_type="BOILER",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=100,
)

Industrial_methane_furnace = ChemicalHeatConversionAsset(
    asset_type="METHANE_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)

Industrial_hydrogen_furnace = ChemicalHeatConversionAsset(
    asset_type="HYDROGEN_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)

Building_gas_burner_60kW = ChemicalHeatConversionAsset(
    asset_type="GAS_BURNER",
    capacityHeat_kW=60,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

Building_heatpump_20kW = TransportHeatConversionAsset(
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=20,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)
