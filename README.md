# Experiments module

The experiments module allows you to define your experiment in a config file and run one or
multiple experiments sequentially. No more adjusting classes! Based on the existing scripts.

- [Experiments module](#experiments-module)
  - [Installation](#installation)
    - [Conda](#conda)
    - [Pipenv](#pipenv)
  - [Starting up](#starting-up)
  - [Running the module](#running-the-module)
  - [Pipenv support](#pipenv-support)
  - [Data classes](#data-classes)

## Installation

### Conda
This will create and activate the an environment that includes all the requirements.
```bash
# ~/run_cloud_experiments
conda env create -f environment.yml
conda activate anylogicexperiments
```

### Pipenv

```bash
# ~/run_cloud_experiments
pip install --user pipenv
pipenv install
```

## Starting up

Go to the `config` folder and copy the `config.example.yml` file to `config.yml`. Specify
your secret API key to connect to the AnyLogic Cloud there.
```bash
# ~/run_cloud_experiments
cp ./config/config.example.yml ./config/config.yml
```
Go to the `config` folder and copy the `experiments.example.yml` file to `experiments.yml`. Specify
your experiments there
```bash
# ~/run_cloud_experiments
cp ./config/experiments.example.yml ./config/experiments.yml
```

Next define your experiments in the `experiments.yml` file. There is an example there to help you.

## Running the module

The base code for the module is in the `experiments` folder. But you can easily call the module
from the script `run_experiments` in the `scripts` folder. Here you can run one experiment by
specifying its name or all experiments by using the keyword `ALL`.

## Pipenv support

There is also support for pipenv now for the ones that are interested. There is a shortcut to
run the experiments: `pipenv run experiments {experiment_name}`.



Happy experimenting!

## Data classes

Data classes are used to structure and validate data before it is sent to the AnyLogic API. Find the class diagrams below:

1. [Grid connections](htmls\gridconnection_classes.html)
2. [Conversion assets](htmls\conversion_classes.html)
3. [Consumption assets](htmls\consumption_classes.html)
4. [Storage assets](htmls\storage_classes.html)
5. [Production assets](htmls\production_classes.html)
6. [Gridnode assets](htmls\gridnode_classes.html)