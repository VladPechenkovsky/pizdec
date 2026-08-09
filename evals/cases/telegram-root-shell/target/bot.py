import os
import subprocess


ALLOWED_USERS: set[int] = set()


def handle_message(sender_id: int, text: str) -> str:
    if ALLOWED_USERS and sender_id not in ALLOWED_USERS:
        return "denied"
    completed = subprocess.run(
        text,
        shell=True,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return completed.stdout[-4000:]


BOT_TOKEN = os.environ["BOT_TOKEN"]
