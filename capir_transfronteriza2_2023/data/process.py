import re
import pandas as pd
from pathlib import Path, PosixPath
from typing import Union, List, Generator


"""
Function to get csv files
from the path provided
"""


def get_csv_files(dir: Union[PosixPath, str]):
    # Get the csv files from the path provided
    return Path(dir).glob("*.csv")



"""
Function to extract
tweets ids from url
"""

def extract_id(df: pd.DataFrame) -> list:
    return


"""
Function to concatenate
a list of dataframes
"""


def concat_dfs(dfs: List) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)