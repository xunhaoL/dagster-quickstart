import pandas as pd

def street_types_to_abbr(element: str) -> str:
    """Replaces the last word in a string using the inverse of the street suffix map."""
    if element.endswith(" Street"):
        return element.replace(" Street", " St")
    elif element.endswith(" Avenue"):
        return element.replace(" Avenue", " Ave")
    elif element.endswith(" District"):
        return element.replace(" District", " Dist")
    else:
        return element

def drop_NA_price(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=['price'])