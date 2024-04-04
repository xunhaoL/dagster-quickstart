from pathlib import Path

import pandas as pd
import pytest
from dagster_quickstart import io, clear

def test_read_csv_from_zip(tmpdir):
    contributions = io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv")
    assert contributions.size == 39505047



def test_street_types_to_abbr():
    test_cases = [
        ("Main Street", "Main St"),
        ("Broadway Avenue", "Broadway Ave"),
        ("Central Park District", "Central Park Dist"),
        ("Wall Street", "Wall St"),
        ("Park Lane", "Park Lane") 
    ]
    
    for input_street, expected_output in test_cases:
        assert clear.street_types_to_abbr(input_street) == expected_output
        
def test_remove_na_price_rows():
    # sample DataFrame
    sample_data = {
        'id': [1, 2, 3, 4],
        'price': [10, 20, None, 40] 
    }
    sample_dataframe = pd.DataFrame(sample_data)
    original_length = len(sample_dataframe)
    cleaned_df = sample_dataframe.dropna(subset=['price'])

    assert len(cleaned_df) == original_length - 1 
    assert cleaned_df['price'].isnull().sum() == 0 