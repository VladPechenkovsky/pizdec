# Security Policy

## Reporting a vulnerability in PIZDEC

Use GitHub's private vulnerability-reporting flow for this repository when available. Do not open a public issue containing an exploit, secret, private target code, or evidence that could identify an audited system.

If private reporting is unavailable, open a minimal public issue stating that you need a private contact channel. Include no sensitive technical details until the maintainer provides one.

Useful reports include:

- A prompt-injection path that can override the skill's authority boundary.
- Behavior that causes mutation, remediation execution, secret disclosure, or unauthorized network access.
- A reproducible way to claim false completion or silently omit an authorized critical surface.
- Hidden data collection, external upload, executable content, or dependency introduced into the distributable skill.

## Scope

This policy covers the PIZDEC instructions and repository packaging. It does not authorize testing third-party targets, and this repository is not a place to publish vulnerabilities discovered in systems audited with PIZDEC.

## Supported version

Until versioned releases are published, only the current default branch is supported. Security fixes will be documented in the relevant commit or release notes.

## Disclosure

Please allow reasonable time for validation and a coordinated fix before public disclosure. The maintainer will acknowledge valid reports through the private GitHub thread when that feature is available.
