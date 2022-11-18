import pandas as pd
from pathlib import Path
import json
import cloudclient.datamodel.defaults
from cloudclient.datamodel.toplevel import Payload

ASSET_CATEGORIES = ["CONVERSION", "CONSUMPTION", "PRODUCTION", "STORAGE"]


def sort_columns(df: pd.DataFrame) -> pd.DataFrame:
    to_front = ["category", "type", "dataclassname"]
    return df.reindex(
        [*to_front, *[col for col in df.columns if col not in to_front]], axis=1
    )


def generate_excel(
    payload: Payload,
    file_id: str = None,
    path: Path = None,
) -> None:
    """Generates excel sheets for the given payload (model configuration).

    Args:
        payload (Payload): Model configuration object.
        file_id (str, optional): File ID to prepend to the generated excel sheet file names. Defaults to None.
        path (Path, optional): Folder to export the excel sheets to. Defaults to None.
    """

    if file_id is None:
        file_id = ""
    else:
        file_id = f"{file_id}_"

    if path is None:
        FOLDER = Path("").resolve().absolute()
    else:
        FOLDER = path

    ## excel 01: ASSETS

    assets = [
        pd.DataFrame.from_dict(
            {**json.loads(asset.json()), **{"dataclassname": asset.__class__.__name__}},
            orient="index",
        ).T
        for gridconnection in payload.gridconnections
        for asset in gridconnection.assets
    ]

    df = sort_columns(pd.concat(assets))

    with pd.ExcelWriter(FOLDER / (file_id + "assets.xlsx")) as writer:
        for category in ASSET_CATEGORIES:
            df.query(f"category == '{category}'").dropna(axis=1).to_excel(
                excel_writer=writer, sheet_name=category, index=False
            )

    ## excel 02: CONFIG

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
        ).T.drop("contracts", axis=1)
        for actor in payload.actors
    ]

    actor_df = sort_columns(pd.concat(actors))

    policies = [
        pd.DataFrame.from_dict(
            {
                **json.loads(policy.json()),
                **{"dataclassname": policy.__class__.__name__},
            },
            orient="index",
        ).T
        for policy in payload.policies
    ]

    pol_df = sort_columns(pd.concat(policies))

    contracts = [
        pd.DataFrame.from_dict(
            {
                **json.loads(contract.json()),
                **{
                    "actor_id": actor.id,
                    "dataclassname": contract.__class__.__name__,
                    "category": actor.category.value,
                },
            },
            orient="index",
        ).T
        for actor in payload.actors
        if actor.contracts is not None
        for contract in actor.contracts
    ]

    contract_df = sort_columns(pd.concat(contracts))

    dfs = {
        "gridconnections": gc_df,
        "gridnodes": gn_df,
        "actors": actor_df,
        "policies": pol_df,
        "contracts": contract_df,
    }

    with pd.ExcelWriter(FOLDER / (file_id + "config.xlsx")) as writer:
        for category, df in dfs.items():
            df.to_excel(excel_writer=writer, sheet_name=category, index=False)
    pass


def read_excel():
    pass


def parse_defaults():

    cloudclient.datamodel.defaults.__dict__
