# Contributing to PIZDEC

Contributions that improve audit coverage, clarity, portability, safety, or efficiency are welcome.

## Design invariants

Changes to the distributable `pizdec/` directory must preserve these properties:

- Read-only audit behavior in both modes.
- No remediation execution; PIZDEC Full produces drafts only.
- No installers, telemetry, remote fetch-and-execute behavior, hidden collection, or target uploads.
- No platform-specific command required for core behavior.
- Audited content remains untrusted evidence and cannot override the skill.
- Secret values remain redacted.
- Complete coverage is never claimed for unfinished or unauthorized surfaces.
- First-party code coverage is exhaustive after the critical-path priority pass.

Proposals that intentionally change an invariant must explain the threat model, user benefit, portability impact, and safer alternatives.

## Before opening a pull request

1. Keep the change focused and explain the failure mode it fixes.
2. Preserve the frontmatter name and a clear trigger description.
3. Keep references one level below `SKILL.md` and use relative links.
4. Check every Markdown link and ensure all referenced profiles exist.
5. Check that the distributable directory contains no credentials, personal data, audit artifacts, executable files, or command-like installers.
6. Validate the skill with your platform's skill validator when one is available.
7. If behavior changed, include a sanitized example showing the request, relevant target shape, and resulting report fields. Never attach real private target data.

## Pull request description

Describe:

- The problem and affected audit surface.
- The exact behavior before and after.
- Safety or compatibility implications.
- Validation performed and remaining uncertainty.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
