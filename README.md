# ProjectGraph OS

A reusable AI operating system for Product Management and project building.

Structured context in local markdown. Works with Claude, ChatGPT, Cursor, Antigravity, and Gemini. Zero dependencies.

---

## What it does

Gives AI tools a consistent, low-token project memory so they spend less time guessing and more time helping. Every file has a clear job. You decide what gets committed.

---

## Repo structure

```
your-project/
├── .projectgraph/
│   ├── CONTEXT.md        # What this project is — AI reads first
│   ├── STATE.md          # Where we are right now
│   ├── RESEARCH.md       # What we've learned
│   ├── CONVENTIONS.md    # Rules for AI and humans
│   ├── CAPTURE.md        # Raw inbox — normalize weekly
│   ├── AI.md             # Per-tool setup instructions
│   ├── ARCHITECTURE.md   # System layers, contracts, tech choices (optional)
│   ├── IMPLEMENTATION.md # Phase plan with exit criteria (optional)
│   ├── EVAL.md           # Success criteria, smoke tests, known limits (optional)
│   └── log/
│       └── YYYY-MM-DD-decision-title.md
├── .cursor/
│   └── rules/
│       └── projectgraph.mdc
├── .antigravity/
│   └── rules/
│       └── projectgraph.md
├── .gitignore
└── README.md
```

---

## Quick start

1. Fill the 3 REQUIRED fields in `CONTEXT.md` — takes 5 minutes
2. Copy your tool's block from `AI.md` into its native config
3. Drop raw notes into `CAPTURE.md` — normalize into the right file weekly

---

## File responsibilities

| File | When to update | Committed by default |
|---|---|---|
| CONTEXT.md | Rarely — project identity changes | Yes |
| STATE.md | Daily / each session | Solo: yes. Team: no (gitignored) |
| RESEARCH.md | Per finding | Yes |
| CONVENTIONS.md | Per new rule | Yes |
| CAPTURE.md | Continuously | No (gitignored) |
| AI.md | Per tool change | Yes |
| log/*.md | Per decision | Yes |
| ARCHITECTURE.md | When layers or contracts change | Yes |
| IMPLEMENTATION.md | When phases or exit criteria change | Yes |
| EVAL.md | When success criteria or limitations change | Yes |

---

## Optional files: when to use them

**ARCHITECTURE.md** — Add this when your project has more than one moving part (e.g. a backend + LLM + frontend). It gives AI a map of layers, data contracts, and tech choices so it stops guessing at structure. Skip it for single-file scripts or pure research projects.

**IMPLEMENTATION.md** — Add this when you are building in phases and need AI to respect sequencing. Each phase has exit criteria — AI should not suggest Phase N work while Phase N-1 is incomplete. Skip it for exploratory or one-shot builds.

**EVAL.md** — Add this whenever an LLM is involved, or when "does it work?" is non-trivial to answer. It records what good output looks like, a smoke test checklist, and known limitations AI should surface. It is the answer to "how do we know this is right?"

---

## Design principles

- **Low token usage** — structured fields, no prose padding
- **Reduced hallucination** — AI reads facts, not vibes
- **Beginner-friendly** — every file explains itself inline
- **Team-safe** — volatile files are gitignored by default
- **Tool-agnostic** — same files, per-tool config blocks in `AI.md`
