from pydantic import BaseModel, Extra
from typing import Mapping, Union


class HOLONConfig(BaseModel, extra=Extra.forbid):
    parameters: Mapping[str, Mapping[str, Union[str, None]]]
