import json
import pandas as pd

from config.logging_config import logger

def transform_youtube_data():

    try:

        with open(
            "data/raw/raw_youtube_data.json",
            "r"
        ) as file:

            raw_data = json.load(file)

        video_list = []

        for item in raw_data["items"]:

            snippet = item["snippet"]
            statistics = item["statistics"]

            video_data = {

                "video_id": item.get("id"),

                "title": snippet.get("title"),

                "channel_title": snippet.get("channelTitle"),

                "published_at": snippet.get("publishedAt"),

                "views": statistics.get("viewCount"),

                "likes": statistics.get("likeCount"),

                "comments": statistics.get("commentCount")

            }

            video_list.append(video_data)

        df = pd.DataFrame(video_list)

        numeric_columns = [
            "views",
            "likes",
            "comments"
        ]

        for col in numeric_columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        df["published_at"] = pd.to_datetime(
            df["published_at"]
        )

        df["engagement_score"] = (
            df["likes"] + df["comments"]
        )

        df.drop_duplicates(
            subset=["video_id"],
            inplace=True
        )
        import os
        os.makedirs("data/processed", exist_ok=True)
        df.to_csv(
            "data/processed/clean_youtube_data.csv",
            index=False
        )

        logger.info(
            "Data transformed successfully!"
        )

        return df

    except Exception as e:

        logger.error(
            f"Error during transformation: {e}"
        )

        raise