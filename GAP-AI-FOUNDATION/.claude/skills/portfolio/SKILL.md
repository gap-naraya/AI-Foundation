---
name: portfolio
description: Use this skill for ALL Level 3 portfolio work. Triggers on "portfolio", "scan portfolio", "portfolio scan", "portfolio audit", "portfolio approve", "portfolio draft", "portfolio map", "portfolio update", "Level 3", "AI assessment", "evidence", "merit increase", "Transformer certification". Six modes: scan (auto-detect evidence), approve (promote to log), audit (review all 5 dimensions), draft (write evaluation answers), map (does X count?), update (log manual evidence).
---

# Portfolio Skill — Level 3 Transformer Certification

Nelson uses this unified skill for ALL Level 3 evidence portfolio work. Six modes in one place: scan, approve, audit, draft, map, and update.

**Target:** October 2026 re-evaluation for Level 3 AI Value Leader certification + merit increase.

---

## Six Modes (Pick What You Need)

### Mode 1: `/portfolio scan` — Automated Evidence Detection

Automatically scans your recent work for Level 3 evidence.

**What it does:**
1. Reads last scan date from `evidence-scan.snapshot.md`
2. Runs `git log` for commits since last scan
3. Finds recently modified project files
4. Filters for GAP-only scope (excludes Cenfotec)
5. Cross-checks against `evidence-log.md` for duplicates
6. Stages new findings in `evidence-staging.md`

**When to use:**
- After completing significant work (new skill, helper, automation)
- Daily automated (via `/schedule portfolio scan`)
- Anytime to capture pending evidence

**Output:** ✅ N items staged in `evidence-staging.md`. Next: run `/portfolio approve`.

---

### Mode 2: `/portfolio approve` — Promote Staged Findings

Moves approved items from staging into your official evidence log.

**What it does:**
1. Reads all 🟡 STAGED items from `evidence-staging.md`
2. For each item: asks "Approve? (y/n/edit):"
   - **y** → item will be added to evidence-log.md
   - **n** → item is discarded
   - **edit** → provide replacement text, then add
3. **Before any write:** archives current `evidence-log.md` → `archive/evidence-log-YYYY-MM-DD.md` (timestamped backup)
4. Appends approved items with ✅ APPROVED [DATE] status
5. Clears staging file

**When to use:**
- After running `/portfolio scan` and reviewing findings
- Anytime you want to commit staged evidence

**Safety:** Automatic archive backup before every write to `evidence-log.md`.

---

### Mode 3: `/portfolio audit` — Review All Dimensions

Get a comprehensive view of your portfolio across all 5 evaluation dimensions.

**What it does:**
1. Loads your current `evidence-log.md`
2. Reviews all 5 dimensions: what's documented, what's missing, what's weak
3. Produces a gap list with actionable next steps
4. Flags dimensions that are stale or need attention

**When to use:**
- Monthly checkpoint (see if you're on track for October)
- Mid-July progress check (per Level 3 timeline)
- Before calling Gerardo (understand your position first)

**Output:** Dimension-by-dimension breakdown + punch list of gaps.

---

### Mode 4: `/portfolio draft [dimension number]` — Write Evaluation Form Answers

Writes a compelling, evidence-based answer for a specific dimension (for the October evaluation form).

**Example:** `/portfolio draft 1` → writes an answer for Dimension 1.

**What it does:**
1. Loads `evidence-log.md` and focuses on your dimension [N] evidence
2. Writes a narrative paragraph for the evaluation form
3. Cites specific artifacts from your log (files, dates, impact)
4. Uses professional tone; no exaggeration; grounded in real evidence

**When to use:**
- August / early September (after evidence capture is mostly done)
- To practice your evaluation form responses
- To wordsmith your self-evaluation before October submission

**Output:** Ready-to-copy paragraph for the October evaluation form.

---

### Mode 5: `/portfolio map [task description]` — Does This Count as Evidence?

Analyzes whether a specific work item qualifies as Level 3 evidence.

**Example:** `/portfolio map: "I created a new Claude OS blueprint for Cenfotec training"` → tells you which dimensions it supports (if any in GAP scope).

**What it does:**
1. Analyzes your task description against the 5 evaluation dimensions
2. Identifies which dimension(s) it supports
3. Explains WHY it qualifies (or doesn't)
4. Recommends how to document it

**When to use:**
- When you complete something and want to know if it's portfolio-worthy
- To understand what counts as evidence BEFORE doing the work
- To avoid logging non-evidence items

**Output:** Dimension mapping + documentation guidance.

---

### Mode 6: `/portfolio update [manual evidence item]` — Log Evidence AI Cannot Auto-Detect

For items that git commits and file changes cannot capture (time metrics, peer feedback, adoption events).

**Examples:**
- "Time saved: EoD report took 12 min vs. 30 min before (saved 18 min today)"
- "Peer adoption: Gerardo asked to use the Claude OS system today"
- "Decision cycle: Escalation to Ken took 4 hours vs. 2 days before"

**What it does:**
1. Takes your hand-written note on manual evidence
2. Formats it as a proper evidence item (with dimension, metric, date)
3. **Before appending:** archives current `evidence-log.md` → `archive/evidence-log-YYYY-MM-DD.md`
4. Appends to the correct dimension in `evidence-log.md`

**When to use:**
- After tracking time on a workflow (Dimension 3)
- When someone gives you feedback on adopting your system (Dimension 5)
- When you observe measurable improvement (decision speed, communication efficiency)

**Output:** Item appended to `evidence-log.md` with ✅ APPROVED [DATE] status.

---

## Quick Reference: Which Mode to Use?

| What you want to do | Use this mode |
|---|---|
| Automatically find new evidence from my work | `/portfolio scan` |
| Review & commit staged evidence to the log | `/portfolio approve` |
| See what's documented vs. missing | `/portfolio audit` |
| Write my October evaluation form answer | `/portfolio draft [dimension]` |
| Find out if [task X] counts as evidence | `/portfolio map` |
| Log time saved, peer feedback, metrics | `/portfolio update` |

---

## Workflow Examples

### Example 1: Daily Automated Capture
```
1. Work on Mediquant automation all day
2. Schedule runs `/portfolio scan` at 6 PM
3. Next morning: review evidence-staging.md
4. Run `/portfolio approve` to commit to log
```

### Example 2: Monthly Audit
```
1. `/portfolio audit` to see full picture
2. See gaps in Dimension 3 (measurable impact)
3. `/portfolio update` with time-tracking notes from the past week
4. Run `/portfolio audit` again to see if gaps reduced
```

### Example 3: Pre-October Preparation
```
1. `/portfolio audit` to see what's strong, what's weak
2. `/portfolio draft 3` to write your Dimension 3 answer (metrics)
3. Adjust your work plan to close gaps
4. `/portfolio scan` weekly to capture new evidence as you work
5. October: submit evaluation form with completed answers
```

---

## Files Involved

| File | What it does |
|---|---|
| `helpers/portfolio-builder.md` | Detection engine — signal mapping and dimension logic |
| `evidence-log.md` | Source of truth — your official evidence log (5 dimensions) |
| `evidence-staging.md` | Review buffer — new findings await your approval |
| `evidence-scan.snapshot.md` | Scan state — remembers last scan date to avoid rescans |
| `archive/` | Timestamped backups — safe copy before each approval |
| `.claude/skills/portfolio/agents/evidence-scanner.md` | Sub-agent — does the actual scanning |

---

## Key Rules

1. **You always review before commitment.** Agent stages; you approve and own the final log.
2. **Archive-safe:** Before ANY write to `evidence-log.md`, today's version is backed up (Mode 2, Mode 6).
3. **Scope is GAP-only:** Cenfotec work is auto-filtered (ERS, educational assessment, review-assignment).
4. **No duplicates:** Agent checks the log before staging — won't duplicate evidence.
5. **Manual evidence gaps visible:** When time metrics or peer feedback are stale (7+ days), agent flags them.

---

## Next Steps

1. **Automated daily scans:** `/schedule portfolio scan` (runs at end of business)
2. **Weekly audit:** `/portfolio audit` to monitor gaps
3. **Time tracking:** Start logging time saved on EoD, Gantt, and other workflows (Dimension 3)
4. **August prep:** `/portfolio draft` your evaluation answers as evidence solidifies
5. **October:** Submit certified evidence and unlock your merit increase

---

## Companion Files

- **Engine:** `helpers/portfolio-builder.md` — full detection logic and dimension mapping
- **Rubric:** Embedded in this skill; also in `level3-portfolio` if you need more context
- **Evaluation framework:** `projects/ai_impact_evaluation/AI Impact Evaluation for MANAGERS.pdf`
