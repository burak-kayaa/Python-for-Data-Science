import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a DataFrame from a CSV file and write dimensions to the console

    Parameters
    ----------
    path : str
        The path to the CSV file

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
