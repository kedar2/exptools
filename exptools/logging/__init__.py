import pandas as pd
from pathlib import Path

def add_result(result: dict, filename: str = "results/experiment.csv"):
    """
    Add the result of an experiment to a CSV file.
    Any new columns will be added to the CSV file.

    Args:
        result (dict): Dictionary containing the results.
        filename (str, optional): Path to the CSV file. Defaults to "results/experiment.csv".
    """
    # Create directory if it does not exist
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    if Path(filename).exists():
        # If the file already exists, add to it
        df = pd.read_csv(filename)
        df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
    else:
        # If the file does not exist, create it
        df = pd.DataFrame([result])

    # Save the file
    df.to_csv(filename, index=False)

def merge_results(filename1: str, filename2: str, merged_filename: str = "results/experiment.csv"):
    """
    Merge two CSV files containing experiment results.

    Args:
        filename1 (str): Path to the first CSV file.
        filename2 (str): Path to the second CSV file.
        merged_filename (str, optional): Path to the merged CSV file. Defaults to "results/experiment.csv".
    """

    # Load the CSV files
    df1 = pd.read_csv(filename1)
    df2 = pd.read_csv(filename2)

    # Merge the CSV files
    df = pd.concat([df1, df2], ignore_index=True)

    # Save the file
    df.to_csv(merged_filename, index=False)


if __name__ == "__main__":
    merge_results("results/results1.csv", "results/results2.csv")