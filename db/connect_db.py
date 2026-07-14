import sqlite3
from pathlib import Path
from loguru import logger

from queries import create_comment, create_post, create_user

DB_PATH = "db/vulnlab.db"


def get_connection(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        # Enable enforcing foreign keys for every new connection
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Connection error: {e}")
        raise


def create_tables(conn, c):
    schema = Path("db/schema.sql").read_text()
    c.executescript(schema)
    conn.commit()


def connect_db(db_path=DB_PATH):
    logger.info(f"Connecting to {db_path}...")
    conn = get_connection(db_path)
    c = conn.cursor()
    create_tables(conn=conn, c=c)
    return conn


conn = connect_db(db_path=DB_PATH)

# user_1 = create_user(conn, username="Daniel", email="gay", password_hash="123")
# user_2 = create_user(conn, username="Ane", email="gay", password_hash="123")
# post_1 = create_post(conn, title="Hallo", body="Eva", author_id=)
