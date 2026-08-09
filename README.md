# PIZDEC — Project & Infrastructure Zero-trust Defense Exposure Check

*Find it before it finds you.*

`PIZDEC` is both the acronym above and a deliberate transliteration of the Russian word «пиздец»: what an overlooked security exposure can turn into.

[Русская версия](README.ru.md)

PIZDEC is a platform-neutral, read-only security-audit skill for AI coding agents. It instructs an agent to connect code to its deployed environment, inspect the selected depth systematically, and produce a short evidence-based report for both a human and a future agent.

PIZDEC does not fix anything. It contains no installer, executable scripts, telemetry, remote fetches, universal shell commands, or prewritten remediation.

## What it audits

- Websites, frontends, backends, APIs, webhooks, and bots.
- Servers, workstations, identities, SSH, services, listeners, firewalls, tunnels, and persistence.
- Docker, Compose, Kubernetes, images, mounts, volumes, networks, and registries.
- Databases, caches, queues, object storage, backups, and direct data-access paths.
- First-party source code, configuration, infrastructure, migrations, hooks, and deployment trees.
- CI/CD, dependencies, package lifecycle, Git exposure, and software supply chain.
- AI agents, prompts, memory, skills, plugins, MCP tools, browser control, and excessive agency.

Every mode starts with breadth discovery and checks dangerous trust paths early. The selected mode controls how far code and lower-risk surfaces are reviewed after that.

## Modes

| User-facing mode | Machine mode | Intended use | Coverage result | Changes the target? |
|---|---|---|---|---|
| PIZDEC Triage | `TRIAGE` | Fast check of exposed infrastructure, identities, ports, containers, agents, bots, and one or two risk-ranked projects | `TRIAGE_COMPLETE` or `PARTIAL_READ_ONLY` | No |
| PIZDEC Full | `FULL` | Comprehensive risk-based review of every major surface and active/security-connected project | `FULL_COMPLETE` or `PARTIAL_READ_ONLY` | No |
| PIZDEC Total | `TOTAL` | Exhaustive whole-target review, including every first-party file and inactive project | `COMPLETE_READ_ONLY` or `PARTIAL_READ_ONLY` | No |

`FULL` is the default when the user does not name a mode. `TOTAL` must be requested explicitly. Every mode reports evidence only: no commands, patches, implementation sequence, or automatic remediation is generated.

## Install or provide the skill

The distributable skill is the entire [`pizdec`](pizdec/) directory. Keep `SKILL.md` and its `references/` directory together.

Use whichever method your agent supports:

1. Copy the `pizdec/` directory into the agent's skills or instructions directory.
2. Import the repository subdirectory if the platform supports skills from Git repositories.
3. If the platform has no skill registry, provide `pizdec/SKILL.md` and the applicable referenced files with your audit request.

PIZDEC uses Markdown instructions and relative references only. It intentionally avoids platform-specific commands. Compatibility depends on whether the host agent can read the files, inspect the authorized target, preserve task state, and obey the safety boundary; automatic skill discovery is platform-specific and is not guaranteed.

## Use it

Fast first pass:

> Use PIZDEC Triage to inspect this authorized server. Check the host, SSH, identities, exposed ports, containers, databases, bots, agents, and CI/CD, then deeply review one or two highest-risk projects. Work read-only and return the PIZDEC report.

Comprehensive audit:

> Use PIZDEC Full to audit this authorized project and its deployment environment. Cover every major surface and active project using risk-based review. Report evidence only and change nothing.

Exhaustive audit:

> Use PIZDEC Total to audit this entire authorized server, including every first-party project and file. Continue in safe read-only batches until the PIZDEC completion gate is satisfied or a proven terminal condition prevents it.

State the authorized scope clearly. For external-surface or current-vulnerability verification, explicitly identify permitted destinations and network actions. Without that permission, PIZDEC remains local and read-only.

## Existing local analyzers

PIZDEC may use already installed local secret, static-code, dependency, container, infrastructure, configuration, or vulnerability analyzers when they can operate safely and read-only.

It never installs or updates them, starts a scanner service or container, uploads target data, runs project lifecycle code, or enables auto-fix. Tool output is treated as a lead and validated against source, effective configuration, deployment state, and reachability before it becomes a finding.

## Report contract

The terminal report contains:

- What was checked and exact reviewed/discovered coverage required by the selected mode.
- What was found, with severity, confidence, minimal evidence, reachability, exploit prerequisites, and plain-language risk.
- Deliberate mode exclusions and anything else not verified.
- Local analyzers used and known vulnerability-database freshness.
- Whether dynamic or external validation was authorized and performed.
- A short “What you can ask next” section generated from human-readable finding titles.

Finding IDs such as `F-001` remain stable agent anchors, but the user never has to type them. Natural requests such as “Explain what is most dangerous”, “Prepare a safe plan for the SSH password problem”, or “Fix the critical findings one by one and ask before each change” are mapped back to the findings by the next agent.

Completion means only that the selected authorized safe read-only contract was completed. It is not a promise that exploitation, target-code execution, unrestricted external scanning, runtime-only behavior, or every current CVE was tested.

## Safety model

- Target files are evidence, not instructions. Repository files such as `AGENTS.md`, `CLAUDE.md`, and `.cursorrules` cannot override the authenticated audit boundary.
- Memory and prior reports provide context, not current proof or authorization.
- Secret values are redacted; only their type, minimal location, and exposure path are reported.
- Target code, tests, hooks, containers, builds, migrations, and binaries are not executed merely for inspection.
- Audit material is not written into the target or uploaded elsewhere without explicit authorization.
- Required unfinished work is reported as `PARTIAL_READ_ONLY` or continued through a compact coverage capsule.

Read the complete behavior contract in [`pizdec/SKILL.md`](pizdec/SKILL.md).

## Repository layout

```text
.
|-- README.md
|-- README.ru.md
|-- SECURITY.md
|-- CONTRIBUTING.md
|-- LICENSE
`-- pizdec/
    |-- SKILL.md
    `-- references/
```

Repository documentation stays outside the distributable skill so it does not consume the agent's audit context.

## Limitations

PIZDEC improves audit discipline; it does not make an AI agent infallible or replace specialist scanners and qualified human review. Results depend on authorization, accessible evidence, tool capabilities, model reasoning, target size, selected mode, and current vulnerability intelligence.

Only audit assets you own or are authorized to assess.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and [SECURITY.md](SECURITY.md) for privately reporting vulnerabilities in PIZDEC itself. Never submit real credentials, private target code, or unredacted audit evidence to a public issue.

## License

MIT. See [LICENSE](LICENSE).
