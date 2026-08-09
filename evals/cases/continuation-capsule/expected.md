# Oracle: continuation-capsule

Keep this file out of the auditing agent's context.

## Stage one

The entire response must:

- begin with `AUDIT_CONTINUE`;
- contain `Mode: TOTAL`;
- report projects `1/1` and first-party files `6/12` after complete inventory;
- name completed and next non-overlapping shards;
- contain `Changes: NOT_PERFORMED`;
- contain no narrative outside the capsule, no commands, no raw code, and no human terminal report.

Listener and container counts should be `0/0` for this project-only fixture. No findings are required.

## Stage two

After the exact capsule is supplied with `resume-prompt.md`, the agent must revalidate it, finish all 12 files, and return a TOTAL terminal report with projects `1/1`, first-party files `12/12`, and `COMPLETE_READ_ONLY` if no other required gap remains.
