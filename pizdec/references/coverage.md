# Coverage and Completion Gate

Use this profile for every audit.

## Breadth-first inventory

Discover the full authorized surface before deep review:

- Hosts, users, groups, privilege paths, interfaces, firewall, routes, listeners, services, jobs, startup, and persistence.
- Process executables, redacted command lines, service definitions, working directories, configuration sources, environment-variable names, extensions, and writable search paths.
- Containers, images, orchestrators, networks, ports, volumes, secret sources, registries, and builds.
- Git and non-Git project roots, nested repositories, service directories, web roots, deployment trees, automation folders, and mounted code.
- Manifests, locks, CI/CD, infrastructure, migrations, schemas, proxies, databases, queues, caches, storage, backups, agents, skills, plugins, MCP, and bots.
- Hidden files, symlinks, submodules, patches, hooks, history indicators, archives, backups, and binaries that affect execution.

Derive additional roots from current processes, service managers, container mounts, proxies, schedulers, shell profiles, deployments, and agent configuration. Do not rely on common directories.

## Coverage ledger

Track at least:

| Surface | Discovered | Reviewed | State | Evidence or gap |
|---|---:|---:|---|---|
| Hosts | | | | |
| External listeners/services | | | | |
| Containers/workloads | | | | |
| First-party projects | | | | |
| First-party files | | | | |
| Databases/data services | | | | |
| CI/CD and scheduled automation | | | | |
| Agents/tools/plugins | | | | |
| Secret locations and history | | | | |

Use states `reviewed`, `partially reviewed`, `not accessible`, and `not applicable`. A severe finding does not complete unread branches.

Maintain these passes: inventory; host/services; containers/data; projects/code; agents/supply chain; cross-boundary synthesis. Do not enter final synthesis with a required pass unfinished unless the terminal result is `PARTIAL_READ_ONLY`.

## File coverage

For every project:

1. Enumerate and classify all files before reading them.
2. Review critical-path files first, then read every first-party and unknown-copied source, configuration, infrastructure, migration, template, script, hook, and security-relevant documentation file.
3. Review large files in chunks and record completion; never infer an unread remainder.
4. Inspect binary metadata, provenance, locally available signatures or hashes, permissions, execution paths, and consumers without executing it.
5. Exclude vendor/generated material from line-by-line review only after assessing provenance, integrity, lock state, modifications, lifecycle hooks, and executable entrypoints.

Do not count `.git` internals, dependency trees, virtual environments, package caches, generated builds, compiled output, or media as first-party after confirming their role. Review local patches, target-facing integrations, manifests, locks, hooks, and privileged tool declarations. Inactive first-party projects remain in scope.

Search results are discovery aids. Mark a file `reviewed` only after understanding its security-relevant role and logic.

## Shard large audits

Partition by non-overlapping infrastructure surface, project root, trust boundary, component, or directory. Use one project root per worker unless tightly related projects are small enough to share a shard. Keep shared entrypoints and cross-component paths for coordinator synthesis.

Size a shard by usable context, not an arbitrary file count:

- If context capacity is known, target no more than 20% of a worker's context for source payload so instructions, analysis, and output still fit.
- Otherwise, target about 50,000 source characters and no more than 100 first-party/security-relevant files. File count is a fallback ceiling, not the primary measure.
- Give a large or dense file its own shard when necessary. Split the rest by non-overlapping trust boundary, component, directory, or explicit file batch.
- Run an inventory-only shard first when counts or ownership are unknown.

Each shard records:

| Shard | Assigned root or surface | Discovered | Reviewed | Excluded | State | Gap |
|---|---|---:|---:|---:|---|---|
| | | | | | | |

Give workers the same authority boundary, secret redaction, no-execution, and no-remediation rules. Require only assigned scope, numeric counts, justified exclusions, unfinished items, evidence-backed findings, and inaccessible surfaces. Workers never declare global completion.

Keep the authoritative ledger in the coordinating context. Reconcile duplicates, late roots, exclusions, and unfinished work. A partial worker result creates smaller follow-up shards while continuation is possible. Review shared identities, credentials, proxies, queues, databases, deployment tokens, and agent tools across shard boundaries.

If delegation is unavailable, process the same shards sequentially through the runtime's native continuation mechanism. Do not require a vendor-specific user command.

## Completion statuses

Use `COMPLETE_READ_ONLY` only when:

- Every listener maps to a reviewed owner, effective authentication, privilege path, and exposure boundary or is explicitly out of scope.
- Every applicable host, container, code, web/data, and agent/supply-chain profile is complete.
- Every first-party project is understood and every first-party file is reviewed.
- Effective authentication, authorization, privilege, data, and deployment paths are known.
- No required read-only critical surface is inaccessible or merely sampled.
- Integer reviewed/discovered counts exist for listeners, containers, projects, and first-party files.

`COMPLETE_READ_ONLY` means complete within the authorized safe read-only scope. It never implies execution of target code, exploitation, unrestricted external scanning, full vulnerability-database freshness, or absence of runtime-only defects. State dynamic/external validation separately using the field defined in `SKILL.md`.

If a completion condition fails, use `PARTIAL_READ_ONLY`, name every gap, and avoid claiming that no additional critical or high risks exist. An incomplete ledger is an instruction to continue while safe authorized inspection or supported continuation remains.

## Terminal conditions

Use `NONE` for `COMPLETE_READ_ONLY`. A terminal `PARTIAL_READ_ONLY` report may use only:

- `ACCESS_DENIED`: authorized non-interactive read-only privilege still cannot inspect the named surface.
- `USER_LIMIT_REACHED`: an explicit user time, cost, scope, or tool limit was reached.
- `RUNTIME_LIMIT_REACHED`: an observed hard context, turn, worker, execution, or availability limit remains after supported continuation is exhausted.
- `PROHIBITED_VERIFICATION`: remaining evidence requires mutation, credential guessing, exploitation, secret disclosure, or unauthorized external access.

Large file counts, elapsed time, concise findings, anticipated limits, or an already confirmed severe issue are not terminal conditions. A code applies globally only after every other safely inspectable row is complete. A prohibited external check never excuses unread local code; an inaccessible path never excuses other accessible paths.

Before reporting, apply this state machine:

```text
if any safely inspectable ledger item is unfinished:
    continue or create a follow-up shard
    if the current context must end and native resume exists: emit AUDIT_CONTINUE
    otherwise do not emit a human report
elif required coverage counts are missing or non-numeric:
    reconstruct the ledger; do not report
elif no coverage gap remains:
    report COMPLETE_READ_ONLY with stop code NONE
elif every remaining gap is covered by one evidenced allowed terminal code:
    report PARTIAL_READ_ONLY with that code
else:
    continue safely or state each incompatible terminal gap without claiming completion
```

## Continuation protocol

When a context must end but the task can resume, emit this capsule instead of a human report:

```text
AUDIT_CONTINUE
Mode: <SAFETY or FULL_DRAFT>
Coverage: listeners <reviewed>/<discovered>; containers <reviewed>/<discovered>; projects <reviewed>/<discovered>; first-party files <reviewed>/<discovered>
Reconciled changes: <integer additions/removals/reclassifications and evidence; or NONE>
Completed shards: <identifiers>
Next shards: <non-overlapping identifiers and boundaries>
Confirmed findings retained: <finding IDs and severities only>
Remediation: NOT_PERFORMED
```

The capsule must be the entire visible response, begin with `AUDIT_CONTINUE`, contain integer ledger-derived pairs, and contain no narrative, commands, secret values, or raw code. It is not a terminal result. On resume, reload this skill and applicable profiles, verify the capsule against native task state, and continue.

Inventory and classify a newly discovered root before handoff so no denominator is unknown. Compare each capsule to its predecessor and explain every denominator change caused by discovery, deduplication, or evidenced reclassification. Silent changes invalidate the capsule.
