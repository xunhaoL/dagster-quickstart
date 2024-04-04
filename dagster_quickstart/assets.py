import json
import requests
from dagster_quickstart import io, clear

import pandas as pd

from dagster import (
    MaterializeResult,
    MetadataValue,
    asset,
)
from dagster_quickstart.configurations import HNStoriesConfig


@asset
def read_csv(config: HNStoriesConfig):
    """Read the csv data we need from zip."""
    return io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv")


#@asset(deps=[read_csv])
#def remove_NA_price(config: HNStoriesConfig) -> MaterializeResult:
    """Get items based on story ids from the HackerNews items endpoint."""
    with open(config.hn_top_story_ids_path, "r") as f:
        hackernews_top_story_ids = json.load(f)

    results = []
    for item_id in hackernews_top_story_ids:
        item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()
        results.append(item)

    df = pd.DataFrame(results)
    df.to_csv(config.hn_top_stories_path)

    return MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(str(df[["title", "by", "url"]].to_markdown())),
        }
    )

@asset(deps=[read_csv])
def remove_NA_price(config: HNStoriesConfig) -> MaterializeResult:
    df = io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv")
    return clear.drop_NA_price(df)

@asset(deps=[remove_NA_price])
def to_abbr(config: HNStoriesConfig) -> MaterializeResult:
    df = clear.drop_NA_price(io.read_csv_from_zip("data/archive.zip","rideshare_kaggle.csv"))
    return clear.street_types_to_abbr(df)

@asset(deps=[remove_NA_price])
def time_normalize(config: HNStoriesConfig):
    return
    
@asset(deps=[to_abbr, time_normalize])
def merge_and_divide(config: HNStoriesConfig):
    return