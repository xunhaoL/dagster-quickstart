import io
import pathlib
import zipfile

import pandas as pd
import requests
import csv

def read_csv_from_zip(zip_file_path: pathlib.Path, csv_filename: str) -> pd.DataFrame:
    # Extract the CSV file from the ZIP archive
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        csv_file_list = [file for file in zip_ref.namelist() if file.endswith('.csv')]
        if not csv_file_list:
            raise ValueError("No CSV file found in the ZIP archive")
        if len(csv_file_list) > 1:
            raise ValueError("Multiple CSV files found in the ZIP archive, specify the exact filename")

        csv_filename_in_zip = csv_file_list[0]
        with zip_ref.open(csv_filename_in_zip) as csv_file:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file)

    return df