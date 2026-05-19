from scripts.extract import extract_youtube_data
from scripts.transform import transform_youtube_data
from scripts.load import load_to_postgresql

from config.logging_config import logger

def run_pipeline():

    try:

        extract_youtube_data()

        df = transform_youtube_data()

        load_to_postgresql(df)

        logger.info(
            "Full ETL Pipeline executed successfully!"
        )

    except Exception as e:

        logger.critical(
            f"Pipeline failed: {e}"
        )

if __name__ == "__main__":
    run_pipeline()