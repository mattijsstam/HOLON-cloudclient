from cloudclient.datamodel import (
    ElectricCoversionAsset,
    ChemicalHeatConversionAsset,
    TransportHeatConversionAsset,
)

House_heatpump_MT_S = TransportHeatConversionAsset(
    name="House_heatpump_MT_S",
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=4,
    eta_r=0.5,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_heatpump_MT_M",
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_L = TransportHeatConversionAsset(
    name="House_heatpump_MT_L",
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=11,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_gas_burner = ChemicalHeatConversionAsset(
    name="House_gas_burner",
    asset_type="GAS_BURNER",
    capacityHeat_kW=30,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

House_DH_heatdeliveryset = ChemicalHeatConversionAsset(
    name="House_DH_heatdeliveryset",
    asset_type="HEAT_DELIVERY_SET",
    capacityHeat_kW=10,
    eta_r=0.99,
    deliveryTemp_degc=90,
)

Electrolyser = ElectricCoversionAsset(
    name="Electrolyser",
    asset_type="ELECTROLYSER",
    capacityElectricity_kW=100,
    eta_r=0.6,
)

DH_gas_burner_S = ChemicalHeatConversionAsset(
    name="DH_gas_burner_S",
    asset_type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

DH_heat_pump_HT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    asset_type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degc=90,
    ambientTempType="GROUND",
)

DH_boiler_L = ChemicalHeatConversionAsset(
    name="DH_boiler_L",
    asset_type="BOILER",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=100,
)

Industrial_methane_furnace = ChemicalHeatConversionAsset(
    name="Industrial_methane_furnace",
    asset_type="METHANE_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)

Industrial_hydrogen_furnace = ChemicalHeatConversionAsset(
    name="Industrial_hydrogen_furnace",
    asset_type="HYDROGEN_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)

Building_gas_burner_60kW = ChemicalHeatConversionAsset(
    name="Building_gas_burner_60kW",
    asset_type="GAS_BURNER",
    capacityHeat_kW=60,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

Building_heatpump_20kW = TransportHeatConversionAsset(
    name="Building_heatpump_20kW",
    asset_type="HEAT_PUMP_AIR",
    capacityElectricity_kW=20,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)
