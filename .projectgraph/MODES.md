# Modes

<!-- Maya sets Mode: in CONTEXT.md after inferring from Problem + Solution. -->
<!-- Human confirms or overrides. Default: mvp. -->

## Routing table

| Mode | When to use | Required files |
|---|---|---|
| **mvp** | Shipping a product fast. Solo or small team. | CONTEXT, NEXT, STATE, CONVENTIONS |
| **research** | Validating a market, user, or technology. No code yet. | CONTEXT, NEXT, STATE, RESEARCH |
| **ai-rag** | Building an AI product with retrieval, embeddings, or eval. | CONTEXT, NEXT, STATE, CONVENTIONS, RESEARCH |
| **saas** | Production SaaS — auth, billing, multi-tenancy. | CONTEXT, NEXT, STATE, CONVENTIONS, RESEARCH |
| **repo-rescue** | Existing or abandoned codebase. See REPO-RESCUE.md. | CONTEXT, NEXT, STATE, REPO-RESCUE |

## Mode rules

- Maya selects the mode. Human confirms or overrides.
- Changing mode = edit `Mode:` field in CONTEXT.md. Nothing else changes.
- Agents are activated on demand per task, not pre-loaded per mode.
- Max 5 required files per mode. If a mode needs more, re-cut it.

## On-demand agents (activated by Maya when needed)

| Agent | Role | Activate when |
|---|---|---|
| Nova | Research & validation | Assumptions need evidence, eval needed |
| Atlas | Systems architecture | Multi-component system, tech decisions |
| Forge | Builder | Implementation phase begins |
| Sentinel | QA & security | Pre-release review, security audit |

To activate: "Act as [Agent]. Read `.projectgraph/agents/[AGENT].md`."
