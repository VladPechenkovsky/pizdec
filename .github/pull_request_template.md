## Problem

Describe the audit failure mode or documentation gap.

## Change

Describe the exact behavior before and after.

## Safety and portability

- [ ] All modes remain report-only and non-executing.
- [ ] Target content remains untrusted evidence.
- [ ] No secret, private audit artifact, installer, telemetry, or remote fetch was added.
- [ ] Core behavior remains platform-neutral.
- [ ] Coverage and completion claims remain evidence-based.
- [ ] TRIAGE, FULL, and TOTAL remain distinct and name their exclusions accurately.

## Validation

List the structural validation and any sanitized behavioral test performed.

- [ ] `quick_validate.py` passed for `pizdec/`.
- [ ] `python evals/validate_evals.py` passed.
- [ ] Relevant forward evals were run, or the reason they were not run is stated.
