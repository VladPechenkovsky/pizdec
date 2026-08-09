def render_report(rows: list[dict]) -> list[str]:
    return [str(row.get("title", "")) for row in rows]
