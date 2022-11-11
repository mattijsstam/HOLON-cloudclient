from gridconnections import GridConnection
from assets.consumption import HeatConsumptionAsset


grid = GridConnection(
    id="g1",
    owner_actor="o1",
    capacity_kw=1500,
    parent_electric="b1",
    assets=[
        HeatConsumptionAsset(
            yearlyDemandHeat_kWh=12, asset_type="HOT_WATER_CONSUMPTION"
        )
    ],
)


if __name__ == "__main__":
    import json

    print(json.dumps(json.loads(grid.json()), indent=4))