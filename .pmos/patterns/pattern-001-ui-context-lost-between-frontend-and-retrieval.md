# Pattern 001 — UI Context Lost Between Frontend and Retrieval Layer

Date captured: 2026-06-07
Project: mf-faq-chatbot-v2
Reuse: yes — any project with a tabbed/contextual UI feeding a backend retrieval system

---

## Problem

User selects a context in the UI (scheme tab, category filter, date range, etc.).
Frontend sends that context to the backend.
Backend schema does not declare the field.
Field is silently dropped.
Retrieval runs without context → wrong or empty results.
User sees failure. Developer sees no error.

---

## Symptoms

- Contextless queries ("Who is the fund manager?") always fail.
- Full-name queries ("What is the expense ratio of HDFC Mid Cap?") work fine.
- No 422 or 400 error — backend returns 200 with a refusal or empty result.
- Switching UI context (tab, filter, dropdown) has no effect on results.

---

## Detection Method

1. Inspect the exact network payload from the frontend (browser DevTools → Network → POST body).
2. Compare every key in the payload against the backend request schema.
3. Any key present in payload but absent in schema = dropped field.
4. Confirm: does the retrieval function receive the context? Add a log line.

---

## Root Cause

API contract mismatch. Frontend built assuming backend accepts context field.
Backend schema written for a different query style (full natural-language names).
Pydantic (and most validation libraries) silently discard extra fields by default.
No integration test exercises the boundary with realistic frontend payloads.

---

## Fix

**Option A — Backend schema (preferred):**
Add `context_field: Optional[str] = None` to the request model.
Use it to enrich the retrieval query: `f"{message} for {context_field}"`.
Keeps frontend unchanged. Zero risk if field is absent (backward compatible).

**Option B — Frontend enrichment:**
Prepend context to message before sending: `"${message} for ${selectedContext}"`.
No backend change required. Works immediately with existing deployed backend.
Downside: couples natural-language query construction to frontend logic.

---

## Prevention Strategy

1. **Contract test at project start:** Write one pytest that sends the full realistic frontend payload and asserts the backend accepts it without 422.
2. **Strict extra-field rejection:** Use `model_config = ConfigDict(extra='forbid')` in Pydantic so extra fields raise a 422 immediately rather than disappearing silently.
3. **Integration test before first deploy:** Test with a short/contextless query (not just a full-name query) against the live or staging backend.
4. **Frontend-backend handoff review:** When the frontend is built by a different tool (Lovable, v0, etc.), explicitly check what payload shape it sends before writing the backend schema.
