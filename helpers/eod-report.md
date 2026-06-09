# Helper: End-of-Day Project Status Report

**Owner:** Nelson Araya
**Created:** 2026-06-07
**Status:** v1 (Slack only — client email layer pending email examples)

---

## Purpose

Takes raw daily notes and produces polished end-of-day project status
reports in **two or three formats**:

1. **STANDARD** — internal Slack format (boss-approved)
2. **CLIENT EMAIL** — same content, transformed for client audience
   (formal tone, no internal trajectory tags, more explanatory)
3. **OPTIMIZED** — Standard + three additive enhancements (pending boss
   approval)

The multi-format design serves three goals:
- **Daily:** generate Slack + client email from the same notes (30 min
  faster than writing separately)
- **One-time pitch:** use Standard + Optimized side-by-side when
  proposing trajectory tags / slippage markers to your boss
- **Consistency:** same content, different packaging for different
  audiences

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
> `projects/<your-project>/eod-report.context.md`. Generate the STANDARD
> (Slack) and CLIENT EMAIL versions. My raw notes for today:
>
> [paste notes — bullets, copy-pastes from Slack/Jira, paragraphs,
> stream-of-consciousness, all fine; no need to clean up first]

**Optional:** To get **accurate slippage markers** (if proposing OPTIMIZED
format to your boss later), also paste yesterday's report below today's
notes. Without prior-day context, the helper will skip slip markers rather
than guess.

**Optional:** To also see the OPTIMIZED version (Standard + trajectory tags
+ slippage markers), add: "Also generate OPTIMIZED for comparison."

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
- **Emojis in STANDARD format:** Use headline emoji (📊 for title, 🔧/✅ for workstreams, 📋 for actions), progress emoji (📈), and status emoji (⚠️ for OFF TRACK / AT RISK). These improve visual scannability on mobile Slack.

---

## OUTPUT FORMAT 1 — STANDARD (boss-approved, default until further notice)

```
# 📊 [PROJECT_NAME] PROJECT STATUS UPDATE
**Mon XX, YYYY**

---

## EXECUTIVE SUMMARY

[Workstream 1 name], [2-4 sentence narrative covering what shipped,
what's in flight, key issues, forward commitments]

[Workstream 2 name], [2-4 sentence narrative, same shape]

---

## 🔧 [WORKSTREAM 1 NAME] — ⚠️ [ON TRACK / AT RISK / OFF TRACK]

**Objective:** [stable text from context]

**Progress:** 📈 [X]% complete ([A] of [B] tasks)

**DELIVERED TODAY:**
- [bullet]
- [bullet]

**BLOCKERS:**
- [bullet OR "NTR"]

---

## ✅ [WORKSTREAM 2 NAME] — ⚠️ [STATUS]

**Objective:** [stable text from context]

**Progress:** 📈 [X]% complete ([A] of [B] tasks)

**DELIVERED TODAY:**
- [bullet OR "NTR"]

**BLOCKERS:**
- [bullet OR "NTR"]

---

## 📋 ACTIONS REQUIRED:

- **[date]:** [action]
- **[date]:** [action]
```

---

## OUTPUT FORMAT 2 — CLIENT EMAIL (v2 — uses STANDARD content, transforms for client audience)

Use the STANDARD format content. Transform it using these rules:

### Structure (match the sample email layout exactly)

```
Subject: [PROJECT_NAME] Project Status Update | [Date]

To: [Client stakeholders — use full names and email addresses from context]
Cc: [GAP team members per project context]
From: [Your name and title — may be sent by delivery manager on behalf of team]

---

[BODY — plain text or HTML]

[PROJECT_NAME] PROJECT STATUS UPDATE
[Date in format: Month DD, YYYY]

Executive Summary

[Workstream 1 name]: [2-3 sentence narrative — what shipped, current state, forward commitment. More explanatory than Slack version; include business impact where relevant]

[Workstream 2 name]: [2-3 sentence narrative — same shape]


[WORKSTREAM 1 NAME] – [ON TRACK / AT RISK / OFF TRACK]

Objective: [stable text from context]

Progress: [X]% complete ([A] of [B] tasks)

Delivered Today:
- [bullet]
- [bullet]

Blocker:
- [bullet OR "None to report"]


[WORKSTREAM 2 NAME] – [STATUS]

Objective: [stable text from context]

Progress: [X]% complete ([A] of [B] tasks)

Delivered Today:
- [bullet OR "None to report"]

Blockers: [bullet OR "None to report"]


ACTIONS REQUIRED

[Date]: [action]
[Date]: [action]

Best Regards,

[Your name]
[Your title]
Growth Acceleration Partners (GAP)
Email: [Your email]
Website: WeAreGAP.com
Phone: [Your phone]
```

### Transformation rules (STANDARD → CLIENT EMAIL)

**What stays the same:**
- Workstream names, objectives, progress %, delivered items, blockers, action dates
- Overall structure and logical flow

**What changes:**
1. **Executive Summary:** Expand from 2-4 sentences to more explanatory 3-4 sentence narrative. Include context on *why* deliverables matter (e.g., "CI/CD pipeline improves deployment speed and reliability"). Avoid internal jargon; assume client audience may not know GAP-specific tools or acronyms.
2. **Delivered items:** Add brief context if needed (e.g., "New Project Smoke Testing completed" → "New Project Smoke Testing completed (validates end-to-end functionality)"). Keep bullets concise.
3. **Tone:** Professional, formal closing. First names only acceptable but use full names in email header. No emojis, no Slack shorthand.
4. **Acronyms:** Keep only well-known ones (HIPAA, CI/CD). Define others on first mention (e.g., "Azure Functions (serverless compute)").
5. **Dates:** Format as "Mon DD" in headers but preserve exact dates in ACTIONS REQUIRED (e.g., "Jun 05").

**What to remove:**
- No trajectory tags (RECOVERING / HOLDING / SLIPPING) — client doesn't need to see internal trajectory framing
- No slippage markers from prior dates — present cleanly without historical context
- No forward-looking speculation ("we might..."); use commitments only

### When to use this format

- Weekly or daily reports sent to client stakeholders (Shawn F, Ken, etc.)
- Canonical source is always the STANDARD Slack version
- Client email is a *translation*, not new information
- Send same day or next morning; timestamp matches when Slack was generated

---

## OUTPUT FORMAT 3 — OPTIMIZED (pending boss approval)

Three additive enhancements vs Standard (when approved). Everything else identical.

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
   stakeholder roles, acronym glossary, client names. If not specified or missing,
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

4. **Produce STANDARD format first** (internal Slack version).

5. **Produce CLIENT EMAIL format second** by transforming the Standard
   content using the rules in OUTPUT FORMAT 2 (more narrative, formal
   closing, client-friendly tone, remove trajectory tags).

6. **Produce OPTIMIZED format third** (if requested) with the three
   enhancements applied to Standard. If yesterday's report is not in
   context, skip slippage markers and note that explicitly.

7. **Present all requested formats**, clearly labeled. Default: STANDARD
   + CLIENT EMAIL. OPTIMIZED on request.

8. **Flag clarifying questions** for missing progress numbers, ambiguous
   ownership, unclear status, missing client stakeholder list. Don't invent
   data — ask.

---

## What this helper does NOT do (yet)

- Pull from Slack / Jira / email automatically (notes still manual)
- Send messages or emails for you (you review and send manually)
- Detect slippage without context (paste yesterday's report alongside
  today's notes if you want slip markers)

---

## Changelog

- **2026-06-08** — v2 released. Added CLIENT EMAIL format. Now generates
  STANDARD (Slack) + CLIENT EMAIL by default. OPTIMIZED available on
  request. Uses sample Gerardo Mora email (Jun 5) as structure reference.
- **2026-06-07** — v1 created. Slack only. Standard + optimized
  formats. Client email derivative pending.
