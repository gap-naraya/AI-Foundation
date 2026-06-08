# Helper: End-of-Day Project Status Report

**Owner:** Nelson Araya
**Created:** 2026-06-07
**Status:** v1 (Slack only — client email layer pending email examples)

---

## Purpose

Takes raw daily notes and produces a polished end-of-day project status
report in **two formats side by side**:

1. **STANDARD** — the current boss-approved format
2. **OPTIMIZED** — same content with three additive enhancements
   (pending boss approval)

The two-output design serves two goals:
- Daily: see both, pick which to send
- One-time: use the side-by-side as a pitch artifact when proposing the
  optimizations to a boss

This file is a **generic template**. Project-specific details (project
codename, client, stakeholder cast, acronyms, workstream objectives)
live in a separate context file alongside each project (e.g.,
`projects/<project-name>/eod-report.context.md`).

---

## How to use

In a Claude conversation, paste this prompt and **tell Claude which
project context file to load**:

> Run my EoD report helper. Use the format definitions and voice rules
> in `helpers/eod-report.md`, and project context from
> `projects/<your-project>/eod-report.context.md`. Generate BOTH the
> standard and optimized versions side by side. My raw notes for today:
>
> [paste notes — bullets, copy-pastes from Slack/Jira, paragraphs,
> stream-of-consciousness, all fine; no need to clean up first]

To get **accurate slippage markers** in the optimized version, also paste
yesterday's report below today's notes. Without prior-day context, the
helper will skip slip markers rather than guess.

---

## Voice rules (universal)

- **Tone:** internal, direct, professional but not stiff
- **First names without titles** when referring to teammates
- **Acronyms used freely** — Slack audience already knows them
- Every Executive Summary includes at least one **forward-looking
  statement** ("We will...", "[Owner] will work with...")
- **Causal framing** — don't just list what happened; say *why* it
  matters or what it unblocks
- Use the actual status from the data; **do not soften** OFF TRACK to
  "in progress" or similar
- Do not invent new sections or add commentary outside the defined
  format

---

## OUTPUT FORMAT 1 — STANDARD (boss-approved, default until further notice)

```
[PROJECT_NAME] PROJECT STATUS UPDATE
[date in format: Mon XX, YYYY]

EXECUTIVE SUMMARY

[Workstream 1 name], [2-4 sentence narrative covering what shipped,
what's in flight, key issues, forward commitments]

[Workstream 2 name], [2-4 sentence narrative, same shape]


[WORKSTREAM 1 NAME] - [ON TRACK / AT RISK / OFF TRACK]

Objective: [stable text from context]

Progress: [X]% complete ([A] of [B] tasks)

DELIVERED TODAY:
- [bullet]
- [bullet]

BLOCKERS:
- [bullet OR "NTR"]


[WORKSTREAM 2 NAME] - [STATUS]

Objective: [stable text from context]

Progress: [X]% complete ([A] of [B] tasks)

DELIVERED:
- [bullet OR "NTR"]

BLOCKER
- [bullet OR "NTR"]


ACTIONS REQUIRED:
- [date]: [action]
- [date]: [action]
```

---

## OUTPUT FORMAT 2 — OPTIMIZED (pending boss approval)

Three additive enhancements vs Standard. Everything else identical.

### Enhancement 1: One-sentence headline at the top

Right after the date, **before** the EXECUTIVE SUMMARY, add a single
sentence distilling the entire day for a leader skimming on mobile.

Example shape:
```
[PROJECT_NAME] PROJECT STATUS UPDATE
[date]

HEADLINE: [Major delivery this cycle]; [biggest movement on
timeline/status]; [most important commitment forward].

EXECUTIVE SUMMARY
...
```

Rules:
- One sentence, ideally under 30 words
- Lead with the most consequential fact of the day
- Include forward-looking shift if a date slipped
- Semicolons to chain 2-3 clauses if needed

### Enhancement 2: Trajectory indicator on workstream status

Change status labels from `[WORKSTREAM] - OFF TRACK` to
`[WORKSTREAM] - OFF TRACK | RECOVERING` (or HOLDING / SLIPPING).

Decision criteria:
- **RECOVERING:** progress % increasing toward objective, blockers
  shrinking, deadline shifts contained
- **HOLDING:** no material change since last report
- **SLIPPING:** progress stalled or regressing, blockers compounding,
  dates pushed further

When ON TRACK, no trajectory tag needed.

### Enhancement 3: Slippage markers on Actions Required

When an action's date moves later than a previous report's date for the
same action, mark the slip explicitly:

```
Before:  Jun 09: Final agreement on policy baseline
After:   Jun 09 (slipped from Jun 04): Final agreement on policy baseline
```

Rules:
- Apply only with clear evidence the action was previously committed to
  an earlier date (yesterday's report alongside today's notes)
- If unsure, **omit** the slip marker rather than guess
- Surface in the action line itself, not a separate section

---

## Working sequence (how the helper produces output)

When invoked, do this in order:

1. **Read the project context file** the user specified (e.g.,
   `projects/<project>/eod-report.context.md`) for project-specific
   details: project codename, workstream names + objectives,
   stakeholder roles, acronym glossary. If not specified or missing,
   use generic placeholders and flag it.

2. **Parse raw notes** into:
   - "Delivered today" items per workstream
   - "Blockers" per workstream
   - "Actions required" items with dates and owners
   - Progress signals (% completion, ratios, deadline movement)

3. **Draft Executive Summary narratives** (judgment-heavy):
   - 2-4 sentences per workstream
   - Use causal framing
   - Include at least one forward-looking statement

4. **Produce STANDARD format first.**

5. **Produce OPTIMIZED format second** with the three enhancements
   applied. If yesterday's report is not in context, skip slippage
   markers and note that explicitly.

6. **Present both side by side**, each clearly labeled.

7. **Flag clarifying questions** for missing progress numbers, ambiguous
   ownership, unclear status. Don't invent data — ask.

---

## What this helper does NOT do (yet)

- Pull from Slack / Jira / email automatically (notes still manual)
- Generate the client email version (v2)
- Send messages for you (you review and send manually)
- Detect slippage without context (paste yesterday's report alongside
  today's notes if you want slip markers)

---

## Changelog

- **2026-06-07** — v1 created. Slack only. Standard + optimized
  formats. Client email derivative pending.
