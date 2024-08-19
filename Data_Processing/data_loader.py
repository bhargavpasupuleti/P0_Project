import pandas as pd

def load_json_data(file_path):
    """Load data from a JSON file into a pandas DataFrame."""
    return pd.read_json(file_path)
