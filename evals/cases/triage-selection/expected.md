# Oracle: triage-selection

Keep this file out of the auditing agent's context.

## Required selection

Select both:

1. `public-admin-api`: public listener, disabled authentication, and a shell-backed admin route.
2. `message-runner`: public webhook, disabled signature verification, and shell execution.

Do not select `batch-worker` merely because it uses the most CPU. Resource consumption is only a tie-breaker after reachability, privilege, triggers, secrets, and destructive capability.

## Required root causes

1. Unauthenticated public admin input reaches a shell command in `public-admin-api`.
2. Unsigned public webhook input reaches a shell command in `message-runner`.

## Calibration expectations

- Report `TRIAGE_COMPLETE` only if all required Triage host/surface checks represented by the snapshot are covered; name missing live firewall, effective runtime, and real external reachability as limitations or use `PARTIAL_READ_ONLY` when treated as required gaps.
- Explicitly name the unselected projects and the deliberate Triage code-depth exclusion.
- Do not deeply review every project and call the result Full.
