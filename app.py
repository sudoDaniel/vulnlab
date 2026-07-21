# app.py
from flask import Flask, redirect, render_template, url_for

from db.connect_db import connect_db
from db.queries import (
    get_all_posts,
    get_comments_for_post,
    get_post_by_id,
    get_user_by_id,
)

app = Flask(__name__)

DB_PATH = "db/vulnlab.db"
conn = connect_db(db_path=DB_PATH)


@app.route("/")
def get_all(conn=conn):
    # return "This should list all posts in the database, title, username, created_at, pull via a JOIN"
    df = get_all_posts(conn=conn)
    print(df)
    return render_template(
        "index.html",
        columns=df.columns.tolist(),
        rows=df.to_dict(orient="records"),
    )


@app.route("/posts/<int:post_id>")
def get_detailed_post(post_id: int):
    # return "a single post's detail page: the post itself, plus all its comments and each comment's author"
    df = get_post_by_id(conn=conn, post_id=post_id)
    return render_template(
        "posts.html",
        columns=df.columns.tolist(),
        rows=df.to_dict(orient="records"),
    )


@app.route("/users/<int:user_id>")
def get_detailed_user(user_id: int):
    return "a user's profile: username, email, and a list of posts they've authored"


if __name__ == "__main__":
    # DB_PATH = "db/vulnlab.db"
    DEBUG = True
    # conn = connect_db(db_path=DB_PATH)
    # posts = get_all_posts(conn=conn)
    post = get_post_by_id(conn=conn, post_id=1)
    print("POST!!!!!!!!")
    print("bare post:")
    print(post)
    app.run(debug=DEBUG, port=5009)
