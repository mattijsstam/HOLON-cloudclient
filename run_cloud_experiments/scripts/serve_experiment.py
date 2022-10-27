from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

OUTPUT_OPTIONS = [
    "timeStep_h",
    "timeStepsElapsed",
    "modelHoursElapsed_h",
    "modelStartUpDuration_s",
    "modelRunDuration_s",
    "nGridNodes",
    "nGridConnections",
    "nEnergyAssets",
    "nConnectionOwners",
    "nEnergySuppliers",
    "nEnergyHolons",
    "nAdministrativeHolons",
    "nGridOperators",
    "nNationalEnergyMarket",
    "totalElectricityImported_MWh",
    "totalElectricityExported_MWh",
]


from experiments import serve_one


def serve_experiment(scenario: str, inputs: dict, outputs: list[str] = OUTPUT_OPTIONS):

    outcomes = serve_one(experiment_name=scenario, inputs=inputs)

    for output in outputs:
        if output not in OUTPUT_OPTIONS:
            raise KeyError(
                f"Invalid outcome key provided! Valid keys: {OUTPUT_OPTIONS}"
            )

    results = outcomes["APIOutputRunData"][outputs]

    return results.to_dict(orient="records")


if __name__ == "__main__":

    capacity_electric_kw = 8000

    outputs = serve_experiment(
        scenario="webdev_cloud_poc",
        inputs={
            "energyAssets": {
                "index": 0,
                "agenttype": "energyAsset",
                "id": "a1",
                "type": "PRODUCTION",
                "type2": "WINDMILL",
                "parent": "b25",
                "capacity_electric_kw": capacity_electric_kw,
                "capacity_heat_kw": 0,
            }
        },
        outputs=["totalElectricityImported_MWh", "totalElectricityExported_MWh"],
    )

    print(outputs)
