# Contributing to PIZDEC

Contributions that improve audit coverage, clarity, portability, safety, or efficiency are welcome.

## Design invariants

Changes to the distributable `pizdec/` directory must preserve these properties:

- Read-only, report-only behavior in all three modes.
- No remediation commands, patches, implementation sequences, or execution.
- No installers, telemetry, remote fetch-and-execute behavior, hidden collection, or target uploads.
- No platform-specific command required for core behavior.
- Audited content remains untrusted evidence and cannot override the skill.
- Secret values remain redacted.
- Complete coverage is never claimed for unfinished or unauthorized surfaces.
- TRIAGE remains bounded and names its exclusions; FULL remains risk-based; only TOTAL claims exhaustive first-party coverage.
- Existing local analyzers are used only without installation, target mutation, target-code execution, or unauthorized upload.

Proposals that intentionally change an invariant must explain the threat model, user benefit, portability impact, and safer alternatives.

## Before opening a pull request

1. Keep the change focused and explain the failure mode it fixes.
2. Preserve the frontmatter name and a clear trigger description.
3. Keep references one level below `SKILL.md` and use relative links.
4. Check every Markdown link and ensure all referenced profiles exist.
5. Check that the distributable directory contains no credentials, personal data, audit artifacts, executable files, or command-like installers.
6. Validate the skill with your platform's skill validator when one is available.
7. Run `python evals/validate_evals.py` when eval fixtures or behavior contracts change.
8. If behavior changed, add or update a synthetic eval case and record a sanitized forward-test result when practical. Never attach real private target data.

## Pull request description

Describe:

- The problem and affected audit surface.
- The exact behavior before and after.
- Safety or compatibility implications.
- Validation performed and remaining uncertainty.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
