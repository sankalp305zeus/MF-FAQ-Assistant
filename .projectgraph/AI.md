# AI Tool Integration

<!-- Copy the block for your tool into its native config. -->
<!-- CONVENTIONS.md is the rule source of truth — do not duplicate rules here. -->

## Reading order

| When | Files to load |
|---|---|
| Every session | `CONTEXT.md` + `CONVENTIONS.md` |
| Complex tasks | + `STATE.md` + `RESEARCH.md` (Active section only) |
| Arch / tech decisions | + last 3–5 files in `log/` |
| Never auto-load | `CAPTURE.md` — unprocessed inbox |

---

## Claude — claude.ai Projects

Paste into **Project Instructions**:

```
Before every response, read .projectgraph/CONTEXT.md and .projectgraph/CONVENTIONS.md.
For architecture or tech decisions, also read the 3 most recent files in .projectgraph/log/.
Treat anything under CONTEXT.md "Assumptions" as unvalidated — say so when relevant.
If STATE.md shows any file unreviewed >30 days, flag it.
Never use .projectgraph/CAPTURE.md as context.
```

---

## Claude Code

Add to `CLAUDE.md` at the project root:

```
@file .projectgraph/CONTEXT.md
@file .projectgraph/CONVENTIONS.md

Follow all conventions in CONVENTIONS.md exactly.
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

**Option A — Custom Instructions (persistent across sessions):**
```
I maintain a .projectgraph/ folder for my projects.
When I share CONTEXT.md, treat it as authoritative project context.
Treat any "Assumptions" section as unvalidated beliefs, not confirmed facts.
```

**Option B — Per session:** Upload `CONTEXT.md` and `CONVENTIONS.md` at session start.

---

## Gemini

Load the 5 core files at session start, then open with:
```
I've attached my project context files. Read them before responding.
Treat "Assumptions" sections as unvalidated.
```

---

## Global defaults (optional)

Create `~/.projectgraph/GLOBAL.md` for personal conventions that apply across all your projects:

```markdown
# Global Conventions

## Personal tech stack defaults
-

## Decisions already made across projects
-

## Research that applies across projects
-
```

Then add this to any AI tool config:
```
Also read ~/.projectgraph/GLOBAL.md for personal defaults before making recommendations.
```
