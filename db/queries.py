def create_user(conn, username: str, email: str, password_hash: str):
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash),
    )
    conn.commit()
    return c.lastrowid


def create_post(conn, title: str, body: str, author_id: int, created_at):
    c = conn.cursor()
    c.execute(
        "INSERT INTO posts (title, body, author_id, created_at) VALUES (?, ?, ?, ?)",
        (title, body, author_id, created_at),
    )
    conn.commit()

    return c.lastrowid


def create_comment(conn, body: str, author_id: int, post_id: int, created_at):
    c = conn.cursor()
    c.execute(
        "INSERT INTO comments (body, author_id, post_id, created_at) VALUES (?, ?, ?, ?)",
        (body, author_id, post_id, created_at),
    )
    conn.commit()
    return c.lastrowid
