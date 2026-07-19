import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE = os.getenv("DATABASE", "database/test_db.sqlite3")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"