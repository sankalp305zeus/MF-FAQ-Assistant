# Eval

<!-- AI: read this before suggesting changes that affect quality or correctness. -->
<!-- Track what "good" looks like — not just what passes tests. -->

## Success criteria

<!-- What does a working system look like to a real user? -->

| Scenario | Expected result |
|----------|-----------------|
| [Happy path] | [Specific observable output] |
| [Edge case] | [Specific observable output] |
| [Failure / degraded mode] | [Acceptable fallback behaviour] |

---

## Smoke test checklist

<!-- Run this after any significant change. Binary pass/fail per step. -->

| # | Step | Expected |
|---|------|----------|
| 1 | [Setup step] | [No errors] |
| 2 | [Typical input] | [N results with explanations] |
| 3 | [Impossible / empty input] | [Friendly empty state + hints] |
| 4 | [Fallback mode, e.g. MOCK_LLM=1] | [Degraded but functional output] |
| 5 | [Test suite] | [All tests pass] |

---

## LLM-specific checks

<!-- Only fill if the project uses an LLM. -->

- [ ] Output is grounded in provided data — no hallucinated facts outside the input
- [ ] Fallback activates when LLM is unavailable or returns malformed output
- [ ] Prompt injection surface is constrained (length caps, scope restrictions)
- [ ] API key is never logged or leaked in responses

---

## Known limitations

<!-- Honest list of what this system does NOT do well. AI should surface these when relevant. -->

- [e.g. Dataset coverage — only validated for City X; other cities have sparse data]
- [e.g. Budget bands are heuristic, not validated against real pricing]

---

## Open eval questions

<!-- Things we want to measure but haven't yet. -->
- [e.g. What is the false-positive rate on the filter step for edge-case cuisines?]
