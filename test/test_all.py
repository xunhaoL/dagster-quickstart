from pathlib import Path

import pandas as pd
from dagster_quickstart import io

def test_read_csv_from_zip(tmpdir):
    contributions = io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv")
    assert contributions.size == 39505047
