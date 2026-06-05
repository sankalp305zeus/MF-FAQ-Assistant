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
Hardcoded prototype built (app.py). 5 schemes, 10 FAQ pairs, Groww citations, advisory guardrail.
Syntax validated locally. Needs deploy to Streamlit Cloud.

## Next
Deploy to Streamlit Cloud → get live URL → verify one end-to-end query in browser.

## Decisions made
- Groq (Llama-3.3-70b) for generation — fast, free tier, sufficient for factual extraction
- BGE-small-en-v1.5 for embeddings — local inference, no API cost
- Streamlit for UI — ships fastest
- 5 HDFC schemes only — precision over breadth for v1

## Verified
None — project not yet started.

## Launch
- Target: Streamlit Cloud
- URL: not deployed
- Status: not-deployed

<!-- Launch checklist — complete before setting status to deployed-and-verified:
□ Health check endpoint returns expected response
□ One end-to-end test query returns correct result
□ Environment variables confirmed present (not assumed)
□ No errors in deploy logs
□ If multi-service: each service verified independently
-->
