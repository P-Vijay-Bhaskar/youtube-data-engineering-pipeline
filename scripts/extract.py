import requests
import json

from config.config import (
    API_KEY,
    BASE_URL,
    VIDEOS_ENDPOINT
)

from config.logging_config import logger

def extract_youtube_data():

    try:

        endpoint = BASE_URL + VIDEOS_ENDPOINT

        params = {
            "part": "snippet,statistics",
            "chart": "mostPopular",
            "regionCode": "IN",
            "maxResults": 50,
            "key": API_KEY
        }

        response = requests.get(
            endpoint,
            params=params
        )

        response.raise_for_status()

        data = response.json()

        with open(
            "data/raw/raw_youtube_data.json",
            "w"
        ) as file:

            json.dump(data, file, indent=4)

        logger.info(
            "Raw YouTube data extracted successfully!"
        )

        return data

    except Exception as e:

        logger.error(
            f"Error during extraction: {e}"
        )

        raise