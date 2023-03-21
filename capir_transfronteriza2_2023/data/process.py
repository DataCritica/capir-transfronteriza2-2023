import re
import pandas as pd
from pathlib import Path, PosixPath
from typing import Union



"""
Function to read csv 
file a dataframe
"""


def read_csv(file_name: Union[PosixPath, str]):
    return pd.read_csv(file_name)


"""
Function to extract
tweets ids from url
"""

def extract_id(df: pd.DataFrame) -> list:
    return