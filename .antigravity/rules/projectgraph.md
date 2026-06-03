# ProjectGraph OS — Antigravity Rules

## Files to load

**Every session:**
- `.projectgraph/CONTEXT.md`
- `.projectgraph/ACTIVE.md`

**Complex tasks:**
- latest journal handoff referenced by ACTIVE.md
- artifacts listed in that handoff
- `.projectgraph/SUMMARY.md` when it exists and is relevant

**Never load:**
- `.projectgraph/NEXT.md`
- `.projectgraph/STATE.md`
- `.projectgraph/CONVENTIONS.md`
- `.projectgraph/AI.md`
- `.projectgraph/REPO-RESCUE.md`
- `.projectgraph/RESEARCH.md`
- `.projectgraph/IMPLEMENTATION.md`
- `.projectgraph/EVAL.md`
- `.projectgraph/log/`
- `.projectgraph/CAPTURE.md`

## Behaviour rules

- Follow rules in `.projectgraph/CONTEXT.md` exactly.
- Treat anything under `CONTEXT.md` Assumptions as unvalidated.
- If a file is not in the agent startup protocol, do not load it without explicit instruction.
- When reviewing architecture or decisions, prefer the latest journal handoff and referenced artifacts.
