import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3/"
VIDEOS_ENDPOINT = "videos"

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
