# Pattern 002 — Grounding Validator Unit Alias Mismatch

Date captured: 2026-06-07
Project: mf-faq-chatbot-v2
Reuse: yes — any RAG system with a numeric grounding validator and scraped corpus data

---

## Problem

Source data uses abbreviated units (`Cr`, `Lakh`, `Mn`, `Bn`, `K`).
LLM expands abbreviations to full words (`crore`, `lakh`, `million`, `billion`, `thousand`) in generated answers.
Grounding validator performs literal substring match: extracted number + expanded unit not found in chunk text.
Grounding failure → link-only fallback or refusal.
The answer was correct. The validator rejected it for a formatting reason, not a factual one.

---

## Symptoms

- One specific query type always returns fallback ("unable to generate / visit scheme page").
- All other query types work correctly.
- Deploy log shows `grounding_failure: ['<number> <full_unit>']` consistently.
- The number IS present in the corpus — just with a different unit string.
- Example: chunk has `₹2,70,046 Cr`, answer has `₹2,70,046 crore` → failure.

---

## Detection Method

1. Find the grounding failure log: `grounding_failure: ['X']`.
2. Extract the failing number token: e.g. `2,70,046 crore`.
3. Search corpus chunks for the number without unit: `2,70,046` → found in chunk as `₹2,70,046 Cr`.
4. Confirm: chunk unit (`Cr`) ≠ extracted unit (`crore`).
5. Reproduce locally: feed simulated LLM answer to `check_grounding()` with real retrieved chunks.

---

## Root Cause

Two-layer mismatch:
1. Source HTML uses abbreviated units (Groww uses `Cr` for crore, financial sites use `Lakh`, `Mn`, etc.).
2. LLMs are trained on text where full words dominate — they expand abbreviations consistently and reliably.
3. Grounding validator uses literal `in` substring match with no normalisation layer.

---

## Fix

**Minimal (comparison normalisation):**
In `check_grounding()`, normalise chunk text before comparison only:
```python
chunk_text_normalised = re.sub(r"\bCr\b", "crore", all_chunk_text)
if num_clean not in chunk_text_normalised:
    ungrounded.append(num_clean)
```
Answer text, corpus, and outputs remain unchanged.

**Better (corpus normalisation at ingestion):**
In the ingestion/parse layer, normalise units during extraction:
replace `Cr` → `crore`, `Lakh` → `lakh` in chunk text before storing in ChromaDB.
Eliminates the need for runtime normalisation entirely.

---

## Prevention Strategy

1. **Corpus audit before writing validator:** Scan all chunk texts for unit abbreviations. Build a unit alias map before the validator is written.
2. **Normalise at ingestion, not at query time:** Clean up abbreviations in `sections.py` or `chunk.py` so the stored text already matches LLM output conventions.
3. **Grounding validator design principle:** Always normalise both sides (answer + chunk) before comparison. Never assume the source and the LLM use identical string representations.
4. **Unit alias test in validator suite:** Assert that `"2,70,046 crore"` passes grounding when chunk contains `"₹2,70,046 Cr"`.
5. **Validate every numeric field type during ingestion QA:** AUM, NAV, minimum investment — run a spot check comparing chunk text format to expected LLM output format.
