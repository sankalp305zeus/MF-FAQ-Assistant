# AI Tool Integration

<!-- CONVENTIONS.md is the rule source of truth — do not duplicate rules here. -->

## Token loading tiers

| Tier | Files | When |
|---|---|---|
| Tier 1 (always) | `CONTEXT.md`, `NEXT.md`, `STATE.md` | Every session start |
| Tier 2 (relevant) | `CONVENTIONS.md`, `RESEARCH.md`, `MODES.md` | Based on task |
| Tier 3 (on demand) | `log/`, `CAPTURE.md` | Investigating history only |

## Maya — entry point

Maya is the orchestrator. Activate her at the start of every project session.

```
Act as Maya for this project.
Read .projectgraph/agents/MAYA.md for your role definition.
Read .projectgraph/CONTEXT.md and .projectgraph/NEXT.md.
```

Maya infers context, selects the mode, and activates downstream agents on demand.
See `.projectgraph/agents/MAYA.md` for her full protocol.

---

## Claude — claude.ai Projects

Paste into **Project Instructions**:

```
Before every response, read .projectgraph/CONTEXT.md and .projectgraph/NEXT.md.
For conventions, also read .projectgraph/CONVENTIONS.md.
For architecture or tech decisions, read the 3 most recent files in .projectgraph/log/.
Treat anything under CONTEXT.md "Assumptions" as unvalidated — say so when relevant.
If STATE.md Health check shows any file unreviewed >30 days, flag it.
Check CONTEXT.md Mode field → see MODES.md for which agents and files are active.
Never use .projectgraph/CAPTURE.md as context.
```

---

## Claude Code

Add to `CLAUDE.md` at the project root:

```
@file .projectgraph/CONTEXT.md
@file .projectgraph/NEXT.md
@file .projectgraph/CONVENTIONS.md

Follow all conventions in CONVENTIONS.md exactly.
Check MODES.md for the active mode and which agents apply.
For architecture decisions, check .projectgraph/log/ before proposing changes.
Treat CONTEXT.md "Assumptions" as unvalidated.
```

---

## Cursor

`.cursor/rules/projectgraph.mdc` is already configured in this repo. No action needed.

---

## Antigravity

`.antigravity/rules/projectgraph.md` is already configured in this repo. No action needed.

---

## ChatGPT

Upload `CONTEXT.md` + `NEXT.md` + `CONVENTIONS.md` at session start. Then activate Maya.

---

## Gemini

Load Tier 1 + Tier 2 files at session start (context window is generous). Then activate Maya.

---

## Cross-project (optional)

Create `~/.projectgraph/GLOBAL.md` for personal defaults that apply across all your projects:

```markdown
# Global Conventions

## Personal tech stack defaults
-

## Decisions already made across projects
-

## Research that applies across projects
-
```

Then add to any AI tool config:
```
Also read ~/.projectgraph/GLOBAL.md for personal defaults before making recommendations.
```
