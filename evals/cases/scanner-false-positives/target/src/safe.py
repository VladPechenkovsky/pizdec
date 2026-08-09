import sqlite3
import subprocess


def image_tool_version() -> str:
    completed = subprocess.run(
        ["/usr/bin/convert", "--version"],
        shell=False,
        capture_output=True,
        text=True,
        check=True,
    )
    return completed.stdout


def find_user(db: sqlite3.Connection, email: str):
    return db.execute(
        "SELECT id, email FROM users WHERE email = ?", (email,)
    ).fetchone()
