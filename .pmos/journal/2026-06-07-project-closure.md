# Project Closure — MF FAQ Assistant MVP

Date: 2026-06-07
Type: ship + learn

---

## What happened

Built, debugged, and shipped a production-grade mutual fund FAQ chatbot from scratch in approximately 3 days. The system answers factual questions about 5 HDFC schemes with Groww source citations, refuses advisory/comparison queries by design, and is live at groww-chat-buddy.lovable.app.

---

## Timeline

| Date | Milestone |
|---|---|
| 2026-06-04 | Ingestion pipeline built — 5 schemes, 51 chunks, 9 sections each |
| 2026-06-05 | FastAPI backend deployed to Railway. 403 incident (single railway.toml) investigated and resolved. |
| 2026-06-06 | Lovable frontend built and connected to Railway backend. Bug-001 (scheme_name dropped) identified, investigated, fixed, deployed. Production verified — all 5 tabs working. |
| 2026-06-07 | Bug-002 (AUM grounding failure, Cr vs crore) quantified, fixed, deployed. MVP production-verified. Project closure. |

---

## Decisions made

- **Groq + Llama-3.3-70b** for generation — fast, free tier, sufficient factual extraction
- **BGE-small-en-v1.5** for embeddings — local inference, no API cost, 384-dim
- **Lovable** for frontend — fastest path to a functional React UI, GitHub-synced
- **Single Railway service** — avoided the prior v2 mistake of splitting into two services with one railway.toml
- **Enriched retrieval query** (not backend schema split) for scheme context — least invasive fix
- **Validator normalisation at comparison** (not corpus rewrite) for Cr→crore — minimal blast radius

---

## Major milestones

1. Investigation-first protocol followed on both bugs — no blind fixes
2. Full corpus quantification before proposing validator fix
3. All fixes backtested locally before Railway deploy
4. CHECKPOINT.md maintained across both bugs
5. Zero rollbacks — every deploy worked

---

## Key learnings

1. **Test the API boundary, not just each component.** The frontend-backend contract was never explicitly tested. A single integration test would have caught Bug-001 before deployment.

2. **LLMs expand abbreviations.** Source data abbreviations will always be expanded by the LLM. Normalise at ingestion, not at query time.

3. **Pydantic silent field dropping is a footgun.** Extra fields disappear without error. Use `extra='forbid'` to surface mismatches immediately.

4. **UI-built tools (Lovable) send payloads you don't control.** Always inspect the actual network payload before writing the backend schema.

5. **Quantify before fixing.** The Cr/crore analysis (51 chunks, every unit occurrence counted) took 10 minutes and prevented a wrong fix. The proposed normalization approach (remove ₹, commas) would not have worked. Investigation saved a second deploy cycle.

6. **PMOS investigation protocol works.** FACT/DISPROVEN/UNKNOWN discipline kept both debug sessions focused and short.
