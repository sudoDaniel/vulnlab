# app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_all():
    return "This should list all posts in the database.\ntitle, username, created_at, pull via a JOIN"


@app.route("/posts/<int:post_id>")
def get_detailed_post(post_id: int):
    return "a single post's detail page: the post itself, plus all its comments and each comment's author"


@app.route("/users/<int:user_id>")
def get_detailed_user(user_id: int):
    return "a user's profile: username, email, and a list of posts they've authored"


if __name__ == "__main__":
    app.run(debug=True, port=5009)
