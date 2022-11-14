import pandas as pd
from pathlib import Path


if __name__ == "__main__":

    from cloudclient.datamodel import (
        Payload,
        Actor,
    )

    actors = [
        Actor(actor_type="CONNECTIONOWNER", id="com1", parent_actor="hol1"),
        Actor(actor_type="CONNECTIONOWNER", id="com2", parent_actor="hol1"),
        Actor(actor_type="CONNECTIONOWNER", id="com3", parent_actor="hol1"),
        Actor(actor_type="ENERGYSUPPLIER", id="sup1", parent_actor="nat"),
        Actor(actor_type="ENERGYHOLON", id="hol1", parent_actor="sup1"),
        Actor(actor_type="GRIDOPERATOR", id="o1", parent_actor="nat"),
    ]

    from cloudclient.datamodel.defaults import (
        Logistics_fleet_hgv_E,
        Solarpanels_1MW,
        Grid_battery_10MWh,
        Building_solarpanels_0kWp,
        Building_gas_burner_60kW,
    )

    from cloudclient.datamodel.gridconnections import (
        IndustryGridConnection,
        BuildingGridConnection,
        ProductionGridConnection,
    )

    grid_connections = [
        BuildingGridConnection(
            insulation_label="NONE",
            heating_type="GASBURNER",
            grid_type="LOGISTICS",
            owner_actor="com1",
            parent_electric="E2",
            id="b1",
            capacity_kw=2000,
            assets=[
                Logistics_fleet_hgv_E,
                Building_solarpanels_0kWp,
                Building_gas_burner_60kW,
            ],
        ),
        IndustryGridConnection(
            heating_type="GASBURNER",
            grid_type="INDUSTRY_OTHER",
            owner_actor="com2",
            parent_electric="E2",
            id="b2",
            capacity_kw=1000,
            assets=[Building_solarpanels_0kWp, Building_gas_burner_60kW],
        ),
        ProductionGridConnection(
            grid_type="SOLARFARM",
            owner_actor="com3",
            parent_electric="E2",
            id="b3",
            capacity_kw=2000,
            assets=[Solarpanels_1MW, Solarpanels_1MW],
        ),
        ProductionGridConnection(
            grid_type="GRIDBATTERY",
            owner_actor="com4",
            parent_electric="E2",
            id="b4",
            capacity_kw=1000,
            assets=[Grid_battery_10MWh],
        ),
    ]

    from cloudclient.datamodel.gridnodes import ElectricGridNode

    grid_nodes = [
        ElectricGridNode(
            id="E2", parent="E1", owner_actor="o1", capacity_kw=1200, grid_type="MSLS"
        ),
        ElectricGridNode(
            id="E1", owner_actor="o1", capacity_kw=500000, grid_type="HSMS"
        ),
    ]

    from cloudclient.datamodel.config import HOLONConfig

    config = HOLONConfig(
        parameters={
            "EV_charging_attitude_standard": {
                "value": "CHEAP",
                "unit": None,
                "comment": "charging behaviour not contingent on holon",
            },
            "Grid_MS_congestion_allowance_level_kW": {
                "value": "3",
                "unit": "kW",
                "comment": "gridOperator policy variable",
            },
            "Grid_MS_congestion_price": {
                "value": "0.5",
                "unit": "kW",
                "comment": "gridOperator policy value",
            },
            "Grid_MS_congestion_threshold": {
                "value": "0.7",
                "unit": "fr",
                "comment": "gridOperator policy value",
            },
            "Grid_MS_congestion_pricing_consumption": {
                "value": "TRUE",
                "unit": None,
                "comment": "gridOperator policy value",
            },
            "Grid_MS_congestion_pricing_production": {
                "value": "FALSE",
                "unit": None,
                "comment": "gridOperator policy value",
            },
        }
    )
    payload = Payload(
        actors=actors,
        grid_connections=grid_connections,
        grid_nodes=grid_nodes,
        config=config,
    )
    import json

    fp = Path(__file__).parent / "doc" / "assets" / "example.json"
    
    with open(fp, "w") as outfile:
        json.dump(json.loads(payload.json()), outfile, indent=4)
