# seed.py
import sys

from loguru import logger

from db.connect_db import connect_db
from db.queries import (
    create_comment,
    create_post,
    create_user,
    get_all_posts,
    query,
)
from models import User
from utils import delete_all_tables, display_tables

DEBUG = True
DB_PATH = "db/vulnlab.db"


logger.remove()
logger.add(sys.stderr, level="DEBUG" if DEBUG else "INFO")


user_1 = User("A", "A@A.com", "123")
user_2 = User("B", "B@B.com", "123")


conn = connect_db(db_path=DB_PATH)
delete_all_tables(conn)

A = create_user(
    conn=conn,
    username=user_1.username,
    email=user_1.email,
    password_hash=user_1._password_hash,
)

B = create_user(
    conn=conn,
    username=user_2.username,
    email=user_2.email,
    password_hash=user_2._password_hash,
)

post_1 = create_post(
    conn=conn, title="Testpost", body="lol", author_id=A
)
post_2 = create_post(
    conn=conn, title="POST 2", body="hahahaha", author_id=A
)
comment = create_comment(
    conn=conn, body="elendig comment", author_id=B, post_id=post_1
)
comment_2 = create_comment(
    conn=conn, body="elendig", author_id=A, post_id=post_2
)
display_tables(conn)

# get_comments_and_posts = """SELECT comments.body, posts.title
# FROM comments
# JOIN posts ON comments.post_id = posts.id;"""
# query(conn, get_comments_and_posts)

get_comment_and_author_name_by_post_id = """SELECT comments.body, users.username
FROM comments
JOIN users ON comments.author_id = users.id
WHERE comments.post_id = ?;"""


query(conn, get_all_posts)


# get_all_posts(conn=conn)
