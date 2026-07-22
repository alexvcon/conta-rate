import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Config:
    DATABASE = os.getenv("DATABASE", str(BASE_DIR / "database" / "test_db.sqlite3"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"