# db/queries.py
import sqlite3
from datetime import datetime

from loguru import logger


def query(conn: sqlite3.Connection, query: str):
    logger.debug("Executing Query:\n")
    print(f"\n{query}\n")
    c = conn.cursor()
    c.execute(query)

    for row in c.fetchall():
        print(row)

    conn.commit()


""" CREATING USERS, POSTS AND COMMENTS """


def create_user(
    conn: sqlite3.Connection,
    username: str,
    email: str,
    password_hash: str,
):

    logger.debug("Creating user {}", username)

    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash),
    )
    conn.commit()
    logger.info(f"User {username} created with id: {c.lastrowid}")

    return c.lastrowid


def create_post(
    conn: sqlite3.Connection,
    title: str,
    body: str,
    author_id: int,
    created_at=None,
):
    if created_at is None:
        created_at = datetime.now()
    logger.debug("Creating post {}", title)
    c = conn.cursor()
    c.execute(
        "INSERT INTO posts (title, body, author_id, created_at) VALUES (?, ?, ?, ?)",
        (title, body, author_id, created_at),
    )
    conn.commit()

    return c.lastrowid


def create_comment(
    conn: sqlite3.Connection,
    body: str,
    author_id: int,
    post_id: int,
    created_at=None,
):
    if created_at is None:
        created_at = datetime.now()

    logger.debug("Creating comment on post {}", post_id)

    c = conn.cursor()
    c.execute(
        "INSERT INTO comments (body, author_id, post_id, created_at) VALUES (?, ?, ?, ?)",
        (body, author_id, post_id, created_at),
    )
    conn.commit()

    return c.lastrowid


""" GET QUERIES """


def get_all_posts(conn: sqlite3.Connection):
    logger.debug("Fetching all posts in the database")
    pass


def get_post_by_id(conn: sqlite3.Connection, post_id: int):
    logger.debug("Fetching details on post_id: {}", post_id)
    pass


def get_comments_for_post(conn: sqlite3.Connection, post_id):
    logger.debug("Fetching comments on post_id: {}", post_id)
    pass


def get_user_by_id(conn: sqlite3.Connection, user_id: int):
    logger.debug("Fetching details on user_id: {}", user_id)
    pass
