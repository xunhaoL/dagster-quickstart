import io
import pathlib
import zipfile

import pandas as pd
import requests
import csv

def read_csv_from_zip(zip_file_path: pathlib.Path, csv_path: pathlib.Path) -> pd.DataFrame:
    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract the CSV file
        return zip_ref.extractall()
