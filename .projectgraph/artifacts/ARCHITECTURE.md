# Architecture

<!-- AI: read this when making structural or technology decisions. -->
<!-- Keep to bullets and tables. No prose padding. -->

## Goals

| Goal | Rationale |
|------|-----------|
| [e.g. Separation of concerns] | [Why it matters for this project] |
| [e.g. Structured-first, LLM-second] | [Reduces hallucination + token cost] |
| [e.g. Graceful degradation] | [LLM failure must not crash the user flow] |

---

## System layers

<!-- List layers top-to-bottom. Layers depend only downward. -->

```
Layer N — [Name]     [folder/]
...
Layer 1 — [Name]     [folder/]
```

| Layer | Module | Responsibility |
|-------|--------|----------------|
| [N] | `path/to/module` | [What it owns] |

---

## Data contracts

<!-- One block per boundary crossing. Keep schemas minimal. -->

### [Input name]
```json
{ "field": "type — description" }
```

### [Output name]
```json
{ "field": "type — description" }
```

---

## Key flows

<!-- Sequence or flowchart for the primary happy path only. -->

```
[Actor] → [Step] → [Step] → [Output]
```

---

## Technology choices

| Concern | Choice | Why / Alternatives considered |
|---------|--------|-------------------------------|
| [e.g. LLM] | [e.g. Groq llama-3.3-70b] | [Fast inference; fallback to rule-based if unavailable] |

---

## Cross-cutting concerns

### Security
- [e.g. API keys in env only — never logged, never in image]

### Reliability
- [e.g. LLM timeout → fallback to deterministic rankings]

### Observability
- [e.g. Structured log per pipeline step: step name, latency_ms, result code]

---

## Known limitations

- [Hard constraint or scope boundary — be specific]
