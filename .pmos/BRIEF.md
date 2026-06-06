# RAG-MF-FAQ

## What
Facts-only FAQ chatbot that answers mutual fund scheme questions with source citations from Groww.

## Why
Retail investors spend 3-5 minutes per lookup navigating dense AMC pages. A fast, cited, facts-only answer reduces friction and prevents reliance on unverified social media sources.

## Success looks like
- Answers 10 common MF scheme questions correctly with source citations
- Advisory/comparison queries are refused by design
- Live demo accessible via URL
- Evaluation dataset of 24 questions scored for precision and groundedness

## Constraints
- Free tier only (Groq, Railway/Streamlit Cloud)
- No investment advice — facts only
- 5 HDFC schemes for v1 (narrow corpus = high retrieval precision)
- Solo builder, ship in 1 week

## Rules
- Use existing libraries before writing custom code (LangChain splitter > custom chunking)
- Every answer must carry a Groww source citation URL
- Deploy as single service — split only when necessary
- Build evaluation dataset BEFORE building pipeline

## Now
MVP shipped and production-verified. All 5 HDFC schemes live. Full RAG pipeline deployed.
Two bugs fixed post-deploy (Bug-001: scheme_name dropped; Bug-002: AUM grounding failure).
Project closed.

## Next
1. Confirm RAILWAY_DEPLOY_HOOK_URL in GitHub Secrets for automated daily refresh
2. Build evaluation dataset — 24 questions scored for precision and groundedness
3. Expand to 14 additional schemes across other AMCs

## Decisions made
- Groq (Llama-3.3-70b) for generation — fast, free tier, sufficient for factual extraction
- BGE-small-en-v1.5 for embeddings — local inference, no API cost
- Streamlit for UI — ships fastest
- 5 HDFC schemes only — precision over breadth for v1

## Verified
2026-06-07 — MVP production verified.
All 5 tabs tested: HDFC Mid-Cap, Large Cap, Small Cap, Gold ETF FoF, Defence.
AUM, expense ratio, exit load, fund manager, minimum SIP — all returning answers with Groww citations.
Refusal behaviour confirmed on advisory queries.
Grounding validator confirmed catching hallucinated numbers.

## Current Architecture
- Backend: FastAPI + BGE-small-en-v1.5 + ChromaDB + Groq (llama-3.3-70b-versatile)
- Frontend: Lovable (React/TypeScript)
- Deploy: Railway (backend) + Lovable Cloud (frontend)
- Ingestion: GitHub Actions — daily 10:00 AM IST

## Evaluation Outcome
Functional verification passed. Formal eval dataset (24 questions, precision + groundedness scoring) not yet built — next milestone.

## Launch
- Target: Railway (backend) + Lovable (frontend)
- URL: https://groww-chat-buddy.lovable.app
- Backend: https://mf-faq-chatbot-v2-clean-production.up.railway.app
- Status: deployed-and-verified

<!-- Launch checklist — complete before setting status to deployed-and-verified:
□ Health check endpoint returns expected response
□ One end-to-end test query returns correct result
□ Environment variables confirmed present (not assumed)
□ No errors in deploy logs
□ If multi-service: each service verified independently
-->
