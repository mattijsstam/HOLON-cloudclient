import pandas as pd
from pathlib import Path
import json
import cloudclient.datamodel.defaults
import numpy as np

ASSET_CATEGORIES = ["CONVERSION", "CONSUMPTION", "PRODUCTION", "STORAGE"]


def sort_columns(df: pd.DataFrame) -> pd.DataFrame:
    to_front = ["category", "type", "dataclassname"]
    return df.reindex(
        [*to_front, *[col for col in df.columns if col not in to_front]], axis=1
    )


def generate_excel():

    assets = [
        pd.DataFrame.from_dict(
            {**json.loads(asset.json()), **{"dataclassname": asset.__class__.__name__}},
            orient="index",
        ).T
        for gridconnection in payload.gridconnections
        for asset in gridconnection.assets
    ]

    df = sort_columns(pd.concat(assets))

    with pd.ExcelWriter("assets.xlsx") as writer:
        for category in ASSET_CATEGORIES:
            df.query(f"category == '{category}'").dropna(axis=1).to_excel(
                excel_writer=writer, sheet_name=category, index=False
            )

    pass


def read_excel():
    pass


def parse_defaults():

    cloudclient.datamodel.defaults.__dict__


from mvp import payload

gridconnections = [
    pd.DataFrame.from_dict(
        {
            **json.loads(gridconnection.json()),
            **{"dataclassname": gridconnection.__class__.__name__},
        },
        orient="index",
    ).T
    for gridconnection in payload.gridconnections
]

gc_df = sort_columns(pd.concat(gridconnections))


# unpack assets to default asset name
gc_df["assets"] = gc_df["assets"].apply(
    lambda assets: [asset["name"] for asset in assets]
)


gridnodes = [
    pd.DataFrame.from_dict(
        {
            **json.loads(gridnode.json()),
            **{"dataclassname": gridnode.__class__.__name__},
        },
        orient="index",
    ).T
    for gridnode in payload.gridnodes
]

gn_df = sort_columns(pd.concat(gridnodes))


actors = [
    pd.DataFrame.from_dict(
        {
            **json.loads(actor.json()),
            **{"dataclassname": actor.__class__.__name__},
        },
        orient="index",
    ).T
    for actor in payload.actors
]

actor_df = sort_columns(pd.concat(actors))

policies = [
    pd.DataFrame.from_dict(
        {
            **json.loads(policie.json()),
            **{"dataclassname": policie.__class__.__name__},
        },
        orient="index",
    ).T
    for policie in payload.policies
]

pol_df = sort_columns(pd.concat(policies))

dfs = {
    "gridconnections": gc_df,
    "gridnodes": gn_df,
    "actors": actor_df,
    "policies": pol_df,
}

with pd.ExcelWriter("config.xlsx") as writer:
    for category, df in dfs.items():
        df.to_excel(
            excel_writer=writer, sheet_name=category, index=False
        )

