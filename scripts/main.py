from scripts.extract import extract_youtube_data
from scripts.transform import transform_youtube_data
from scripts.load import load_to_postgresql

from config.logging_config import logger


def run_pipeline():

    try:

        print("Starting ETL Pipeline...")

        extract_youtube_data()
        print("Extraction complete")

        df = transform_youtube_data()
        print("Transformation complete")

        load_to_postgresql(df)
        print("Load complete")

        logger.info(
            "Full ETL Pipeline executed successfully!"
        )

        print("Pipeline finished successfully")

    except Exception as e:

        logger.critical(
            f"Pipeline failed: {e}"
        )
        raise


if __name__ == "__main__":
    print("MAIN.PY STARTED")
    run_pipeline()