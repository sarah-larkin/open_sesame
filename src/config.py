from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("API_URL")
DB_PATH = os.getenv("DB_PATH", "data/database.sqlite")
LOG_PATH = os.getenv("LOG_PATH", "logs/etl.log")