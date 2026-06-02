# ProjectGraph OS

Structured project context + Maya-led AI orchestration. Local markdown. Zero dependencies.

Works with Claude, ChatGPT, Cursor, Antigravity, and Gemini.

---

## What it does

Gives AI tools a consistent, low-token project memory. Maya — the product lead agent — reads your problem statement, infers context, selects a mode, and activates specialist agents only when needed.

---

## Quick start

1. Fill **Problem** and **Solution** in `CONTEXT.md` — takes 5 minutes
2. Copy your tool's block from `AI.md` into its native config
3. Activate Maya: `"Act as Maya. Read .projectgraph/agents/MAYA.md, CONTEXT.md, and NEXT.md."`
4. Maya infers the rest, asks at most 3 questions, and sets up your project

---

## Repo structure

```
.projectgraph/
├── CONTEXT.md          # Project identity + mode — AI reads first
├── NEXT.md             # Current goal + next action — read on every resume
├── STATE.md            # Current status
├── CONVENTIONS.md      # Rules for AI and humans
├── MODES.md            # Mode routing table — Maya uses this to select mode
├── RESEARCH.md         # Findings with confidence + staleness
├── CAPTURE.md          # Raw inbox — normalize weekly
├── REPO-RESCUE.md      # Workflow for existing/abandoned repos
├── AI.md               # Tool setup: Claude / Cursor / ChatGPT / Gemini / Antigravity
├── agents/
│   └── MAYA.md         # Product Lead & Orchestrator
└── log/
    └── YYYY-MM-DD-decision-title.md

.cursor/rules/projectgraph.mdc    # Cursor auto-load
.antigravity/rules/projectgraph.md
```

---

## Maya — the orchestrator

Maya is the entry point for every project. She:

- Reads your Problem + Solution and infers Name, Type, Stage, Users, Constraints
- Asks at most 3 high-value questions — only what she cannot infer
- Selects the right mode from `MODES.md`
- Presents a filled `CONTEXT.md` and `NEXT.md` for your approval
- Activates specialist agents (Nova, Atlas, Forge, Sentinel) on demand as work progresses

Human is always the final approver at each gate.

---

## Modes

| Mode | When | Required files |
|---|---|---|
| **mvp** | Shipping fast, solo or small team | CONTEXT, NEXT, STATE, CONVENTIONS |
| **research** | Market/user/tech validation, no code | CONTEXT, NEXT, STATE, RESEARCH |
| **ai-rag** | AI product with retrieval or eval | CONTEXT, NEXT, STATE, CONVENTIONS, RESEARCH |
| **saas** | Production SaaS — auth, billing, multi-tenancy | CONTEXT, NEXT, STATE, CONVENTIONS, RESEARCH |
| **repo-rescue** | Existing or abandoned codebase | CONTEXT, NEXT, STATE, REPO-RESCUE |

Maya selects the mode. You confirm or override.

---

## Token tiers

| Tier | Files | When |
|---|---|---|
| 1 — always | CONTEXT, NEXT, STATE | Every session start |
| 2 — relevant | CONVENTIONS, RESEARCH, MODES | Based on task |
| 3 — on demand | log/, CAPTURE | Investigating history |

---

## File responsibilities

| File | When to update | Committed |
|---|---|---|
| CONTEXT.md | Rarely — identity changes | Yes |
| NEXT.md | Every session | Solo: optional. Team: gitignored |
| STATE.md | Per status change | Solo: optional. Team: gitignored |
| CONVENTIONS.md | Per new rule | Yes |
| MODES.md | When mode structure changes | Yes |
| RESEARCH.md | Per finding | Yes |
| CAPTURE.md | Continuously | No (gitignored) |
| AI.md | Per tool change | Yes |
| agents/*.md | Per agent change | Yes |
| log/*.md | Per decision | Yes |

---

## Design principles

- **Maya-led** — one entry point, consistent orchestration
- **Infer first, ask second** — Maya fills gaps before prompting the human
- **Low token usage** — structured fields, no prose padding
- **Max 5 required files per mode** — enforced in MODES.md
- **Agents on demand** — no agent is pre-loaded; Maya activates them when needed
- **Tool-agnostic** — same files, per-tool config blocks in `AI.md`
