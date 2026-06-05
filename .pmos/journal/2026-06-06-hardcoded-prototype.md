# Hardcoded prototype — 10 FAQ pairs + Streamlit UI

Date: 2026-06-06
Type: build

## What happened
Built app.py: single-file Streamlit app with an inline FAQ lookup table.
5 HDFC schemes (Mid-Cap, Top 100, Small Cap, Gold FoF, Defence), 2 FAQ pairs each = 10 total.
Two modes: browse-by-scheme (expander UI) and keyword search.
Advisory query detection blocks comparison/recommendation questions by design.
Groww source citation attached to every answer.
Disclaimer banner on every page load.
requirements.txt: streamlit>=1.35.0 only — zero ML dependencies.

## Outcome
Working — syntax validated, data structure verified (5 schemes, 10 pairs, all URLs present).
Not yet deployed to Streamlit Cloud.

## Decisions
- Inline lookup table in app.py (no separate data file) — reduces file count for a prototype
- Advisory keyword blocklist hardcoded — sufficient for demo; replace with LLM classifier in v1
- Browse + Search dual mode — browse covers happy path, search sets up the query UX for RAG phase

## Learning
Single-file Streamlit prototype with inline data is the fastest path to a live demo.
Zero dependencies = zero deploy surprises on Streamlit Cloud.
Build the advisory guardrail from day 1 — it's a differentiator, not an afterthought.
