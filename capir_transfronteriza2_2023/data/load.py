from pathlib import Path, PosixPath
from typing import Union
import pandas as pd
import capir_transfronteriza2_2023.utils.paths as paths

# Inputs
data_raw = paths.data_raw_dir()
data_processed = paths.data_processed_dir()


# Outputs
users = paths.data_raw_dir("users.csv")

