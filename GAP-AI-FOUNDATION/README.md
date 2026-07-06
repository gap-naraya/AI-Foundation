# GAP-AI-FOUNDATION — Mediquant DOM Project

This repository contains automation, tools, and documentation for Nelson Araya's work as Senior Project Manager at Growth Acceleration Partners (GAP), leading the critical **Mediquant DOM** (automation) project.

---

## 📋 Project Overview

**Mediquant DOM** is a complex infrastructure and compliance automation initiative currently in execution. This project requires careful stakeholder communication, rapid decision-making, and transparent progress tracking under high visibility.

### Key Stakeholders

| Role | Name | Organization |
|---|---|---|
| Project Manager | Nelson Araya | GAP |
| Architecture Lead | Sean | GAP (internal) |
| Client Executive (Approval) | Shawn Fergason | Mediquant |
| Client Executive | Ken Manley | Mediquant |
| DevOps/CI-CD Lead | Jeff | EA Team (partner) |

---

## 🗂️ Directory Structure

```
GAP-AI-FOUNDATION/
├── README.md                          # This file
├── CLAUDE.md                          # Project-specific Claude instructions
├── context/                           # Contextual documentation
│   ├── 2026_Goals_Context.md         # 2026 strategic goals
│   ├── Career_Context_Document.md    # Career trajectory and context
│   ├── Communication_Context.md      # Communication style and preferences
│   ├── Business_Context.md           # Business operating principles
│   └── Personal_Constitution.md      # Core values and operational principles
├── helpers/                           # Reusable helper templates
│   ├── eod-report.md                 # EoD report generation helper (generic template)
│   └── eod-report-quick-invoke.md    # Quick reference for running EoD reports
├── projects/                          # Project-specific files
│   └── mediquant/                    # Mediquant DOM project
│       ├── eod-report.context.md     # Project context (workstreams, acronyms, stakeholders)
│       ├── eod-report.previous.md    # Previous report snapshot (for slippage detection)
│       └── client-email-template.html # HTML email template for client communications
└── .claude/skills/                   # Claude Code skills (automation)
    ├── eod-report/                   # Daily status report generation skill
    ├── escalate-gerardo/             # Manager escalation skill
    ├── draft-message/                # Professional message drafting skill
    └── portfolio/                    # AI impact evaluation portfolio skill (6 modes)
```

---

## 🚀 Available Skills

This project includes four Claude Code skills that automate common workflows:

### 1. `/eod-report` — Daily Status Report Generation
Generates both internal (Slack) and client-facing (HTML email) status reports automatically.

**Quick Start:**
```
/eod-report
```

Then paste today's raw notes when prompted.

**Outputs:**
- **STANDARD** — Slack internal format (emojis, progress %, status labels)
- **CLIENT EMAIL** — Formal HTML email for Shawn Fergason and Ken Manley

**What it does:**
- Reads project context, previous snapshot, and email template
- Detects slippage by comparing to yesterday's metrics
- Generates both formats from the same notes
- Creates Slack DM and Gmail draft after approval
- Updates snapshot file for tomorrow's comparison

📖 Full documentation: `helpers/eod-report.md`

### 2. `/escalate-gerardo` — Manager Escalation
Escalate blockers, decisions, or concerns to your manager Gerardo.

**Triggers:** "stuck", "Rule of 45", "escalate to Gerardo", blocked 45+ minutes

### 3. `/draft-message` — Professional Communication
Draft Slack messages, emails, or sensitive communications to specific people.

**Triggers:** "draft a message to", "write an email to", "how do I tell [name]"

### 4. `/portfolio` — AI Impact Evaluation Portfolio (6 Modes)
Unified skill for tracking, auditing, and preparing evidence for the GAP AI Impact Evaluation (October re-evaluation).

**Six Modes:**
- **scan** — Auto-detect evidence from git commits and file changes
- **approve** — Review and commit staged findings to evidence log (archive-safe)
- **audit** — Review all 5 dimensions; identify gaps and action items
- **draft [N]** — Write evaluation form answer for a specific dimension
- **map** — Analyze if a task qualifies as evidence
- **update** — Log manual evidence (time metrics, peer feedback)

**Daily Routine:** Cloud agent runs **5pm Costa Rica time** daily, detects new evidence, reports findings. You review and approve locally with `/portfolio approve`.
- View routine results: https://claude.ai/code/routines
- Next run: Tomorrow at 5pm Costa Rica time

**Triggers:** "portfolio", "scan portfolio", "portfolio audit", "portfolio draft", "portfolio map", "portfolio update", "Level 3", "AI assessment", "evidence", "merit increase"

📖 Full documentation: `helpers/portfolio-builder.md`

---

## 📊 EoD Report Workflow

The **End-of-Day Report** is the core daily communication tool for this project. Here's how it works:

### Flow

1. **Generate** → Run `/eod-report` and paste today's raw notes
2. **Review** → Check STANDARD (Slack) and CLIENT EMAIL (HTML) formats
3. **Approve** → Confirm ready to send
4. **Execute** → Reports sent automatically:
   - Slack DM to you
   - Gmail draft for client email (To: Shawn, Ken; Cc: Milagro, Matt, Steven)
   - Snapshot file updated for tomorrow

### Key Rules

- **Report Date:** Always dated for **tomorrow** (schedules to send early next morning)
- **Format:** Two outputs from one set of notes (30 min faster than writing separately)
- **Slippage Detection:** Compares to previous snapshot; flags date slips and status changes
- **Voice:** Direct, professional, causal framing (explain *why* things matter)
- **Status:** Use actual data; don't soften OFF TRACK to "in progress"

### Example: Running Today's Report

```bash
# In Claude Code, run the skill
/eod-report

# Paste your raw notes covering:
# - What Core Team Execution delivered
# - What Compliance & Architecture delivered
# - Blockers per workstream
# - Progress updates and key action dates

# Approve when ready
# Review: Slack message + Gmail draft are created
# Update: Snapshot file is updated for tomorrow
```

📖 Detailed guide: `helpers/eod-report.md`  
⚡ Quick reference: `helpers/eod-report-quick-invoke.md`

---

## 📁 Context Files

Each context file provides essential background for decision-making and communication:

### `context/2026_Goals_Context.md`
Strategic goals for 2026: Mediquant project success (3-month horizon) and Level 3 certification (October). 6-hour weekly commitment structure.

### `context/Career_Context_Document.md`
Career trajectory, core strengths, current challenges, and the 2-year vision to remain a productive, joyful pillar of support.

### `context/Communication_Context.md`
Communication preferences by stakeholder:
- **Clients (Shawn, Ken):** Formal, data-driven, executive summaries
- **Internal team (Sean, Jeff):** Casual, direct, action-focused
- **Manager (Gerardo):** Transparent, decision-ready, blocked items first

### `context/Business_Context.md`
Operating principles, decision-making frameworks, tools used, and current project status.

### `context/Personal_Constitution.md`
Core values (empathy, loyalty, presence, teamwork) and operational principles (The Pause, Courageous Proactivity, The Black List).

---

## 🎯 Workstreams (Mediquant DOM)

The project is organized into two primary workstreams:

### Workstream 1: Core Team Execution
**Objective:** Fully functional, testable environment (HiTrust/HIPAA-compliant) by June 5  
**Status:** AT RISK (87% complete, 21 of 24 tasks)

**Focus:**
- Infrastructure provisioning (Databricks, Security Groups, privileged accounts)
- Smoke testing and defect remediation
- Portal security training completion

**Current Blocker:** Databricks workspace login configuration (escalated to MQ IT)

### Workstream 2: Compliance & Architecture Review
**Objective:** EastinIT Architecture Design assessment delivered by June 5  
**Status:** ON TRACK (100% complete, 7 of 7 tasks)

**Focus:**
- HIPAA compliance framework and definitions
- Formal compliance remediation plan
- User story creation for remediation work
- Architecture assessment and design

**Current Blocker:** Subscription-per-environment architecture approval pending

---

## 📧 Email Communication

All client emails use the HTML template at `projects/mediquant/client-email-template.html`. The template provides:

- Professional color scheme and typography
- Color-coded status sections (green for delivered, red for issues, blue accents)
- Progress indicators with percentages and task counts
- Responsive layout for mobile and desktop

**Recipients:**
- **To:** Shawn Fergason (sfergason@mediquant.com), Ken Manley (kenm@mediquant.com)
- **Cc:** Milagro Prado, Matt Veitch, Steven Yelton (GAP team)

---

## 🔑 Acronyms & Glossary

| Acronym | Definition |
|---|---|
| **DOM** | Project codename for Mediquant automation |
| **MQ** | Mediquant (the client) |
| **GAP** | Growth Acceleration Partners (Nelson's employer) |
| **EA** | EA team (CI/CD infrastructure partner) |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **HiTrust** | Health Information Trust Alliance (compliance certification) |
| **CI/CD** | Continuous Integration / Continuous Deployment |
| **NTR** | Nothing To Report |

---

## 📝 Important Files

### Required for EoD Reports
- `projects/mediquant/eod-report.context.md` — Project context (workstreams, stakeholders, acronyms)
- `projects/mediquant/eod-report.previous.md` — Yesterday's snapshot (for slippage detection)
- `projects/mediquant/client-email-template.html` — HTML email template

### Templates & Helpers
- `helpers/eod-report.md` — Complete EoD report generation guide with format specs, voice rules, and working sequence
- `helpers/eod-report-quick-invoke.md` — Quick reference for running EoD reports
- `CLAUDE.md` — Project-specific instructions (loads after root CLAUDE.md)

---

## 💡 Quick Start

### Generate Today's EoD Report

1. **Run the skill:**
   ```
   /eod-report
   ```

2. **Paste your raw notes** covering deliverables, blockers, and progress

3. **Review** the STANDARD (Slack) and CLIENT EMAIL (HTML) outputs

4. **Approve** when satisfied

5. **Done!** Reports are automatically:
   - Sent to you via Slack DM
   - Created as Gmail draft for client
   - Snapshot updated for tomorrow

### Draft a Message to a Stakeholder

```
/draft-message

How do I tell Shawn about the Databricks delay?
```

### Escalate a Blocker to Gerardo

```
/escalate-gerardo

We've been blocked on Databricks workspace access for 3 days. Need guidance on next steps.
```

---

## 📚 Related Resources

- **Root CLAUDE.md** — Shared operating system (hard rules, core values, Nelson's profile)
- **Auto Memory** — Persistent context across conversations (`~/.claude/projects/-Users-naraya-Documents-AI-Foundation/memory/`)
- **Dual OS Architecture** — GAP-AI-FOUNDATION + CENFOTEC-AI-FOUNDATION (shared root, separate domains)

---

## 🔗 Integration with Root Project

This folder is part of a **dual OS architecture**:

- **GAP-AI-FOUNDATION** (this folder) — Mediquant project, client communication, status reporting
- **CENFOTEC-AI-FOUNDATION** — Educational/training initiatives (separate skills and context)
- **Shared Root CLAUDE.md** — Hard rules, Nelson's identity, common operating principles

Both projects share the foundational rules and values defined in `/Users/naraya/Documents/AI-Foundation/CLAUDE.md`.

---

## 🆘 Need Help?

- **EoD Report issues?** → Read `helpers/eod-report.md` (full spec) or `helpers/eod-report-quick-invoke.md` (quick reference)
- **Communication guidance?** → See `context/Communication_Context.md`
- **Project blockers?** → Use `/escalate-gerardo` skill
- **Client questions?** → Refer to `projects/mediquant/eod-report.context.md` for stakeholder details

---

**Last Updated:** July 5, 2026  
**Portfolio System Status:** ✅ Live — Daily automated scans running, 7 evidence items approved  
**Maintained By:** Nelson Araya Alvarado  
**Organization:** Growth Acceleration Partners (GAP)
