import subprocess
from typing import Any
import yaml

def run_with_cfg(filename: str, **kwargs: Any):
    """
    Run a Python script with additional configuration arguments.

    Args:
        filename (str): Path to the Python file.
    """
    args = [f"--{key} {value}" for key, value in kwargs.items()]
    args = " ".join(args)
    subprocess.run(f"python {filename} {args}", shell=True)

def run_sweep(filename: str, sweep: dict):
    """
    Run a Python script with a sweep of configuration arguments.
    E.g. if 
    sweep = {
        "x": [1, 2],
        "y": [4, 5],
    }
    then the script will be run with the following arguments:
    --x 1 --y 4
    --x 1 --y 5
    --x 2 --y 4
    --x 2 --y 5

    Args:
        filename (str): Path to the Python file.
        sweep (dict): Dictionary containing the sweep.
    """
    # Get the keys and values of the sweep
    keys = list(sweep.keys())
    values = list(sweep.values())

    # Get the number of combinations
    n_combinations = 1
    for value in values:
        n_combinations *= len(value)

    # Run the script with each combination of arguments
    for i in range(n_combinations):
        # Get the current combination
        combination = []
        for value in values:
            combination.append(value[i % len(value)])
            i //= len(value)
        combination = dict(zip(keys, combination))

        # Run the script with the current combination
        run_with_cfg(filename, **combination)

def run_sweep_from_yml(filename: str, sweep_filename: str):
    """
    Run a Python script with a sweep of configuration arguments.
    The sweep is loaded from a YAML file.

    Args:
        filename (str): Path to the Python file.
        sweep_filename (str): Path to the YAML file containing the sweep.
    """
    
    with open(sweep_filename, "r") as f:
        sweep = yaml.load(f, Loader=yaml.FullLoader)
    run_sweep(filename, sweep)