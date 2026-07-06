# Level 3 Portfolio Builder — Engine

Nelson's goal: Reach Level 3 AI Value Leader by October 2026 to unlock merit increase.

This helper defines the automated workflow for scanning GAP/Mediquant AI evidence and staging it for approval.

**Scope:** Only GAP-related work (Mediquant DOM, Claude OS system, GAP process automation). Exclude Cenfotec-scoped work (educational assessment, ERS grading, review-assignment skill).

---

## The 5 Evaluation Dimensions (Reference)

1. **AI Integration in Daily Workflow** — AI is the default starting point for management workflows. Designed repeatable AI-powered processes. Time reclaimed from admin reinvested in strategy.
2. **Appropriate Use & Validation** — Models exemplary validation behavior. Human-in-the-loop on all outputs. Knows where AI should NOT replace judgment.
3. **Productivity & Measurable Impact** — Demonstrates improvement across multiple metric categories (time saved, decision cycle, communication efficiency, etc.).
4. **Capacity to Design & Orchestrate AI Processes** — Designs multi-step AI workflows. Creates reusable blueprints.
5. **AI as Multiplier Across Teams** — Uplevels team AI maturity. Creates frameworks adopted by others. Contributes to org strategy.

---

## Detection Workflow

### Step 1: Determine Time Window

- If `evidence-scan.snapshot.md` exists: read it to find the last scan date
- Calculate window: "from [last_scan_date] to now"
- If no snapshot exists: scan the last 24 hours (first run)

### Step 2: Scan Git History

Run: `git log --since="[window_start]" --until="[window_end]" --oneline --all`

For each commit:
- Extract message and hash
- Run through **Commit Signal Map** below

**Commit Signal → Dimension Mapping:**

| Keyword in message | Dimension | Example | Evidence type |
|---|---|---|---|
| `Add ... skill` / `Implement ... skill` | 4 | "Add ERS-review-assignment skill" | New reusable workflow |
| `Fix ... skill` / `Refactor ... skill` / `Update ... skill` | 4 | "Fix gantt skill date parsing" | Iterative refinement |
| `Add ... helper` | 1 or 4 | "Add portfolio-builder helper" | New workflow design |
| `Update eod` / `Refactor eod` / `Fix eod` | 1 | "Fix EoD snapshot logic" | Repeated automation |
| `Add ... feedback` / `Add ERS` | 5 | "Add ERS feedback for Pied Piper" | Coaching / teaching |
| `Add ... blueprint` | 5 | "Add Claude OS blueprint" | Knowledge transfer artifact |
| `Share` (in message) | 5 | "Share PM guide with Gerardo" | Team adoption signal |
| Commit count ≥5 in one day | 4 | Multiple commits same day | Active AI-assisted dev session |

### Step 3: Scan Modified Files

Run: `find . -newer evidence-scan.snapshot.md -type f -name "*.md" | grep -v archive | grep -v staging`

For each file modified since last scan:

| Path pattern | Dimension | Example |
|---|---|---|
| `helpers/` or `.claude/skills/` | 1 or 4 | New helper = workflow design (Dim 1 or 4) |
| `projects/ai_impact_evaluation/` | 4 | Portfolio work = meta-design (Dim 4) |
| `context/` | 1 | Knowledge base = workflow support (Dim 1) |
| `projects/mediquant/` | 1 | Active project workflow (Dim 1) |
| `projects/cenfotec/` | 5 | Teaching/assessment work (Dim 5) |

### Step 4: Check for Duplicates

Load `evidence-log.md` and parse existing entries. For each new finding:
- Extract: commit hash (if applicable) and item title
- Search log for exact match by hash or by title (fuzzy match on file path)
- Skip if duplicate found; note in staging output

### Step 5: Check for Manual Entry Gaps

For each dimension, find the most recent entry in `evidence-log.md`:
- **Dimension 3 (Measurable Impact):** If last entry is >7 days old, flag `⚠️ MANUAL ENTRY NEEDED`
- **Dimension 5 (Team Multiplier):** If no entries in last 30 days, flag `⚠️ MANUAL ENTRY NEEDED`

Manual entries require Nelson's hand-written notes (time tracking, peer feedback, etc.) — the agent cannot auto-detect these.

### Step 6: Generate Staged Output

Write to `evidence-staging.md` in this format:

```markdown
## Scan: [TODAY] — [N] items pending review

### Dimension 1: AI Integration in Daily Workflow — [N] items
#### [Item title from commit/file]
- **What:** [plain description of what changed]
- **Signal:** git commit `[hash]` / file `[path]`
- **Evidence value:** [why this counts for dimension 1]
- **Status:** 🟡 STAGED

### Dimension 4: Capacity to Design & Orchestrate AI Processes — [N] items
...

---
⚠️ Dimension 3 — MANUAL ENTRY NEEDED (last entry: June 17, 2026)
Add time-tracking notes: "How long did [task] take vs. before AI?"
```

### Step 7: Update Snapshot

Overwrite `evidence-scan.snapshot.md`:

```markdown
# Evidence Scan Snapshot

Last scan: [TODAY at HH:MM UTC]
Window: [START] to [END]
Items staged: [N]
```

---

## Validation Rules (Human-in-the-Loop)

- Agent NEVER writes to `evidence-log.md` directly
- Agent writes only to `evidence-staging.md` for review
- Nelson reviews each staged item: approve, reject, or edit
- Only after approval does the item move to `evidence-log.md`
- Before ANY write to `evidence-log.md`, create archive: `archive/evidence-log-YYYY-MM-DD.md`

---

## What the Agent Cannot Detect

- **Dimension 3 metrics:** Time saved per workflow, decision cycle reduction, communication efficiency. Requires Nelson's manual time logs.
- **Dimension 5 adoption events:** Gerardo's feedback, peer PM adoption, org strategy impact. Requires direct observation or Slack messages from others.

Agent flags these as `⚠️ MANUAL ENTRY NEEDED` when stale.

---

## Approval Workflow (Skill Mode 2)

After staging, Nelson invokes `/portfolio-scan approve`:

1. Skill reads all `🟡 STAGED` items from `evidence-staging.md`
2. For each item: "Approve? (y/n/edit):"
   - **y** → marked for promotion
   - **n** → item is deleted from staging
   - **edit** → Nelson provides replacement text; item marked for promotion with edited content
3. **Before writing promoted items to `evidence-log.md`:**
   - Create `projects/ai_impact_evaluation/archive/` if missing
   - Copy current `evidence-log.md` → `archive/evidence-log-YYYY-MM-DD.md` (append-only backup)
4. For each approved item:
   - Add `✅ APPROVED [DATE]` status
   - Find correct dimension section in `evidence-log.md`
   - Append item at the end of that dimension's evidence items list
5. Clear `evidence-staging.md`
6. Commit changes (if git add/commit is enabled)

---

## Reusable Patterns (Used in Implementation)

- **Snapshot state tracking:** Same as `projects/mediquant/eod-report.previous.md` — lightweight rolling state file, not full history
- **Read-only scanning:** No writes except to staging or (after approval) to log
- **Dimension-based organization:** Mirrors the 5-dimension structure of `evidence-log.md` and `level3-portfolio` skill
- **Manual entry flags:** Surfaces gaps that automation cannot fill, forcing human judgment
