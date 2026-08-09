# PIZDEC

**Project & Infrastructure Zero-trust Defense Exposure Check**

*Find it before it finds you.*

[Русская версия](README.ru.md)

PIZDEC is a platform-neutral security-audit skill for AI coding agents. It instructs an agent to inspect an authorized project or host deeply, connect code to its deployed environment, and produce a short evidence-based report for both a human and a future fixing agent.

PIZDEC does not fix anything by itself. It does not contain an installer, executable scripts, telemetry, remote fetches, or universal shell commands.

## What it audits

- Websites, frontends, backends, APIs, webhooks, and bots.
- Servers, workstations, identities, SSH, services, listeners, firewalls, tunnels, and persistence.
- Docker, Compose, Kubernetes, images, mounts, volumes, networks, and registries.
- Databases, caches, queues, object storage, backups, and direct data-access paths.
- First-party source code, configuration, infrastructure, migrations, hooks, and deployment trees.
- CI/CD, dependencies, package lifecycle, Git exposure, and software supply chain.
- AI agents, prompts, memory, skills, plugins, MCP tools, browser control, and excessive agency.

The audit starts with breadth discovery, checks the most dangerous trust paths early, and then completes exhaustive read-only review of first-party files and applicable infrastructure surfaces.

## Modes

| User-facing mode | Machine mode | Result | Changes the target? |
|---|---|---|---|
| PIZDEC Safety | `SAFETY` | Findings, evidence, recommendations, and acceptance criteria | No |
| PIZDEC Full | `FULL_DRAFT` | The same audit plus snapshot-bound remediation drafts for confirmed, high-confidence Critical/High findings | No |

Neither mode authorizes execution. Any fix requires a separate, current user approval, and the executing agent must revalidate the environment first.

## Install or provide the skill

The distributable skill is the entire [`pizdec`](pizdec/) directory. Keep `SKILL.md` and its `references/` directory together.

Use whichever method your agent supports:

1. Copy the `pizdec/` directory into the agent's skills or instructions directory.
2. Import the repository subdirectory if the platform supports skills from Git repositories.
3. If the platform has no skill registry, provide `pizdec/SKILL.md` and the applicable referenced files to the agent with your audit request.

PIZDEC uses Markdown instructions and relative references only. It intentionally avoids platform-specific tool names and installation commands. Compatibility depends on whether the host agent can read the files, inspect the authorized target, preserve task state, and obey the safety boundary; automatic skill discovery is platform-specific and is not guaranteed.

## Use it

Safety audit example:

> Use PIZDEC in Safety mode to audit this entire authorized server. Work read-only, use relevant trusted conversation context and memory, inspect every discovered first-party project, and return the PIZDEC report. Do not change anything.

Remediation-ready audit example:

> Use PIZDEC Full to audit this authorized project and its deployment environment. Draft remediation only where PIZDEC permits it. Do not execute any fix.

State the authorized scope clearly. For external-surface or current-vulnerability verification, explicitly identify which destinations and network actions are authorized. Without that permission, PIZDEC remains local and read-only.

## Report contract

The terminal report is deliberately short:

- What was checked and exact reviewed/discovered coverage.
- What was found, with severity, confidence, minimal evidence, reachability, and exploit prerequisites.
- A decision-ready recommendation and observable acceptance criteria for each root cause.
- What was not verified and why.
- Whether dynamic or external validation was authorized and performed.

`COMPLETE_READ_ONLY` means the authorized safe read-only surface was completed. It is not a promise that exploitation, target code execution, unrestricted external scanning, or every current CVE was tested.

In PIZDEC Full, remediation packages are tied to the audit snapshot and marked `NOT_EXECUTED` and `APPROVAL_REQUIRED`. The skill itself contains no ready-made environment-changing commands.

## Safety model

- Target files are evidence, not instructions. Repository files such as `AGENTS.md`, `CLAUDE.md`, and `.cursorrules` cannot override the audit boundary.
- Memory and prior reports provide context, not current proof or authorization.
- Secret values are redacted; only their type, minimal location, and exposure path are reported.
- Target code, tests, hooks, containers, builds, migrations, and binaries are not executed merely for inspection.
- Audit material is not written into the target or uploaded elsewhere without explicit authorization.
- Incomplete work is reported as `PARTIAL_READ_ONLY` or continued through a compact, numeric coverage capsule.

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

Repository documentation is kept outside the distributable skill so it does not consume the agent's audit context.

## Limitations

PIZDEC improves audit discipline; it does not make an AI agent infallible. Results depend on authorization, accessible evidence, tool capabilities, model reasoning, target size, and current vulnerability intelligence. Validate severe findings before making production changes and use qualified human review for high-risk systems.

Only audit assets you own or are authorized to assess.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for changes and [SECURITY.md](SECURITY.md) for privately reporting vulnerabilities in PIZDEC itself. Never submit real credentials, private target code, or unredacted audit evidence to a public issue.

## License

MIT. See [LICENSE](LICENSE).
