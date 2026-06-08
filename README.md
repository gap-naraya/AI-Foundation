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
│   └── eod-report.md
└── projects/                         Project-specific work and context
    ├── mediquant/
    │   └── eod-report.context.md
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
| `eod-report.md` | End-of-day project status report (Slack now; client email later) | v1 live (Slack only); v2 client email pending |

### `projects/` — Project-specific work and context

| Project | Contents | Notes |
|---|---|---|
| `mediquant/` | `eod-report.context.md` | Active client engagement (project codename DOM). Stakeholders, acronyms, workstream objectives. |
| `ai_impact_evaluation/` | `AI Impact Evaluation for MANAGERS.pdf` | Level 3 AI certification rubric. Evidence portfolio rebuild pending. |

---

## How to use helpers

From any Claude Code conversation inside this directory, invoke a helper by referencing its files. Example for the End-of-Day report helper:

> Run my EoD report helper. Use format and voice rules from `helpers/eod-report.md` and project context from `projects/mediquant/eod-report.context.md`. Generate BOTH the standard and optimized versions side by side. My raw notes for today: [paste notes]. Yesterday's report for slippage detection: [paste yesterday's Slack].

Each helper file documents its own invocation pattern.

---

## Memory (lives outside this repo)

Claude's persistent memory across conversations lives at:

```
~/.claude/projects/-Users-naraya-Documents-AI-Foundation/memory/
```

This stays on Nelson's machine and is **not part of this repo** (does not get pushed to GitHub). The `MEMORY.md` index there links to individual memory files: Nelson's profile, core values, 2026 goals, stakeholders, communication preferences, business context, and references to helpers built so far.

---

## Status snapshot (as of 2026-06-07)

**Done**
- Personal context layer (the `context/` folder)
- First helper (`eod-report.md`) — v1 live
- First project context (`projects/mediquant/eod-report.context.md`)
- Memory system primed with user profile, goals, stakeholders, and helper reference

**In progress**
- EoD helper v2 (client email derivative) — pending email examples
- Level 3 AI certification evidence — rubric in place; portfolio rebuild pending

**Upcoming (2026 goals)**
- Mediquant project success — 3-month target
- Level 3 AI certification — October target
