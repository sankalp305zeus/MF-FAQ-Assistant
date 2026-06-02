# Repo Rescue

<!-- Activate: set Mode: repo-rescue in CONTEXT.md -->
<!-- Maya reads this, then activates Atlas → Forge → Sentinel on demand. -->

## When to use

- Inherited codebase with no documentation
- Abandoned repo you want to revive
- Working project with accumulated tech debt
- Build that broke and nobody knows why

## Workflow

### Phase 1 — Assess (activate Atlas)

1. Read existing context: README, docs, package.json / requirements.txt, CI config
2. Map architecture: major components, data flow, external dependencies
3. Audit dependencies: outdated, deprecated, or vulnerable packages
4. Identify failures: build errors, broken tests, runtime crashes
5. Scope estimate: fix (hours) / recovery (days) / rewrite (weeks)

**Output:** Fill `CONTEXT.md` from findings. Update `STATE.md`. Write architecture findings to `log/`.

### Phase 2 — Recovery plan (Atlas proposes, Maya reviews)

6. Produce ordered recovery plan: fixes, dependency updates, missing pieces
7. Tag each item: quick-fix / medium / significant
8. Flag risks: what could break during recovery

**Output:** Update `NEXT.md` with first recovery action. Log plan in `log/`.

### ⛔ Approval gate — human reviews recovery plan before any execution

### Phase 3 — Execute (activate Forge)

9. Fix in dependency order: environment → dependencies → build → tests → features
10. Verify each fix: run tests after each change, not at the end
11. Document deviations in `log/`

### Phase 4 — Verify (activate Sentinel)

12. Run existing tests — compare pass rate before vs. after
13. Smoke test core flows end-to-end
14. Security scan: exposed secrets, broken auth, open ports

**Output:** Verdict in `log/`: recovered / partially-recovered / needs-rewrite

## Token discipline

- Atlas reads file tree + key config files first, not all source code
- Load source files one at a time when investigating a specific issue
- Never dump an entire codebase into context
