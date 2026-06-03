# ProjectGraph OS v4-beta

## The Primitive

```
Handoff → Agent → Handoff
```

Files are storage. Handoffs are communication.
Agents consume handoffs, not project history.

---

# 1. Handoff Schema

Every agent ends its phase by appending a handoff to `journal/`.
Mandatory. No free-form. No exceptions.

```markdown
# Handoff

Phase: [discover | validate | design | build | verify]
Agent: [Maya | Nova | Atlas | Forge | Sentinel]
Date: YYYY-MM-DD
Confidence: [high | medium | low]

## Objective
[What this agent was asked to do. One sentence.]

## Completed
- [Specific deliverable, not activity]

## Decisions
- [Choice + why, one line]

## Risks
- [Specific failure mode, not vague worry]

## Artifacts updated
- [Exact filepath of artifact created or modified]

## Next
Agent: [who runs next]
Action: [specific instruction — executable, not advisory]
Gate: [none | human-approval-required]
Escalate to: [none | human | Maya | Nova | Atlas | Forge | Sentinel]
Status: [ready | blocked: reason]
```

### Schema rules

1. Every field mandatory. Nothing applies → write "None."
2. Decisions are inline. No separate decision file.
3. Risks must be specific. "Something might break" fails review.
   "Only 1 of 4 PDFs extracted — retrieval coverage incomplete" passes.
4. Artifacts updated = exact filepaths. Next agent loads these, nothing else.
5. Next → Action is an instruction, not a suggestion.
   "Build ingestion pipeline starting with HTML extraction" — not
   "Forge should probably look at building."
6. Confidence reflects certainty of output. Low confidence triggers
   careful review by the next agent.
7. Escalate to must be populated whenever Status is `blocked`.
   It names who can unblock: human, or a specific agent.
8. Gate controls human intervention. `human-approval-required` = next agent
   does NOT start until human confirms.

---

# 2. Agent Protocols

## Startup protocol (mandatory, every agent)

```
1. Read CONTEXT.md
2. Read ACTIVE.md
3. Read SUMMARY.md (if it exists — skip for handoffs 1-2)
4. Read latest handoff from journal/
5. Read artifacts listed in handoff's "Artifacts updated"
6. Summarize project state in ≤3 sentences (internal, not output)
7. Confirm: "I own the [phase] phase. My action: [from handoff]."
8. Execute assigned action only. Nothing outside scope.
```

An agent that skips any step is non-compliant. An agent that loads files
not listed in steps 1-5 is non-compliant.

## Shutdown protocol (mandatory, every agent)

```
1. Update or create artifacts in artifacts/
2. Self-check: verify output against the input artifact
   - Forge: does code match ARCHITECTURE.md?
   - Atlas: does design satisfy PRD.md requirements?
   - Nova: are all findings sourced?
   - Sentinel: are all review dimensions covered?
   - Maya: is scope within stated constraints?
   If deviation found → log it in handoff Decisions field.
   If deviation is critical → set Confidence: low and Escalate.
3. Write handoff to journal/YYYY-MM-DD-[phase]-[agent].md
4. If this is the 3rd, 6th, 9th... handoff → regenerate SUMMARY.md
5. Rewrite ACTIVE.md with new phase state
6. Suggest playbook candidate (if a reusable pattern emerged)
   → append to ~/.projectgraph/PLAYBOOK-CANDIDATES.md
7. Set Confidence in handoff (high | medium | low)
8. Set Escalate to in handoff (if blocked)
9. Stop. Turn is over.
```

An agent that produces output without completing shutdown is non-compliant.
The handoff IS the deliverable. Code and artifacts are secondary to the
handoff existing.

### Self-check rules

The self-check (step 2) is NOT a full review — that's Sentinel's job.
It catches obvious deviations before they propagate. Think of it as a
developer reviewing their own PR before requesting review.

What self-check catches:
- Forge used a library not in CONTEXT.md Rules
- Atlas designed for scale the PRD doesn't require
- Nova cited a source that doesn't exist
- Forge's implementation skipped an architecture component

What self-check does NOT catch (Sentinel's job):
- Security vulnerabilities
- Performance bottlenecks
- Cross-component integration issues
- AI quality evaluation

## What agents must NOT do

- Load files not listed in startup steps 1-4
- Edit previous journal entries
- Skip or partially fill the handoff schema
- Produce free-form prose instead of the schema
- Change artifacts owned by another agent without logging a Decision
- Continue past a human-approval gate
- Make architectural decisions during build phase (escalate to Atlas)
- Make scope decisions during any phase except discover (escalate to Maya)

---

# 3. Phase Lifecycle

```
DISCOVER (Maya)
    │
    ▼  handoff
VALIDATE (Nova)              ← skip in mvp mode
    │
    ▼  handoff
DESIGN (Atlas)               ← skip in mvp mode
    │
    ▼  handoff + gate (ai-rag, saas)
BUILD (Forge)
    │
    ▼  handoff
VERIFY (Sentinel)
    │
    ▼  handoff + gate (all modes)
DONE  or  ITERATE (loop back to any phase via handoff)
```

### Phase → Agent → Token budget

| Phase    | Agent    | Reads (4 items max)                | Produces            | Tokens |
|----------|----------|------------------------------------|---------------------|--------|
| Discover | Maya     | CONTEXT + ACTIVE                   | artifacts/PRD.md    | ~300   |
| Validate | Nova     | + Maya handoff + PRD               | artifacts/RESEARCH.md | ~500 |
| Design   | Atlas    | + Nova handoff + RESEARCH          | artifacts/ARCHITECTURE.md | ~500 |
| Build    | Forge    | + Atlas handoff + ARCHITECTURE     | artifacts/IMPLEMENTATION.md + code | ~500 |
| Verify   | Sentinel | + Forge handoff + IMPLEMENTATION   | artifacts/REVIEW.md | ~500 |

Every agent: CONTEXT (~200 tokens) + ACTIVE (~100 tokens) + SUMMARY (~200 tokens, if exists) + handoff (~150 tokens) + artifact (varies).
Typical activation (early): 500-800 tokens. Typical activation (handoff 3+): 700-1,000 tokens.
Compare: v3 loaded 1,500-2,000+ tokens per agent.

### Gates

| Gate | After | Required in | Blocks |
|------|-------|-------------|--------|
| Design approval | Atlas | ai-rag, saas | Forge and downstream |
| Release approval | Sentinel | All modes | Release |

MVP mode: release gate only.

### Iteration

When Sentinel's review verdict is `FIX REQUIRED`, the handoff routes back
to the responsible agent:

- Architecture issue → Atlas
- Implementation issue → Forge
- Scope issue → Maya

The loop uses the same handoff protocol. No special mechanism.

---

# 4. ACTIVE.md

Single source of truth for "where is the project right now."
Rewritten after every handoff. Never appended.

```markdown
# Active

Phase: [discover | validate | design | build | verify | done]
Agent: [who owns the current phase]
Mode: [mvp | research | ai-rag | saas | repo-rescue]

## Objective
[What's happening right now. One sentence.]

## Last handoff
File: journal/YYYY-MM-DD-phase-agent.md
Summary: [One sentence — what was completed and decided]

## Last decision
[Most recent impactful decision affecting execution. One line.]

## Blocker
[What's preventing progress. "None" if clear.]

## Next
[Exact next action. Executable by the named agent without questions.]
```

Target: ~100-120 tokens. Anything longer means the file has drifted
from its purpose.

---

# 5. SUMMARY.md — Memory Persistence

Long-running projects accumulate handoffs. After 5+ phases, the early
decisions (why Groq, why 220-token chunks, why this AMC) are buried
in old journal entries that no agent loads.

SUMMARY.md is a rolling compression of accumulated project knowledge.
It replaces reading the full journal.

```markdown
# Summary

Last generated: YYYY-MM-DD (after handoff #N)

## Key decisions
- [Decision + why — one line each, max 8]

## Architecture state
[What the system looks like right now. 3-5 sentences.]

## Known risks
- [Active risk, not resolved]

## What didn't work
- [Failed approach — prevents repeating mistakes]
```

### Rules

1. Regenerated every 3 handoffs. Not after every one (too noisy),
   not every 5 (too stale). Three handoffs is one Discover→Design
   cycle — the point where accumulated decisions start mattering.
2. Generated by the agent completing the 3rd handoff. Added as step
   between Execute and Handoff in the shutdown protocol.
3. Replaces the previous SUMMARY.md (rewrite, not append).
4. Target: ~200 tokens. This is a compression, not a transcript.
5. If SUMMARY.md exists, agents load it at startup between ACTIVE.md
   and the latest handoff. This is the only change to the startup protocol.

### When SUMMARY.md kicks in

```
Handoff 1 (Maya):    startup reads CONTEXT + ACTIVE
Handoff 2 (Nova):    startup reads CONTEXT + ACTIVE + Maya handoff
Handoff 3 (Atlas):   startup reads CONTEXT + ACTIVE + Nova handoff
                     → Atlas generates SUMMARY.md during shutdown
Handoff 4 (Forge):   startup reads CONTEXT + ACTIVE + SUMMARY + Atlas handoff
Handoff 5 (Sentinel): startup reads CONTEXT + ACTIVE + SUMMARY + Forge handoff
                     ...
Handoff 6 (iterate): → regenerate SUMMARY.md (every 3rd handoff)
```

Before SUMMARY.md exists (handoffs 1-2): no extra file loaded.
After SUMMARY.md exists: adds ~200 tokens to startup. Still under 1,000 total.

### What SUMMARY.md is NOT

- Not a changelog (that's the journal)
- Not a status file (that's ACTIVE.md)
- Not a decisions log (decisions live in handoffs)
- Not manually maintained (auto-generated by agents)

---

# 6. CONTEXT.md

Project identity. Rarely updated. Always loaded.

```markdown
# Context

## Identity
- Name: [Project name]
- Slug: [short-id]
- One-liner: [max 15 words]
- Type: [product | research | experiment | internal-tool]
- Stage: [idea | prototype | mvp | growth | mature]
- Mode: [mvp | research | ai-rag | saas | repo-rescue]

## Problem [max 40 words]
[Who has what pain? Why now?]

## Solution [max 40 words]
[What does this do? What does it NOT do?]

## Constraints [max 4 bullets]
- [Hard constraint]

## Rules [max 4 bullets]
- [Convention that any agent must follow on this project]

## Assumptions (unvalidated)
- [Belief not yet confirmed. Agents treat as uncertain.]
```

Target: ~200 tokens. Rules section replaces the standalone CONVENTIONS.md
for most projects. If a project has >4 rules, create CONVENTIONS.md as
an artifact — not a core OS file.

---

# 7. MODES.md

Routing table. Reference only — not loaded during execution.

```markdown
# Modes

| Mode        | Phases                                 | Gates            | Agents active            |
|-------------|----------------------------------------|------------------|--------------------------|
| mvp         | Discover → Build → Verify              | Release          | Maya, Forge, Sentinel    |
| research    | Discover → Validate                    | None             | Maya, Nova               |
| ai-rag      | Discover → Validate → Design → Build → Verify | Design + Release | All 5             |
| saas        | All 5 phases                           | Design + Release | All 5                    |
| repo-rescue | Design → Build → Verify                | Recovery plan    | Atlas, Forge, Sentinel   |
```

An agent checks MODES.md only to confirm whether its phase is active
in the current mode. Not loaded during normal execution.

---

# 8. Journal

```
journal/
├── 2026-06-01-discover-maya.md
├── 2026-06-02-validate-nova.md
├── 2026-06-02-design-atlas.md
├── 2026-06-03-build-forge.md
├── 2026-06-04-verify-sentinel.md
└── ...
```

Rules:
1. One file per handoff. Named: `YYYY-MM-DD-[phase]-[agent].md`
2. Append-only. Never edit past entries.
3. Only the latest entry is loaded by default (startup protocol step 3).
4. Older entries are on-demand only (debugging, auditing, handoff disputes).
5. File sort by name = chronological order.

---

# 9. Artifacts

```
artifacts/
├── PRD.md              ← Maya
├── RESEARCH.md         ← Nova
├── ARCHITECTURE.md     ← Atlas
├── IMPLEMENTATION.md   ← Forge
├── REVIEW.md           ← Sentinel
└── [whatever the project needs]
```

Rules:
1. No pre-created templates. Agents write directly.
2. Each artifact has one owner (the agent that created it).
3. Reading another agent's artifact: allowed.
4. Editing another agent's artifact: requires a Decision in the handoff.
5. Artifact output format is defined in the agent's .md file (section: Output format).
6. Not every project has every artifact. MVP may produce only PRD.md + code.

---

# 10. Agents

Five agents. Five phases. No changes to names or count.

```
agents/
├── MAYA.md        # Discover — problem framing, PRD, scope, metrics
├── NOVA.md        # Validate — research, competitor analysis, eval
├── ATLAS.md       # Design   — architecture, data model, API contracts
├── FORGE.md       # Build    — implementation, code, tests
└── SENTINEL.md    # Verify   — QA, security, review, release verdict
```

Agent definitions are reference files loaded only when a human or
orchestrator activates the agent for the first time in a project.
After that, the handoff chain carries all necessary instructions.

Each agent file contains:
- Mission (one sentence)
- Phase it owns
- Startup reads (which 4 items)
- Output format (what its artifact looks like)
- Decision rules (when to decide vs. escalate)
- Escalation rules (when to stop and route)

Agent files do NOT contain: templates, examples, lengthy process descriptions.
They are reference cards, not manuals. Target: ~150 tokens each.

---

# 11. PLAYBOOK.md — Organizational Memory

Lives at `~/.projectgraph/PLAYBOOK.md`. Cross-project. Not inside any
single project's .projectgraph/.

```markdown
# Playbook

## [Pattern name]
Agent: [Maya | Nova | Atlas | Forge | Sentinel]
Phase: [discover | validate | design | build | verify]
Context: [When to use this — project type, situation]
Prompt: [Exact prompt or approach]
Outcome: [What happened — worked | failed | partial]
Reuse: [yes | no | conditional: when]
Project: [slug]
Date: YYYY-MM-DD

---
```

Rules:
1. Append-only. Newest at top.
2. Failed patterns are recorded. `Outcome: Failed` + `Reuse: no`.
3. Agents reference PLAYBOOK.md at phase start only if a matching
   pattern exists for the current mode + phase.
4. PLAYBOOK.md is Tier 5 loading — not part of the standard startup protocol.
   Only loaded when an agent explicitly checks for prior art.
5. Human curates. Agents suggest entries; human approves.

### Candidate pipeline

Agents suggest playbook entries during shutdown (protocol step 6).
Candidates go to a separate file. Human reviews and promotes.

```
~/.projectgraph/
├── PLAYBOOK.md                 # Approved entries. Agents may read.
└── PLAYBOOK-CANDIDATES.md      # Agent suggestions. Human reviews.
```

**PLAYBOOK-CANDIDATES.md** uses the same schema as PLAYBOOK.md.
Each entry is prefixed with `Status: candidate`.

Human workflow:
1. After a project milestone, review PLAYBOOK-CANDIDATES.md
2. Approve → move entry to PLAYBOOK.md, remove `Status:` line
3. Reject → delete entry from CANDIDATES
4. Edit → revise wording then promote

Agents NEVER read PLAYBOOK-CANDIDATES.md. Only PLAYBOOK.md.
This prevents unvalidated patterns from influencing execution.

---

# 12. Token Loading Tiers

| Tier | What | When | Tokens |
|------|------|------|--------|
| 1 | CONTEXT.md + ACTIVE.md | Every startup | ~300 |
| 1b | SUMMARY.md (if exists) | Every startup after handoff 3 | ~200 |
| 2 | Latest handoff + referenced artifact | Every startup | ~200-500 |
| 3 | Agent definition (own file only) | First activation | ~150 |
| 4 | Older journal entries | Debugging / disputes | Varies |
| 5 | PLAYBOOK.md (matching entries) | Phase start, optional | Varies |

Typical agent activation (handoffs 1-2): Tier 1 + 2 = **500-800 tokens**.
Typical agent activation (handoff 3+): Tier 1 + 1b + 2 = **700-1,000 tokens**.
Still under half of v3's 1,500-2,000 tokens.

### IDE-specific optimization

Claude Code, Cursor, Codex, Antigravity, and similar tools have limited
context budgets for background files. The OS is designed for this:

**CLAUDE.md / .cursor/rules / .antigravity/rules:**
```
Read .projectgraph/CONTEXT.md and .projectgraph/ACTIVE.md before every response.
If ACTIVE.md references a journal file, read that file.
If ACTIVE.md references artifacts, read only those.
Do not load the full journal/ or artifacts/ directory.
Follow Rules in CONTEXT.md for all project conventions.
```

This loads ~300 tokens of persistent context. Handoff + artifact are
loaded per-task, not as background. Total background cost: ~300 tokens.
Compare: v3.5 loaded CONTEXT + NEXT + STATE + CONVENTIONS as background = ~800+ tokens.

**Key principle for IDEs:** CONTEXT.md + ACTIVE.md are the ONLY files
in auto-load rules. Everything else is pulled on demand by the agent
protocol or by the human pointing the IDE at a specific file.

---

# 13. Repository Bootstrap

ProjectGraph OS is a reusable template. Every new project starts the same way.

### New project

```bash
# 1. Create repo
mkdir my-project && cd my-project && git init

# 2. Clone the OS skeleton
cp -r ~/projectgraph-os-template/.projectgraph .
# Or: git clone --depth 1 <template-repo> .projectgraph-tmp && mv .projectgraph-tmp/.projectgraph . && rm -rf .projectgraph-tmp

# 3. Fill CONTEXT.md (3 required fields: Identity, Problem, Solution)

# 4. Set Mode in CONTEXT.md (default: mvp)

# 5. Write initial ACTIVE.md:
#    Phase: discover | Agent: Maya | Next: [your problem statement]

# 6. Activate Maya — the handoff chain begins
```

### Existing repo (repo-rescue mode)

```bash
# 1. Add .projectgraph/ to existing repo
cp -r ~/projectgraph-os-template/.projectgraph .

# 2. Set Mode: repo-rescue in CONTEXT.md

# 3. Fill CONTEXT.md from what you can infer (README, package.json, etc.)

# 4. Write ACTIVE.md:
#    Phase: design | Agent: Atlas | Next: Reverse-engineer this repository

# 5. Activate Atlas — starts with assessment, not with a PRD
```

### Template repo structure (what you clone)

```
projectgraph-os-template/
└── .projectgraph/
    ├── CONTEXT.md          # Blank template with field labels
    ├── ACTIVE.md           # Blank template with field labels
    ├── MODES.md            # Populated routing table
    ├── agents/
    │   ├── MAYA.md
    │   ├── NOVA.md
    │   ├── ATLAS.md
    │   ├── FORGE.md
    │   └── SENTINEL.md
    ├── journal/            # Empty directory
    └── artifacts/          # Empty directory
```

8 files + 2 empty directories. That is the entire OS.

---

# 14. Mode Routing

| Mode | Phases | Gates | Agents | First agent |
|------|--------|-------|--------|-------------|
| mvp | Discover → Build → Verify | Release | Maya, Forge, Sentinel | Maya |
| research | Discover → Validate | None | Maya, Nova | Maya |
| ai-rag | All 5 | Design + Release | All 5 | Maya |
| saas | All 5 | Design + Release | All 5 | Maya |
| repo-rescue | Design → Build → Verify | Recovery plan | Atlas, Forge, Sentinel | Atlas |

---

# 15. Failure Modes and Recovery

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Agent produces free-form output without handoff | ACTIVE.md not updated after agent runs | Human forces shutdown protocol. Re-run agent. |
| Agent loads wrong files | Handoff references artifacts the agent shouldn't read | Sentinel flags in verify phase. Escalate to human. |
| Handoff chain breaks (session dies mid-agent) | ACTIVE.md shows stale date | Human reads ACTIVE.md, identifies last valid handoff, re-activates current agent |
| Agent disagrees with previous decision | Decision conflict in handoff | Escalate to decision owner or human. New handoff supersedes. |
| Artifact drift (code diverges from ARCHITECTURE) | Sentinel verify phase catches mismatch | FIX REQUIRED verdict routes to Forge or Atlas |
| Blocked status with no escalation target | Handoff has Status: blocked but Escalate to: none | Non-compliant handoff. Human intervenes. Schema violation. |
| Human never approves a gate | ACTIVE.md shows gate-pending indefinitely | Human reviews and either approves, rejects (routes back), or abandons |
| CONTEXT.md grows beyond ~200 tokens | Checked during verify phase | Sentinel flags. Human trims or extracts to artifact. |
| ACTIVE.md has stale Last handoff reference | Journal file doesn't match | Re-sync ACTIVE.md from latest journal entry |
| SUMMARY.md loses critical decision during compression | Agent downstream makes conflicting choice | Sentinel verify catches mismatch. Regenerate SUMMARY.md from journal entries. |
| Self-check passes but Sentinel finds critical issue | Self-check only catches mechanical errors | Expected. Self-check reduces Sentinel's workload, doesn't replace it. |

### The 60-second recovery rule

Any agent — human or AI — should be able to resume a project in under
60 seconds by reading ACTIVE.md + latest handoff. If it takes longer,
ACTIVE.md is stale or the handoff is incomplete. Both are protocol violations.

---

# 16. Migration from v3.5 → v4

| v3.5 file | v4 action |
|-----------|-----------|
| CONTEXT.md | Keep. Add `## Rules` section (absorbs CONVENTIONS.md). Remove fields over 200 tokens. |
| ACTIVE.md (was NEXT.md) | Rewrite to v4 schema. Add `Last decision` field. |
| STATE.md | Delete. Merged into ACTIVE.md. |
| NEXT.md | Delete. Replaced by ACTIVE.md. |
| CONVENTIONS.md | Delete. Rules folded into CONTEXT.md `## Rules`. If >4 rules, create as artifact. |
| CAPTURE.md | Delete. Not used in MF project. Raw notes go in journal/ or nowhere. |
| RESEARCH.md | Move to `artifacts/RESEARCH.md`. |
| MODES.md | Keep. Simplify to routing table only. |
| REPO-RESCUE.md | Delete as standalone file. Repo-rescue is a mode in MODES.md, not a workflow doc. Atlas's agent file covers the procedure. |
| AI.md | Delete. IDE config is 2 lines pointing at CONTEXT + ACTIVE. |
| agents/ (7 files → 5 files) | Already done in v3.5. Keep Maya, Nova, Atlas, Forge, Sentinel. Trim to ~150 tokens each. |
| templates/ (12 files) | Delete all. Agents produce artifacts directly. Output format lives in agent definition. |
| log/ | Rename to `journal/`. Convert existing entries to handoff schema. |
| .cursor/rules/projectgraph.mdc | Rewrite: point at CONTEXT + ACTIVE only. |
| .antigravity/rules.md | Rewrite: point at CONTEXT + ACTIVE only. |
| AGENT_WORKFLOW.md | Delete. The workflow IS the handoff chain. MODES.md covers routing. |

### Net file change: v3.5 had ~32 files → v4 has 8 files + 2 directories

---

# 17. Complete v4 Structure

```
.projectgraph/
├── CONTEXT.md             # ~200 tokens. Identity + rules. Always loaded.
├── ACTIVE.md              # ~100 tokens. Runtime state. Always loaded.
├── SUMMARY.md             # ~200 tokens. Rolling compressed memory. Auto-generated every 3 handoffs.
├── MODES.md               # Reference only. Not loaded during execution.
├── agents/
│   ├── MAYA.md            # ~150 tokens. Discover phase.
│   ├── NOVA.md            # ~150 tokens. Validate phase.
│   ├── ATLAS.md           # ~150 tokens. Design phase.
│   ├── FORGE.md           # ~150 tokens. Build phase.
│   └── SENTINEL.md        # ~150 tokens. Verify phase.
├── journal/               # Append-only. One handoff per file.
│   └── YYYY-MM-DD-phase-agent.md
└── artifacts/             # Agent outputs. Project-specific.
    └── [created during execution]

~/.projectgraph/
├── PLAYBOOK.md            # Approved cross-project memory.
└── PLAYBOOK-CANDIDATES.md # Agent suggestions. Human reviews.
```

IDE auto-load config (all tools):
```
.projectgraph/CONTEXT.md
.projectgraph/ACTIVE.md
```

That's it. ~150 tokens of persistent background context for any IDE.
SUMMARY.md is loaded per-task when the agent protocol runs, not as background.

---

# 18. Critique — What's Still Weak

| Weakness | Severity | Why it persists | Mitigation |
|----------|----------|-----------------|------------|
| No enforcement mechanism | Medium | Agents are prompts, not software. Nothing stops an AI from ignoring the protocol. | Self-check in shutdown catches obvious violations. Sentinel catches the rest. |
| Single-session agents only | Medium | Each agent runs in one session. Multi-session phases (long builds) break the handoff chain. | Forge can write intermediate handoffs (`build-forge-part1`, `build-forge-part2`). Schema supports it. |
| PLAYBOOK.md curation is manual | Low | Human must review candidates and promote. | Candidate pipeline reduces friction. Still requires human judgment — intentional. |
| No versioning within artifacts | Low | If Forge rewrites IMPLEMENTATION.md, old version is gone. | Git tracks this. The OS doesn't duplicate version control. |
| Handoff quality depends on the AI | High | A lazy handoff is schema-compliant but useless. | Self-check catches format violations. Confidence: low triggers review. Sentinel flags low-quality handoffs. |
| No support for parallel agents | Low | The pipeline is sequential. | Acceptable for solo builder. Parallel work is a v5 concern. |
| SUMMARY.md generation quality | Medium | Auto-generated compression may lose important nuance. | 200 token limit forces selectivity. Regenerated every 3 handoffs so it stays fresh. Human can manually regenerate if drift detected. |
| Self-check is same-agent reviewing own work | Low | Agent may not catch its own blind spots. | This is expected. Self-check catches mechanical errors (wrong library, missed component). Sentinel catches systemic issues. Two layers, not one. |

---

# 19. Unresolved Assumptions and Risks

| # | Assumption | Risk if wrong |
|---|-----------|---------------|
| 1 | AI agents will follow the startup/shutdown protocol when instructed | If they don't, handoffs are incomplete and the chain breaks. Mitigation: Sentinel checks. |
| 2 | 200 tokens is enough for CONTEXT.md on complex projects | Large SaaS projects may need more. Mitigation: overflow goes to artifacts, not CONTEXT. |
| 3 | The 60-second recovery rule is achievable | Untested on projects with 20+ journal entries. Mitigation: ACTIVE.md should always be current — journal length doesn't matter if ACTIVE.md is maintained. |
| 4 | PLAYBOOK.md will be maintained across projects | If human stops curating, organizational memory degrades. No automated fix. |
| 5 | The handoff schema is complete | Missing fields will only surface through real project usage. Mitigation: schema is extensible — add fields per-project if needed, propose to core only after 3+ projects validate the need. |
| 6 | Solo builder doesn't need parallel agents | If a project requires simultaneous research and design, the sequential model blocks. Mitigation: human can manually trigger two agents and merge handoffs. |
| 7 | Conventions folded into CONTEXT.md Rules will be sufficient | Projects with >10 conventions will overflow. Mitigation: CONVENTIONS.md becomes an artifact when needed, not a core file. |

---

# 20. Declaring v4-alpha

v4-alpha is ready when:

1. The MF chatbot project has been fully retrofitted to v4 structure
2. At least one complete Discover → Verify cycle has been run using handoff protocol
3. The 60-second recovery rule has been tested after a 48-hour gap
4. At least 3 PLAYBOOK.md entries exist from real project work
5. SUMMARY.md has been auto-generated at least once and validated for accuracy
6. Self-check has caught at least one real deviation in a project
7. At least one PLAYBOOK-CANDIDATES.md entry has been promoted to PLAYBOOK.md

Until all conditions are met, this is a specification, not a validated system.
