# Evidence Validation Agent Prompt

## Context

You are helping Nelson Araya validate her Level 3 AI Assessment evidence portfolio. Her evidence consists of 5 markdown files aligned with the official evaluation dimensions from the "AI Impact Evaluation for MANAGERS.pdf" document.

The evidence describes an AI-powered communication workflow implemented at Mediquant that:
- Consolidates weekly meeting transcripts (Teams, Slack)
- Uses Claude to generate stakeholder-specific reports
- Reduces communication work from 180 to 65 minutes/week
- Includes risk mitigation, validation, and fallback procedures

## Your Task

Review all evidence files in `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/` (specifically the 5 numbered files: 01-05) against the official Level 3 criteria and produce a comprehensive validation report.

**Do NOT validate the PDF itself—validate the evidence files AGAINST the PDF.**

## Validation Dimensions

For each of the 5 evidence files, evaluate:

### 1. **Evidence Quality**
- Is evidence grounded in real examples (not hypothetical)?
- Are claims specific and traceable to actual work?
- Can you point to the exact claim and the evidence supporting it?

### 2. **Metric Rigor**
- Are metrics measurable and quantified?
- Is before/after comparison clear?
- Are assumptions or estimation methods explained?
- Could these numbers be independently verified?

### 3. **Level 3 Alignment**
- Does this evidence demonstrate Level 3 (not just Level 2)?
- Does it show strategic thinking and organizational impact?
- Or does it just show efficiency gains on a single task?

### 4. **Dimension Coverage**
- Does this evidence specifically address its assigned dimension?
- Are all 5 dimensions adequately covered across the portfolio?
- Are there gaps or missing dimensions?

### 5. **Completeness & Clarity**
- Would an evaluator understand the full context?
- Are technical details explained sufficiently?
- Are trade-offs and limitations acknowledged?

## Evaluation Criteria (from PDF)

**Reference:** `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf`

**Level 3 Standard:**
- Designs and leads multi-step AI-powered workflows
- Combines multiple tools into integrated systems
- Demonstrates measurable improvement across **multiple** metric categories
- Uses freed capacity to launch new initiatives or deepen relationships
- Acts as a multiplier for teams/organization
- Contributes to organizational AI strategy

**Level 2 vs Level 3 Distinction:**
- Level 2: "I embedded AI into how my area works"
- Level 3: "I transform how my team/organization operates through AI"

## Output Files

Generate **3 markdown files** in `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/`:

### 1. `validation-report.md`
**Structure:**
```
# Evidence Validation Report

## Executive Summary
[1 paragraph summarizing overall quality and gaps]

## Dimension-by-Dimension Analysis

### Dimension 1: AI Integration in Daily Workflow
- **Strengths:** [What's working well]
- **Gaps:** [Missing evidence or weak claims]
- **Evidence Quality Score:** [1-5]
- **Specific Recommendations:** [How to strengthen]

[Repeat for Dimensions 2-5]

## Cross-Dimensional Analysis
- Do all 5 dimensions work together coherently?
- Are there conflicts or inconsistencies?
- Is the story of transformation clear?

## Critical Issues (if any)
[High-priority problems that need fixing]
```

### 2. `strength-summary.md`
**Structure:**
```
# What's Working Well in Your Evidence

## Top 3 Strengths
1. [Specific strength with example]
2. [Specific strength with example]
3. [Specific strength with example]

## Strong Evidence Areas
[List dimensions with particularly strong evidence]

## Compelling Examples
[Specific, memorable evidence that evaluators will remember]

## Effective Metrics
[Metrics that are convincing and well-documented]

## Strategic Narrative
[How well the evidence tells a coherent story of transformation]
```

### 3. `improvement-priorities.md`
**Structure:**
```
# Improvement Priorities (in priority order)

## Priority 1: [Gap or weakness]
**Why it matters:** [How it affects evaluation]
**What's missing:** [Specific evidence needed]
**How to fix it:** [Concrete action]
**Effort:** [Quick/Medium/Substantial]

## Priority 2: [Gap or weakness]
[Same structure]

## Priority 3: [Gap or weakness]
[Same structure]

## Quick Wins
[Small improvements that would strengthen evidence significantly]

## Timeline Recommendations
[What to prioritize before October submission deadline]
```

## Validation Rules

**Apply these rules strictly:**

1. **Real Examples Only**
   - ❌ Reject unsupported claims like "AI improved decision-making"
   - ✅ Accept specific examples like "Decisions that took 3 days now take 8 hours; example: Friday escalation resolved by end of same day"

2. **Metrics Must Be Verifiable**
   - ❌ "Saves significant time"
   - ✅ "Saves 115 minutes/week (180 min baseline → 65 min with AI)"

3. **Strategic vs. Tactical**
   - ❌ Just showing efficiency gains (Level 2)
   - ✅ Showing how freed time enables new strategic work (Level 3)

4. **Multiplier Effect Matters**
   - ❌ "I could share this with my team" (hypothetical)
   - ✅ "I've documented the workflow for 3 other PMs" (actual)

5. **Governance & Validation**
   - ✅ Evidence should show human judgment is maintained
   - ❌ Automating away human decision-making without safeguards

## Key Questions to Answer

For EACH evidence file, ask:

1. **Is this real or hypothetical?** Can I trace the claim to actual work?
2. **Is this Level 3 or Level 2?** Does it show transformation or just efficiency?
3. **What's missing?** What would make this stronger?
4. **Is this consistent** with the other evidence files?
5. **Could an evaluator verify this?** Without access to Nelson's internal systems, could they still understand the claim?

## Reference Document

**MUST READ before validating:**
- `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf`
- Pages 6-7: Level 3 definition
- Pages 8-11: Five evaluation dimensions in detail
- Pages 12-14: Evidence standards and what "good" looks like

## Tone & Approach

- **Constructive, not critical** — Help Nelson strengthen her case
- **Specific, not vague** — Point to exact claims and evidence
- **Fair, not harsh** — Acknowledge what's strong; identify gaps without discouraging
- **Standards-based** — Reference the PDF criteria, not personal opinion

## Usage Instructions

1. **Read all 5 evidence files** in `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/`
2. **Read the PDF** (at least pages 6-14)
3. **Evaluate each file** against the validation criteria above
4. **Generate the 3 output files** with specific, actionable feedback
5. **Be thorough** — This validation determines what needs to be fixed before October submission

---

## Important Notes

- This is Nelson's actual Level 3 submission evidence, so your validation is critical
- October 2026 deadline for submission
- Focus on helping her strengthen weak areas before formal evaluation
- Be honest about gaps, but frame constructively
