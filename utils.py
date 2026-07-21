# utils.py
import sqlite3

from loguru import logger


def get_all_tables(conn: sqlite3.Connection):
    tables = [
        row[0]
        for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
    ]

    return tables


def delete_all_tables(conn: sqlite3.Connection):
    logger.warning("Deleting all tables...")

    conn.execute("PRAGMA foreign_keys = OFF")
    tables = get_all_tables(conn)
    for table in tables:
        conn.execute(f"DELETE FROM {table}")

    conn.execute("PRAGMA foreign_keys = ON")
    conn.commit()


def display_tables(conn: sqlite3.Connection):

    tables = get_all_tables(conn)
    for table in tables:
        logger.info(f"\n=== {table.upper()} ===")

        cursor = conn.execute(f"SELECT * FROM {table}")

        # Columns
        print([description[0] for description in cursor.description])

        # Rows
        for row in cursor.fetchall():
            print(row)
