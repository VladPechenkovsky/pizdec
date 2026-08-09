import subprocess


def admin_diagnostic(command: str) -> str:
    return subprocess.check_output(command, shell=True, text=True)
