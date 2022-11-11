from pydantic import BaseModel, Extra


class EnergyAsset(BaseModel, extra=Extra.forbid):
    # id: str
    # connection_id: str
    # parent_id: str
    # energy_carriers: list[str]
    pass

# class DefaultEnergyAsset(EnergyAsset):
#     name: str
