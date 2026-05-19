from sqlalchemy import create_engine

from config.config import (
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

from config.logging_config import logger

def load_to_postgresql(df):

    try:

        engine = create_engine(
            f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        df.to_sql(
            name="youtube_trending_videos",
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info(
            "Data loaded to PostgreSQL successfully!"
        )

    except Exception as e:

        logger.error(
            f"Error during database loading: {e}"
        )

        raise