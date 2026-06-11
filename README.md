# AI-Foundation

Nelson Araya's personal **Claude OS** — a collection of files, helpers, and project context that teach Claude how to work with Nelson across work, learning, and personal projects.

---

## Repo map

```
AI-Foundation/
├── CLAUDE.md                         Global Claude Code instructions
├── README.md                         This file (table of contents)
├── context/                          Who Nelson is
│   ├── Personal_Constitution.md
│   ├── 2026_Goals_Context.md
│   ├── Career_Context_Document.md
│   ├── Communication_Context.md
│   └── Business_Context.md
├── helpers/                          Reusable tools (built once, used daily)
│   ├── eod-report.md
│   └── eod-report-quick-invoke.md
├── .claude/                          Claude Code configuration
│   ├── settings.local.json
│   └── skills/                       Auto-triggering skills
│       ├── eod-report/SKILL.md
│       ├── escalate-gerardo/SKILL.md
│       ├── draft-message/SKILL.md
│       └── level3-portfolio/SKILL.md
└── projects/                         Project-specific work and context
    ├── mediquant/
    │   ├── eod-report.context.md
    │   ├── eod-report.previous.md
    │   └── client-email-template.html
    └── ai_impact_evaluation/
        └── AI Impact Evaluation for MANAGERS.pdf
```

---

## What's where

### `CLAUDE.md` — Global instructions

Hard rules Claude follows in every conversation (no assumptions about technical background, data-driven decisions, always ask clarifying questions). Pointers to personal context files. Brief description of current operating context.

### `context/` — Who Nelson is

Five personal context files Claude loads to tailor its work to Nelson specifically.

| File | What it captures |
|---|---|
| `Personal_Constitution.md` | Core values and operating principles |
| `2026_Goals_Context.md` | Strategic goals for the year |
| `Career_Context_Document.md` | Professional background and trajectory |
| `Communication_Context.md` | Tone preferences by audience (formal vs casual) |
| `Business_Context.md` | Work environment and decision-making style |

### `helpers/` — Reusable tools

Each helper is a markdown file containing format definitions, voice rules, and a "how to invoke" prompt. Built once, used repeatedly.

| Helper | Purpose | Status |
|---|---|---|
| `eod-report.md` | End-of-day project status report — STANDARD (Slack) + CLIENT EMAIL (HTML) | v2 live |
| `eod-report-quick-invoke.md` | Shortest possible invocation cheat sheet | Live |

### `.claude/skills/` — Auto-triggering skills

Skills load automatically when Claude detects a matching intent. No file references needed — just use the trigger phrase.

| Skill | Trigger phrase(s) | What it does |
|---|---|---|
| `eod-report` | "eod", "end of day", "daily report", "status update" | Generates STANDARD + CLIENT EMAIL for Mediquant DOM. Dates for tomorrow automatically, sends to Slack + Gmail draft. |
| `escalate-gerardo` | "escalate", "stuck", "blocked", "message to Gerardo" | Fills in one of 3 pre-approved escalation scripts (Unblock / Priority Check / Mentorship) and sends to Gerardo. |
| `draft-message` | "draft a message to [name]", "write email to", "how do I tell [name]" | Drafts any work communication with auto-selected tone, language, and depth per audience matrix. |
| `level3-portfolio` | "Level 3", "AI assessment", "certification", "portfolio", "evidence" | Audits Level 3 evidence, drafts GAP self-evaluation answers, maps daily work to the 5 rubric dimensions. |

### `projects/` — Project-specific work and context

| Project | Contents | Notes |
|---|---|---|
| `mediquant/` | `eod-report.context.md`, `eod-report.previous.md`, `client-email-template.html` | Active client engagement (project codename DOM). Stakeholders, acronyms, workstream objectives, daily snapshot for slippage detection. |
| `ai_impact_evaluation/` | `AI Impact Evaluation for MANAGERS.pdf` | Level 3 AI certification rubric. Evidence portfolio in progress via `level3-portfolio` skill. |

---

## How to use skills

Skills auto-trigger — just use a natural phrase. No file references needed.

```
eod                               → runs the EoD report helper
escalate to Gerardo               → fills in the right escalation script
draft a message to Shawn about X  → drafts a formal client message
Level 3 evidence audit            → maps your work to the rubric
```

## How to use helpers (manual invocation)

Helpers can still be invoked manually by referencing their files. Example:

> Run my EoD report helper. Use format and voice rules from `helpers/eod-report.md` and project context from `projects/mediquant/eod-report.context.md`. Raw notes: [paste notes].

Each helper file documents its own invocation pattern.

---

## Memory (lives outside this repo)

Claude's persistent memory across conversations lives at:

```
~/.claude/projects/-Users-naraya-Documents-AI-Foundation/memory/
```

This stays on Nelson's machine and is **not part of this repo** (does not get pushed to GitHub). The `MEMORY.md` index there links to individual memory files: Nelson's profile, core values, 2026 goals, stakeholders, communication preferences, business context, and references to helpers built so far.

---

## Status snapshot (as of 2026-06-11)

**Done**
- Personal context layer (`context/` folder)
- EoD report helper — v2 live (STANDARD + CLIENT EMAIL, HTML template, slippage detection)
- Mediquant project context + previous snapshot system
- Memory system primed with profile, goals, stakeholders, communication preferences, and helper references
- 4 Claude Code skills: `eod-report`, `escalate-gerardo`, `draft-message`, `level3-portfolio`

**In progress**
- Level 3 AI certification evidence — rubric extracted, portfolio tracking via `level3-portfolio` skill

**Upcoming (2026 goals)**
- Mediquant DOM project success — 3-month target
- Level 3 AI certification — October target (re-evaluation windows: July, October)
