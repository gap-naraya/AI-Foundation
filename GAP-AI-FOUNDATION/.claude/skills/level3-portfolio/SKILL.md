---
name: level3-portfolio
description: Use this skill when the user mentions "Level 3", "AI assessment", "Transformer", "certification", "portfolio", "evidence", "GAP evaluation", "merit increase", or anything related to the GAP AI Impact Evaluation. Also triggers when the user asks how their current work maps to AI maturity, or wants to prepare for the October re-evaluation.
---

# Level 3 AI Portfolio Skill

Nelson's goal is to reach **Level 3 — AI Value Leader** on GAP's AI Impact Evaluation by the October 2026 re-evaluation window. Passing unlocks his merit increase.

## The 5 Evaluation Dimensions (what Nelson is scored on)

| # | Dimension | Level 3 Criteria |
|---|---|---|
| 1 | **AI Integration in Daily Workflow** | AI is the default starting point for ALL management workflows. Designed repeatable AI-powered processes for recurring work. Time reclaimed from admin is reinvested in strategy/relationships. |
| 2 | **Appropriate Use & Validation** | Models exemplary validation behavior. Contributes to responsible use practices. Coaches others. Knows where AI should NOT replace human judgment. |
| 3 | **Productivity & Measurable Impact** | Demonstrates improvement across MULTIPLE metric categories (Decision Cycle Time, Output Quality, Team Throughput, Communication Efficiency, Strategic Leverage of Time, Knowledge Management). |
| 4 | **Capacity to Design & Orchestrate AI Processes** | Designs multi-step AI-powered workflows (Claude Code, N8N, Zapier, or custom integrations). Creates reusable blueprints adopted by others. |
| 5 | **AI as Multiplier Across Teams** | Systematically uplevels team AI maturity. Creates frameworks adopted by other managers. Uses AI to unlock commercial value. Contributes to org AI strategy. |

## Validation best practices (Dimension 2)
- **Source Check** — verify AI outputs against source data
- **Bias Scan** — scan for bias or missing context
- **Contextual Fit** — evaluate if output fits the specific situation
- **Stakeholder Lens** — consider how each stakeholder will read the output
- **"Name on It" Test** — would you publish this with your name on it as-is?

## What Nelson already has (evidence map)

### Dimension 1 — Daily Workflow Integration ✅ Strong
- EoD report helper (`/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/helpers/eod-report.md`) — automated daily status reporting
- Client email generation from same notes
- Slippage detection via previous snapshot system
- Stakeholder communication drafter skill
- Memory system across sessions (`~/.claude/projects/...`)

### Dimension 2 — Validation ✅ Strong
- Human-in-the-loop on every report (Nelson reviews before sending)
- All AI outputs reviewed before Slack/email delivery
- Can articulate: "I review and edit every output; I do not send anything I cannot defend without mentioning AI"

### Dimension 3 — Measurable Impact 🔶 Needs evidence
- Need to quantify: time saved per EoD report (estimate: ~30 min/day)
- Need to quantify: revision rounds reduced on client email
- Need to document: before/after comparison on report turnaround
- **Action:** Start capturing time-saved metrics starting today

### Dimension 4 — AI Process Design ✅ Strong
- Built this entire Claude OS (context files at `GAP-AI-FOUNDATION/context/`, helpers, project structure, skills, memory)
- EoD helper is a multi-step, multi-format automated workflow
- Skills/agents architecture now in place
- **Action:** Document the architecture as a reusable blueprint for other PMs at GAP

### Dimension 5 — Multiplier Effect 🔶 Needs evidence
- Currently individual (no direct reports to coach)
- **Action:** Share this system (or a sanitized version) with Gerardo or other PMs at GAP as a reusable framework. Document that it was shared and adopted.

## Skill modes — what Nelson can ask for

### Mode 1: Evidence audit
"Audit my Level 3 evidence" → Review all 5 dimensions, identify what's documented vs. what's missing, and produce a gap list.

### Mode 2: Draft self-evaluation answers
"Draft my Level 3 self-evaluation for Dimension [X]" → Write a compelling, evidence-based answer for the GAP evaluation form for that specific dimension.

### Mode 3: Map today's work to Level 3
"Does [X] count toward Level 3?" → Analyze a specific work output or activity and identify which dimension(s) it supports and how to document it.

### Mode 4: Portfolio update
"Update my Level 3 portfolio" → Add a new evidence item from today's work to the running evidence log at `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/ai_impact_evaluation/evidence-log.md` (create if it doesn't exist).

## Key dates
- **July 2026**: Re-evaluation window (first checkpoint)
- **October 2026**: Final re-evaluation (target for Level 3 certification + merit increase)
- **Weekly commitment**: 6 hours/week (Tue 1h, Thu 2h, Weekend 3h)

## Important rules
- Evidence must be real, from the past 6 months, verifiable
- Do not exaggerate or make unverifiable claims
- No full client source code in evidence (snippets or screenshots only, credentials removed)
- If uncertain whether something qualifies, default to documenting it and letting the evaluator decide
