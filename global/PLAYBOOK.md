# Playbook

Cross-project organizational memory. Append-only. Newest at top.
Copy this file to ~/.pmos/PLAYBOOK.md on your machine.

---

## PM Patterns

Reusable project-type patterns. These grow as you ship projects.

<!-- After 3+ projects, add pattern entries here like:

## RAG Project Pattern
Context: AI project with retrieval, embeddings, vector search
Approach:
1. Start with 10 hardcoded QA pairs + Streamlit UI — ship demo day 1
2. Replace with real retrieval: use existing splitter library, hosted embeddings, managed vector DB
3. Build evaluation dataset BEFORE building pipeline
4. Deploy as single service — split only when necessary
5. Add source citations on every answer — this is the portfolio differentiator
Key tradeoffs: narrow corpus > broad corpus for v1. Local embeddings > API if cost matters.
Outcome: MF FAQ shipped in ~10h with this approach
Reuse: yes
Project: mf-faq-chatbot-v2
Date: YYYY-MM-DD

-->

---

## Investigation Protocol

Use this when something is broken. Stop fixing. Start investigating.

Context: Production incident, deployment failure, or any bug requiring root-cause diagnosis.

Approach:
1. STOP. Do not attempt fixes before diagnosis.
2. Create an investigation section in the current journal entry.
3. Collect FACTS with evidence. Number them (FACT-001, FACT-002...).
4. For every hypothesis: attempt to DISPROVE it with evidence. Number them (DISPROVEN-001...).
5. Track UNKNOWNS explicitly. Number them (UNKNOWN-001...). Resolve each before acting.
6. Identify root cause only after hypotheses are tested against evidence.
7. Fix the root cause, not the symptom.
8. Verify the fix with evidence (health check, curl, actual response — not assumption).

Outcome: Successfully resolved MF FAQ 403 incident. 20 facts collected, 5 hypotheses disproven,
6 unknowns resolved. Root cause identified as single railway.toml controlling two services.
Reuse: yes — every time something breaks
Project: mf-faq-chatbot-v2
Date: 2026-06-05

---

## Successful Patterns

<!-- Append new patterns here as they emerge from real projects. Schema:

## [Pattern name]
Context: [When to use this — project type, phase, situation]
Approach: [What to do — exact steps or prompt that worked]
Outcome: [What happened]
Reuse: [yes | no | conditional: when]
Project: [slug]
Date: YYYY-MM-DD

-->

---

## Failed Patterns

<!-- Patterns that looked good but failed. Record them to prevent repeating.

## [Pattern name]
Context: [What was happening]
Approach: [What was tried]
Outcome: Failed — [why]
Reuse: no
Lesson: [What to do instead]
Project: [slug]
Date: YYYY-MM-DD

-->
