# ProjectGraph OS — Antigravity Rules

<!-- Antigravity reads this file automatically from .antigravity/rules/ -->

## Files to load

**Every session:**
- `.projectgraph/CONTEXT.md`
- `.projectgraph/CONVENTIONS.md`

**Complex tasks:**
- `.projectgraph/STATE.md`
- `.projectgraph/RESEARCH.md` (Active section only)

**Architecture or tech decisions:**
- `.projectgraph/log/` — 3 most recent files

**Never load:**
- `.projectgraph/CAPTURE.md` — unprocessed inbox, not reliable context

## Behaviour rules

- Follow all conventions in `CONVENTIONS.md` exactly.
- Treat anything under `CONTEXT.md` "Assumptions" as unvalidated — say so when relevant.
- Before proposing an architecture or technology change, check `log/` for prior decisions on that topic.
- If `STATE.md` shows any file unreviewed >30 days, flag it.
- When `RESEARCH.md` entries have `Status: stale`, treat them with skepticism and say so.
