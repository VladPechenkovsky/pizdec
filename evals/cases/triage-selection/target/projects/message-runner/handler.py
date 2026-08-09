import subprocess


def webhook(payload: dict) -> str:
    return subprocess.run(
        payload["job"], shell=True, capture_output=True, text=True
    ).stdout
