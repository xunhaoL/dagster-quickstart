from pathlib import Path

import pandas as pd
from dagster_quickstart import io

def test_read_single_csv(tmpdir):
    contributions = io.read_single_csv("data/rideshare_kaggle.csv")
    assert contributions.size == 39505047
