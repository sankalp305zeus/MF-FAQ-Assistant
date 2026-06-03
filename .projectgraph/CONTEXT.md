# Context

## Identity
- Name: ProjectGraph OS
- Slug: projectgraph-os
- One-liner: Local AI-operated project orchestration with structured handoffs
- Type: product
- Stage: prototype
- Mode: mvp

## Problem
AI-driven project work lacks a consistent local memory format and clear handoff rules across sessions.

## Solution
Provide a minimal `.projectgraph/` OS that standardizes handoffs, limits loaded context, and makes every phase executable by a single agent.

## Constraints
- Zero runtime dependencies outside markdown files
- Tool-agnostic: any IDE or LLM loads only authorized context files
- No legacy v3 file patterns may be active during execution
- Human approval is required at gates and mode changes

## Rules
- Always load `.projectgraph/CONTEXT.md` and `.projectgraph/ACTIVE.md` first
- Every agent reads only files listed in its startup protocol
- Handoffs are mandatory, append-only, and schema-complete
- Change mode only by editing `Mode:` in `.projectgraph/CONTEXT.md`

## Assumptions (unvalidated)
- This repo is a bootstrap for ProjectGraph OS v4-beta
- The current state is a new setup, not a completed product
