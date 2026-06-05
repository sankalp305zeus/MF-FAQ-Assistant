# PMOS — PM Operating System v1.1

The smallest system that repeatedly ships portfolio-worthy projects.

## What this is

PMOS gives a solo PM a reusable project structure that:
- Loads in ~150 tokens (one file: BRIEF.md)
- Works across Claude, Claude Code, Cursor, ChatGPT, Gemini, Antigravity
- Compounds learning across projects via PLAYBOOK.md and FAILURES.md
- Prevents deployment failures via a built-in launch checklist
- Prevents debugging loops via an investigation protocol

## What this is NOT

- Not a framework
- Not a multi-agent system
- Not a project management tool
- Not documentation for documentation's sake

## Structure

```
your-project/
└── .pmos/
    ├── BRIEF.md             # The one file. Project identity + state + launch status.
    ├── journal/             # Append-only. Everything that happened.
    └── artifacts/           # Everything produced. Architecture, PRDs, eval results.

~/.pmos/
├── PLAYBOOK.md              # What worked. Cross-project. Includes investigation protocol.
└── FAILURES.md              # What didn't. Auto-populated from failed journal entries.
```

## Quick start

1. Clone this repo or copy `.pmos/` into your project
2. Copy `global/PLAYBOOK.md` and `global/FAILURES.md` to `~/.pmos/`
3. Fill in BRIEF.md — just the What, Why, and Success sections (2 minutes)
4. Tell your AI: "Read .pmos/BRIEF.md before every response"
5. Start working

## How Maya works

Maya is not a separate agent. Maya is how you talk to your AI tool.

When you start a session:
```
Read .pmos/BRIEF.md. You are Maya — my PM partner.
Check ~/.pmos/PLAYBOOK.md for patterns matching this project type.
Check ~/.pmos/FAILURES.md for known pitfalls.
Then help me with: [your task]
```

Maya has four modes — not separate agents, just focus areas:

| Mode | When | What Maya does |
|---|---|---|
| **Normal** | Default | PM thinking, building, creating |
| **Launch** | Deploying | Follows launch checklist in BRIEF.md. Verifies each step. |
| **Investigate** | Something broke | Follows investigation protocol from PLAYBOOK.md. FACT/DISPROVEN/UNKNOWN. |
| **Verify** | Ready to ship | Checks Success metrics. Verifies deployment. Confirms Verified field. |

## Anti-waste rules

Before any task, Maya evaluates:

| Dimension | Score |
|---|---|
| Portfolio value | high / medium / low |
| Learning value | high / medium / low |
| User value | high / medium / low |
| Effort | hours estimate |

If a task scores LOW on all three value dimensions → challenge it.
If a task is >50% engineering and <20% portfolio value → challenge it.
Ship > optimize. Demo > perfection. Feedback > polish.

## Anti-loop rules

If 2 consecutive attempts produce the same error class:
→ STOP fixing. Switch to investigation mode.
→ Follow the investigation protocol in PLAYBOOK.md.
→ Diagnose first, then fix.

If 3 total attempts fail:
→ Escalate to human with diagnosis and options.

## Journal format

After every significant action, append to journal/:

```markdown
# [Action title]

Date: YYYY-MM-DD
Type: [decision | build | research | fix | ship | learn | investigate]

## What happened
[2-5 sentences.]

## Outcome
[Worked | Failed | Partial]

## Decisions
[If any.]

## Learning
[What to remember for future projects.]
```

Journal entries with `Outcome: Failed` automatically become FAILURES.md candidates.

## Definition of Done

A project is done when:
1. Working demo accessible via URL
2. Success metrics from BRIEF.md are measured (not assumed)
3. At least one evaluation run completed with documented results
4. BRIEF.md Verified field has evidence, not just "done"
5. BRIEF.md Launch status is "deployed-and-verified"
6. PLAYBOOK.md updated with reusable patterns
7. FAILURES.md updated with failure patterns

## IDE auto-load config

For Claude Code, Cursor, Antigravity, or any IDE:

```
Read .pmos/BRIEF.md before every response.
```

That's it. ~150 tokens of background context.

## After 3 projects

Perform a retrospective:
- Which BRIEF.md fields were actually used?
- Which journal entries provided value?
- How many PLAYBOOK entries exist?
- How many FAILURES entries exist?
- Did the investigation protocol get used?
- Did the launch checklist prevent any failures?

Update PMOS based on evidence. Not before.
