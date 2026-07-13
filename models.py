from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self._password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self._password_hash, password)

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"

    def __repr__(self):
        return f"User(username={self.username!r}, " f"email={self.email!r})"


class Post:
    def __init__(self, title: str, body: str, author: User, id: int, created_at=None):
        self.title = title
        self.body = body
        self.author = author
        self.id = id

        if created_at is not None:
            self.created_at = created_at
        else:
            self.created_at = datetime.now()

    def __repr__(self):
        return (
            f"Post(title={self.title!r}, "
            f"author={self.author!r}, "
            f"id={self.id!r})"
        )


class Comment:
    def __init__(self, body: str, author: User, post: Post, id: int, created_at=None):
        self.body = body
        self.author = author
        self.post = post
        self.id = id

        if created_at is not None:
            self.created_at = created_at
        else:
            self.created_at = datetime.now()

    def __repr__(self):
        return (
            f"Comment(post={self.post!r}, "
            f"author={self.author!r}, "
            f"body={self.body!r}, "
            f"created_at={self.created_at!r})"
        )


daniel = User("Daniel", "dan@man.com", "123")
ane = User("Ane", "ane@ane.com", "123")
my_post = Post("Hello!", "I love cats", author=daniel, id=1)
comment = Comment("LOL", ane, my_post, 1)
print(my_post)
print(comment)
