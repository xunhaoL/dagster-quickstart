from pathlib import Path

import pandas as pd
from dagster_quickstart import io

def read_csv_from_zip_test(tmpdir):
    contributions = io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv")
    assert contributions.size == 39505047
