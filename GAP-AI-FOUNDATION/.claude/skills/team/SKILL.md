---
name: team
description: Consult your 4 expert advisors — software architect, risk analyst, senior PM, or Claude expert
---

# /team — Consult Your Workforce

Summon one of your 4 expert advisors to help with decisions, risks, strategy, or Claude/Anthropic technical questions.

## Usage

Type `/team` or say "consult my team" / "ask an expert" / "get a second opinion" — you'll be presented with a menu of your advisors.

## Your Advisors

1. **Software Architect** — Design tradeoffs, system scalability, integration risk, skill/agent architecture
2. **Risk Analyst** — Schedule/client/delivery risk assessment, mitigation strategies, escalation triggers
3. **Senior Program Manager** — Scope/schedule decisions, stakeholder strategy, team dynamics, communication framing
4. **Claude Expert** — Claude models, Claude Code, agents, MCP, prompt design, OS improvements

## What They Do

- Ask clarifying questions first, then advise
- Frame tradeoffs and reasoning explicitly
- Ground advice in your project context (Mediquant DOM, your OS, your stakeholders)
- Recommend next steps; Nelson and Alfred decide and execute
- Do not write code or modify files

## Implementation Notes

This skill presents a menu (via `AskUserQuestion`) and routes your question to the chosen expert via the `Agent` tool with the appropriate `subagent_type`. The expert's response is relayed back conversationally.

Reuses the same pattern as the `portfolio` skill (skill wraps an agent invocation).
