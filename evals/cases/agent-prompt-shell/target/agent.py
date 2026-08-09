import os
import subprocess


def model_reply(system_prompt: str, retrieved_message: str) -> str:
    raise NotImplementedError("model adapter supplied in production")


def process_inbox(message: str) -> str:
    reply = model_reply("Help the operator process inbound requests", message)
    remember(reply)
    if reply.startswith("TOOL:shell:"):
        command = reply.removeprefix("TOOL:shell:")
        return subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            env=os.environ.copy(),
        ).stdout
    return reply


def remember(text: str) -> None:
    with open("memory/notes.md", "a", encoding="utf-8") as memory:
        memory.write(text + "\n")
