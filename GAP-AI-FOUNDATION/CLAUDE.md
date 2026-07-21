# CLAUDE.md — GAP-AI-FOUNDATION (Mediquant Project)

This file contains instructions specific to Nelson's work with Growth Acceleration Partners (GAP) and the Mediquant project. It loads **after** the root CLAUDE.md, so foundational rules and Nelson's identity are already established.

---

## About Nelson's GAP Role

Nelson is a Senior Project Manager at Growth Acceleration Partners, leading a critical Mediquant DOM automation project. To understand his context and decision-making, refer to these files:

- **2026 Goals** → `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/context/2026_Goals_Context.md`
- **Career Context** → `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/context/Career_Context_Document.md`
- **Communication Style** → `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/context/Communication_Context.md`
- **Business Context** → `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/context/Business_Context.md`

---

## Current Situation

Executing a complex project currently off-track, creating monetary and business complications due to high client relevance. Operating under time pressure with a strained client relationship. C-level visibility across the company on project status and progress.

**Environment requires:**
- Careful, data-driven communication
- Rapid, efficient decision-making
- Transparent stakeholder updates
- Risk mitigation and clear accountability

---

## Available Tools & Skills

The following skills activate only when working in GAP-AI-FOUNDATION:

- `/eod` — Daily Mediquant status report generation
- `/gantt` — Weekly Gantt chart Excel generator from ADO CSV export (for Ken & Shawn)
- `/escalate-gerardo` — Escalate blockers to Gerardo (manager)
- `/draft-message` — Draft professional communications (Slack, email)
- `/portfolio` — Level 3 AI Impact Evaluation portfolio (6 modes: scan, approve, audit, draft, map, update)
  - **Automated weekly scan:** Cloud routine runs every Monday at 10am Costa Rica time, detects new evidence, reports findings
- `/team` — Consult your 4 expert advisors: **Software Architect** (design/architecture), **Risk Analyst** (project risk), **Senior Program Manager** (scope/stakeholder strategy), **Claude Expert** (Claude/Anthropic technical + OS improvements)
  - Presents a menu; routes your question to the chosen expert
  - Reuses the pattern: skill wraps expert agent invocation

**Automation & Monitoring:**
- **Claude Expert OS Review:** Runs automatically after every session closes to monitor interactions and surface OS-improvement opportunities. Results logged to `projects/claude_expert/os-review-log.md`. (Fallback: can be switched to weekly cloud routine if per-session cadence proves noisy.)

**Additional Resources:**
- **Level 3 Portfolio Helper:** `helpers/portfolio-builder.md` — Detection engine and dimension mapping logic
