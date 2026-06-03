# Migration Report: v3.5 → v4-beta

**Date:** 2026-06-04
**Status:** Complete

---

## Completed Before This Session

These items were already done in the prior partial migration:

| Item | Action | Status |
|------|--------|--------|
| `CONTEXT.md` | Rewritten to v4 schema (Identity, Problem, Solution, Constraints, Rules, Assumptions) | Done |
| `ACTIVE.md` | Created with v4 schema | Done |
| `MODES.md` | Updated to v4 routing table | Done |
| `AI.md` | Deleted | Done |
| `CONVENTIONS.md` | Deleted — Rules folded into CONTEXT.md | Done |
| `NEXT.md` | Deleted — replaced by ACTIVE.md | Done |
| `REPO-RESCUE.md` | Deleted — repo-rescue is now a mode in MODES.md | Done |
| `ARCHITECTURE.md` → `artifacts/ARCHITECTURE.md` | Moved | Done |
| `EVAL.md` → `artifacts/EVAL.md` | Moved | Done |
| `IMPLEMENTATION.md` → `artifacts/IMPLEMENTATION.md` | Moved | Done |
| `RESEARCH.md` → `artifacts/RESEARCH.md` | Moved | Done |
| `log/` → `journal/` | Renamed | Done |

---

## Completed This Session

| Item | Action |
|------|--------|
| `agents/MAYA.md` | Replaced v3.5 version (90-line orchestrator manual) with v4 reference card (~150 tokens) |
| `agents/NOVA.md` | Created — validate phase agent |
| `agents/ATLAS.md` | Created — design phase agent |
| `agents/FORGE.md` | Created — build phase agent |
| `agents/SENTINEL.md` | Created — verify phase agent |
| `.cursor/rules/projectgraph.mdc` | Rewritten — now points at CONTEXT.md + ACTIVE.md only |
| `.antigravity/rules/projectgraph.md` | Rewritten — now points at CONTEXT.md + ACTIVE.md only |
| `journal/YYYY-MM-DD-decision-title.md` | Deleted — was an old v3.5 decision template, not a v4 handoff |
| `journal/.gitkeep` | Added — preserves empty directory in git |
| `artifacts/.gitkeep` | Added — preserves empty directory in git |

---

## Final Repository Tree

```
projectgraph-os/
├── .antigravity/
│   └── rules/
│       └── projectgraph.md          ← v4: CONTEXT + ACTIVE only
├── .cursor/
│   └── rules/
│       └── projectgraph.mdc         ← v4: CONTEXT + ACTIVE only
├── .gitignore
├── .projectgraph/
│   ├── ACTIVE.md                    ← ~100 tokens, runtime state
│   ├── CONTEXT.md                   ← ~200 tokens, project identity
│   ├── MODES.md                     ← routing table, reference only
│   ├── agents/
│   │   ├── ATLAS.md                 ← design phase, ~150 tokens
│   │   ├── FORGE.md                 ← build phase, ~150 tokens
│   │   ├── MAYA.md                  ← discover phase, ~150 tokens
│   │   ├── NOVA.md                  ← validate phase, ~150 tokens
│   │   └── SENTINEL.md              ← verify phase, ~150 tokens
│   ├── artifacts/
│   │   ├── .gitkeep
│   │   ├── ARCHITECTURE.md          ← migrated from root
│   │   ├── EVAL.md                  ← migrated from root
│   │   ├── IMPLEMENTATION.md        ← migrated from root
│   │   └── RESEARCH.md              ← migrated from root
│   └── journal/
│       └── .gitkeep                 ← ready for first handoff
├── ProjectGraph-OS-v4-beta-spec.md
└── README.md
```

---

## Diff Summary

```
13 files changed (staged), 4 files created (untracked)
363 lines removed, 66 lines added

Deleted:  AI.md, CONVENTIONS.md, NEXT.md, REPO-RESCUE.md
          log/YYYY-MM-DD-decision-title.md (old decision template)
Modified: CONTEXT.md, ACTIVE.md, MODES.md
          agents/MAYA.md (trimmed from ~90 lines to ~25 lines)
          .cursor/rules/projectgraph.mdc
          .antigravity/rules/projectgraph.md
Moved:    ARCHITECTURE.md, EVAL.md, IMPLEMENTATION.md, RESEARCH.md → artifacts/
          log/ → journal/
Created:  agents/NOVA.md, ATLAS.md, FORGE.md, SENTINEL.md
          journal/.gitkeep, artifacts/.gitkeep
```

---

## v4-beta Readiness Checklist

| Requirement | Status |
|-------------|--------|
| CONTEXT.md — v4 schema, ≤200 tokens | ✅ |
| ACTIVE.md — v4 schema, ≤120 tokens | ✅ |
| MODES.md — routing table only | ✅ |
| 5 agent files in agents/, ~150 tokens each | ✅ |
| journal/ directory with .gitkeep | ✅ |
| artifacts/ directory with .gitkeep | ✅ |
| IDE auto-load = CONTEXT + ACTIVE only | ✅ |
| Deleted: AI.md, CONVENTIONS.md, NEXT.md, REPO-RESCUE.md | ✅ |
| No templates/ directory | ✅ (never existed here) |
| PLAYBOOK.md at ~/.projectgraph/ | ⬜ Not created — per spec, human creates after 3+ real projects |

---

## Remaining Item (not a blocker)

`~/.projectgraph/PLAYBOOK.md` — the cross-project organizational memory file. Per spec (section 10), this is human-curated after real project usage and is not part of the template. Create it after running 3+ complete Discover → Verify cycles.

---

## v4-beta Declaration Criteria (spec section 19)

| Condition | Status |
|-----------|--------|
| MF chatbot project fully retrofitted to v4 structure | ⬜ Not in this repo |
| At least one complete Discover → Verify cycle run | ⬜ Pending — ACTIVE.md ready for Maya activation |
| 60-second recovery rule tested after 48-hour gap | ⬜ Pending |
| At least 3 PLAYBOOK.md entries from real project work | ⬜ Pending |

The OS structure migration is complete. v4-beta is declared when the four runtime conditions above are satisfied.
