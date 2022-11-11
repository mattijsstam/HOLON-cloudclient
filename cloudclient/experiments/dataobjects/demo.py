from gridconnections import GridConnection
from assets import ChemicalHeatConversionAsset

from assets.defaults.consumption_defaults import House_hot_water


grid = GridConnection(
    id="g1",
    owner_actor="o1",
    capacity_kw=1500,
    parent_electric="b1",
    assets=[House_hot_water],
)
