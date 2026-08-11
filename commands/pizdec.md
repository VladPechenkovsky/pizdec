---
description: PIZDEC read-only security audit — /pizdec triage|full|total [scope]
argument-hint: triage|full|total [scope]
---

Load and follow the `pizdec` skill: read its `SKILL.md` and every applicable file under its `references/` directory, then obey its contract exactly — strictly read-only, no fixes, the authority boundary, the completion gate, and the terminal report format.

Parse `$ARGUMENTS`:

- First word `triage`, `full`, or `total` selects the machine mode TRIAGE, FULL, or TOTAL.
- First word `help` (or `--help`): print the three modes with one-line coverage summaries and example invocations, then stop without auditing.
- Empty arguments: run `full` on the current working directory.
- An unrecognized first word is ambiguous — never silently pick a mode. Stop and ask whether it was a mistyped mode or a scope (with `full` as the default), or print help.
- Everything after the mode word is the user-authorized audit scope. If it is empty, the scope is the current working directory only; state that assumption in one line before starting. Extending the audit to the deployment environment, external surfaces, or current-vulnerability checks requires explicit user confirmation. If the intended scope is genuinely ambiguous, ask before auditing.

Run the audit at the selected depth and produce the terminal PIZDEC report in the user's language. Change nothing.
