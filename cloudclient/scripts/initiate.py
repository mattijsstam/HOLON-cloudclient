import shutil
from pathlib import Path
from os import sys
import os

CONFIG_FOLDER = Path(__file__).parent.parent / "config"


def create_folder():

    print("Initiating cloudclient...")

    # make folders
    Path(".cloudclient/config").mkdir(exist_ok=True, parents=True)
    Path(".cloudclient/input").mkdir(exist_ok=True, parents=True)
    Path(".cloudclient/ouput").mkdir(exist_ok=True, parents=True)

    # move files
    shutil.copy2(
        CONFIG_FOLDER / "config.example.yml", "./.cloudclient/config/config.yml"
    )
    shutil.copy2(
        CONFIG_FOLDER / "experiments.example.yml",
        "./.cloudclient/config/experiments.yml",
    )

    print("Done!")


def greet(naam):

    print(f"Hallo {naam}")

dicto = {"naam": "Jorrit"}

greet(**dicto)