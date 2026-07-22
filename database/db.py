import sqlite3

from config import Config


def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.executescript(
        '''CREATE TABLE IF NOT EXISTS amounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_amount DECIMAL(10, 2)
);
       CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payment DECIMAL(10, 2),
            date TEXT
        );
    ''')
    conn.commit()
    conn.close()
