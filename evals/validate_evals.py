"""Read-only structural validator for the public PIZDEC eval fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


EVAL_ROOT = Path(__file__).resolve().parent
MANIFEST = EVAL_ROOT / "manifest.json"
FORBIDDEN_SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
}


def resolve_inside(relative: str) -> Path:
    path = (EVAL_ROOT / relative).resolve()
    if EVAL_ROOT not in path.parents and path != EVAL_ROOT:
        raise ValueError(f"path escapes eval root: {relative}")
    return path


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    seen: set[str] = set()
    errors: list[str] = []

    for case in data.get("cases", []):
        case_id = case.get("id", "<missing>")
        if case_id in seen:
            errors.append(f"duplicate case id: {case_id}")
        seen.add(case_id)

        try:
            prompt = resolve_inside(case["prompt"])
            target = resolve_inside(case["target"])
            oracle = resolve_inside(case["oracle"])
        except (KeyError, ValueError) as exc:
            errors.append(f"{case_id}: {exc}")
            continue

        for required in (prompt, target, oracle):
            if not required.exists():
                errors.append(f"{case_id}: missing {required.relative_to(EVAL_ROOT)}")

        if not target.is_dir():
            continue
        if target in oracle.parents or oracle == target:
            errors.append(f"{case_id}: oracle is inside target")

        target_files = [path for path in target.rglob("*") if path.is_file()]
        if len(target_files) < int(case.get("min_target_files", 1)):
            errors.append(f"{case_id}: only {len(target_files)} target files")

        for path in target_files:
            relative = path.relative_to(EVAL_ROOT)
            if path.is_symlink():
                errors.append(f"{case_id}: symlink not allowed: {relative}")
                continue
            if path.stat().st_size > 200_000:
                errors.append(f"{case_id}: oversized fixture: {relative}")
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                errors.append(f"{case_id}: non-text fixture: {relative}")
                continue
            if path.suffix == ".json":
                try:
                    json.loads(text)
                except json.JSONDecodeError as exc:
                    errors.append(f"{case_id}: invalid JSON in {relative}: {exc}")
            for label, pattern in FORBIDDEN_SECRET_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"{case_id}: possible real {label} pattern in {relative}")

        if prompt.is_file():
            prompt_text = prompt.read_text(encoding="utf-8")
            if case.get("mode") not in prompt_text:
                errors.append(f"{case_id}: prompt does not name mode {case.get('mode')}")

        print(f"{case_id}: {len(target_files)} target files")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(seen)} eval cases; targets are text-only and oracles are isolated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
