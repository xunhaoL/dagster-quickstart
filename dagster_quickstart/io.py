import io
import pathlib
import zipfile

import pandas as pd
import requests

def read_single_csv(csv_path: pathlib.Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)