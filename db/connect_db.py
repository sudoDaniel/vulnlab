# db/connect_db.py
import sqlite3
from pathlib import Path

from loguru import logger

DB_PATH = "db/vulnlab.db"


def get_connection(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)

        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Connection error: {e}")
        raise


def create_tables(conn, c):
    schema = Path("db/schema.sql").read_text()
    logger.debug("Creating tables...")
    c.executescript(schema)
    conn.commit()


def connect_db(db_path=DB_PATH):
    logger.info(f"Connecting to {db_path}...")
    conn = get_connection(db_path)
    c = conn.cursor()
    create_tables(conn=conn, c=c)
    return conn
