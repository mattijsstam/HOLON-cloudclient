from pydantic import BaseModel
from typing import List
from cloudclient.datamodel import GridConnection, GridNode, Actor

class Payload(BaseModel):
    grid_connections: List[GridConnection]
    grid_nodes: List[GridNode]
    actors: List[Actor]
