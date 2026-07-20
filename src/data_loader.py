import pandas as pd
from src.config import DATA_PATH as CLEANED_DATA_PATH

def load_dataset():
    """
    Load the cleaned dataset from the specified path.
    Returns:
        DataFrame: Loaded dataset
    """
    try:
        df = pd.read_csv(CLEANED_DATA_PATH)
        return df
    except FileNotFoundError:
        print(f"File not found at {CLEANED_DATA_PATH}. Please check the path.")
        return pd.DataFrame()  # Return an empty DataFrame if file not found