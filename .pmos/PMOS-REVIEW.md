# PMOS Learning Review — MF FAQ Assistant

Date: 2026-06-07
Project: mf-faq-chatbot-v2
Review type: Post-MVP closure

---

## What PMOS handled well

**Investigation protocol:** The FACT/DISPROVEN/UNKNOWN framework was followed on both bugs. Both were diagnosed correctly before any fix was attempted. No wasted deploy cycles from blind fixes.

**Anti-waste scoring:** Hardcoded prototype day 1 was flagged as the right starting point. The system correctly challenged the temptation to build the full RAG pipeline immediately.

**BRIEF.md as context anchor:** Loading BRIEF.md before every session kept Maya oriented without re-deriving project context from scratch. Worked as designed.

**Journal entries:** Append-only journal captured decisions, outcomes, and learnings at each milestone. CHECKPOINT.md served as a real-time bug tracker.

**Single-service deploy rule:** Prevented the prior v2 mistake (split railway.toml) from recurring. Explicit constraint in BRIEF.md enforced during build.

---

## What PMOS missed

**No frontend-backend contract governance.**
PMOS has no template or checklist for verifying API contract alignment when a frontend is built by an external tool (Lovable, v0, Cursor, etc.). Bug-001 would have been caught pre-deploy with a single contract check step.

**No corpus audit step in RAG project pattern.**
The RAG project pattern says "build evaluation dataset before pipeline." It does not say "audit corpus for unit abbreviations, formatting inconsistencies, and LLM output convention mismatches before writing the validator." Bug-002 was entirely preventable at ingestion time.

**No integration test mandate.**
PMOS says "ship > optimize." This is correct. But it does not say "write one integration test per API boundary before first deploy." The framework needs a lightweight integration gate — not a full test suite, just one realistic end-to-end request.

**No external tool handoff protocol.**
When a frontend is built by Lovable/v0/Cursor, the developer does not control the payload shape. PMOS has no step for "inspect actual network payload from external tool before writing backend schema."

---

## New governance rules required

**Rule: API Contract Review before first backend deploy.**
Before any backend is deployed, explicitly verify: what payload does the frontend send? Does the backend schema accept every field? One network inspect + one schema diff check. Takes 5 minutes. Prevents Bug-001 class failures.

**Rule: Corpus Normalisation Audit before writing validators.**
For any RAG project, before writing a grounding or factual validator, scan the full corpus for unit abbreviations, currency symbols, date formats, and number formatting conventions. Compare against LLM output conventions. Document mismatches. Takes 30 minutes. Prevents Bug-002 class failures.

**Rule: One integration test per API boundary.**
Before declaring a feature "done", write one pytest (or equivalent) that exercises the full request path with a realistic payload from the actual client. Not a unit test. Not a smoke test. A request that looks exactly like what the frontend sends.

---

## New templates required

**Template: API Contract Checklist (add to BRIEF.md Rules section)**
```
Before first deploy:
□ Inspect actual frontend payload (DevTools or source code)
□ Every payload field present in backend request schema
□ Test with short/contextless query, not just full-name query
□ Extra field handling confirmed (forbid or accept explicitly)
```

**Template: Corpus Audit Checklist (add to RAG Project Pattern)**
```
Before writing validator:
□ Scan all chunks for unit abbreviations (Cr, Lakh, Mn, Bn, K)
□ Scan for currency symbol variants (₹, Rs., INR)
□ Scan for number formatting (Indian vs Western commas)
□ Compare each against expected LLM output form
□ Document mismatches. Normalise at ingestion if possible.
```

---

## Improvements to bootstrap-sequence.md

Add step after "fill BRIEF.md":

> **If project has a frontend + backend boundary:**
> Add to BRIEF.md Constraints: "API contract review required before first backend deploy."
> Add to Rules: "Inspect actual frontend payload before writing backend schema."

---

## Improvements to evaluation-framework.md

Add to RAG project evaluation:

> **Corpus QA pass** (before ingestion is finalised):
> - All unit abbreviations documented and normalised
> - All numeric fields verified to match LLM output convention
> - At least one end-to-end query per section type tested against the validator

---

## Improvements to agent-protocol.md

Add to "Definition of Done" for API features:

> An API endpoint is done when:
> 1. At least one integration test sends a realistic frontend payload
> 2. Backend schema explicitly declares all fields the frontend sends
> 3. Extra-field behaviour is documented (forbid / ignore / explicit)

---

## N8N in Future Projects

N8N should be brought in as the operational automation layer from the start of the next project — not retrofitted after MVP.

**What N8N replaces:**
- Manual Railway deploy after GitHub Actions ingestion
- Manual health checks
- Manual error monitoring of deploy logs
- Manual sharing of production URLs

**Recommended N8N workflows for next RAG project:**

| Workflow | Trigger | Steps |
|---|---|---|
| **Daily data refresh + deploy** | Schedule (10 AM IST) | GitHub Actions ingest → wait → POST Railway deploy hook → Slack notify |
| **Health monitor** | Cron every 15 min | GET /health → if non-200 → WhatsApp/Slack alert |
| **Error alerter** | Railway log webhook | Parse for `grounding_failure`, `Groq failed`, `scheme_resolved=False` → notify with context |
| **Feedback capture** | Lovable webhook on thumbs down | Log query + answer to Notion → tag for eval dataset |
| **Eval dataset builder** | Manual trigger | Pull last 50 queries from logs → format as JSONL → push to GitHub → open PR |
| **Uptime report** | Weekly schedule | Aggregate /health checks → response time P50/P95 → send summary |

**Integration approach:**
- N8N Cloud (free tier) for orchestration
- Railway webhook URL as deploy trigger
- GitHub API for pushing eval datasets
- Notion/Airtable as the lightweight data store
- WhatsApp Business API or Slack for alerts

**Why N8N over cron + scripts:**
Visual workflow editor means non-engineer stakeholders can inspect and modify operational flows. Error handling and retry logic built in. No new Python scripts to maintain. Audit trail of every workflow execution.
