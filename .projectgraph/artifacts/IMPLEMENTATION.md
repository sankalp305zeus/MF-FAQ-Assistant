# Implementation Plan

<!-- AI: read this when estimating effort or sequencing work. -->
<!-- Rule: do not start a phase until the previous phase's exit criteria are met. -->

## Phase map

| Phase | Scope | Layer / area | Key files |
|-------|-------|--------------|-----------|
| 0 | Setup | Repo + config | Project skeleton, deps, .env.example |
| 1 | [First capability] | [Layer] | [modules] |
| N | [Last phase] | [Layer] | [modules] |

**Critical path:** 0 → 1 → … → N. Mark optional phases explicitly.

---

## Phase 0 — Foundation

**Goal:** Runnable repo with no business logic.

### Tasks
- [ ] Repo scaffold, .gitignore, package layout
- [ ] Pin dependencies; no secrets committed

### Exit criteria
- Fresh clone → install → imports succeed
- Secrets never in git (only `.env.example`)

---

## Phase [N] — [Name]

**Goal:** One sentence — what capability does this unlock?

**Why this phase exists:** [Optional — only fill if non-obvious sequencing]

### Tasks
- [ ] [Task]

### Deliverables

| File | Purpose |
|------|---------|
| `path/to/file` | [What it owns] |

### Exit criteria
<!-- Binary pass/fail — no subjective criteria. -->
- [Condition that proves this phase is done]
- [Edge case that must also pass]

### Manual smoke test
```bash
# Minimal command to verify the phase end-to-end
```

---

## Latency targets

| Operation | Target |
|-----------|--------|
| [e.g. Cached read] | < 50 ms |
| [e.g. LLM call] | < 10 s |

---

## Definition of done (full project)

- [ ] [User-facing capability] *(Phase N)*
