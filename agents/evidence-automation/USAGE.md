# Evidence Automation Pipeline — Usage Guide

Automated monthly updates to your Level 3 evidence portfolio.

## How It Works

### Weekly: Data Collection (Manual)
You track workflow execution metrics weekly:
- Time spent on each workflow
- Reports generated
- Stakeholder feedback
- Any issues or risks that occurred

### Monthly: Automated Update Cycle (Semi-automated)

**First Week of Month:**

```bash
./monthly-update.sh june 2026
```

The script will:
1. ✅ Validate that you have metrics data
2. ✅ Generate a prompt for Evidence Extraction Agent
3. ✅ Create a progress report
4. ⏳ Show you the next steps

**What You Do:**
- Copy the generated prompt
- Invoke Evidence Extraction Agent with it
- Run Evidence Validation Agent
- Review outputs
- Commit to git

**Result:** Updated evidence files with real metrics and outcomes

---

## Step-by-Step Setup

### 1. Make Scripts Executable

```bash
chmod +x monthly-update.sh
```

### 2. Create Your Metrics File

For each month, create a file: `workflow_logs_[MONTH]_[YEAR].json`

**Template Location:** `metrics-template.json`

**How to fill it:**

```json
{
  "month": "june",
  "year": 2026,
  "workflows_count": 4,
  "time_savings": {
    "baseline_per_week_minutes": 180,
    "actual_per_week_average_minutes": 65,
    "percentage_reduction": 63.9
  },
  "stakeholder_feedback": {
    "Ken Manley": ["Report is clear", "Good format"],
    "Gerardo Mora": ["Operational detail appreciated"]
  },
  "risks_occurred": [
    {
      "risk_name": "Missing transcript",
      "mitigation_worked": true,
      "learnings": "Early validation helps"
    }
  ],
  "time_reinvestment": {
    "Level 3 study": 6.0,
    "Strategic work": 1.0
  }
}
```

**Place it:** `Level3 Evidence/workflow_logs_june_2026.json`

### 3. Run Monthly Automation

**First time (June):**
```bash
./monthly-update.sh june 2026
```

The script will:
- ✅ Check that metrics file exists
- ✅ Generate extraction prompt
- ✅ Create progress report
- ⏳ Tell you what to do next

### 4. Manual Agent Steps

**Step 1: Run Evidence Extraction Agent**

The script generates: `extraction_prompt_june_2026.md`

Use it to invoke:
```
Agent(
  subagent_type: "general-purpose",
  description: "Update Level 3 evidence with June 2026 outcomes",
  prompt: [See extraction_prompt_june_2026.md]
)
```

The agent will output updated evidence files.

**Step 2: Review & Move Files**

- Review the generated evidence files
- Check that they integrate new metrics well
- Move them to: `Level3 Evidence/`

**Step 3: Run Evidence Validation Agent**

Use the validation agent prompt:
```
Agent(
  subagent_type: "general-purpose",
  description: "Validate updated Level 3 evidence",
  prompt: [See agents/evidence-validation/prompt.md]
)
```

The agent will identify any gaps or issues.

**Step 4: Address Validation Feedback**

- Review the validation report
- Fix any critical issues
- Make manual adjustments if needed

### 5. Commit to Git

```bash
git add "Level3 Evidence/"
git commit -m "Update Level 3 evidence with June 2026 outcomes and metrics"
git push origin main
```

---

## Monthly Checklist

### Week 1 of Month
- [ ] Gather workflow execution metrics
- [ ] Collect stakeholder feedback
- [ ] Document any risks that occurred
- [ ] Note how freed time was reinvested
- [ ] Create `workflow_logs_[MONTH]_[YEAR].json` file

### Week 2 of Month
- [ ] Run: `./monthly-update.sh [month] [year]`
- [ ] Invoke Evidence Extraction Agent
- [ ] Review and move updated files
- [ ] Invoke Evidence Validation Agent
- [ ] Review validation report

### Week 3 of Month
- [ ] Address validation feedback
- [ ] Make manual adjustments if needed
- [ ] Commit to git
- [ ] Verify push to remote

---

## What Gets Automated

✅ **Automated by Scripts:**
- Pre-flight checks (Python, git, directories)
- Metrics validation (JSON format)
- Prompt generation (for Evidence Extraction)
- Progress report creation
- Git operations (add, commit, push)

⏳ **Manual (Agent-based):**
- Evidence extraction (Evidence Extraction Agent)
- Evidence validation (Evidence Validation Agent)
- Quality review (you)

---

## Scheduling (Optional)

To run automatically every 1st of the month:

```bash
# Add to crontab (runs first day of each month at 8am)
0 8 1 * * /Users/naraya/Documents/AI-Foundation/agents/evidence-automation/monthly-update.sh $(date +\%B | tr '[:upper:]' '[:lower:]') $(date +\%Y)
```

---

## File Structure

```
agents/evidence-automation/
├── README.md                          (Overview)
├── USAGE.md                           (This file)
├── monthly-orchestrator.py            (Main automation script)
├── monthly-update.sh                  (Shell wrapper)
├── metrics-template.json              (Template for metrics)
└── extraction_prompt_[MONTH]_[YEAR].md (Generated)
```

---

## Troubleshooting

**Error: "Metrics file not found"**
- Solution: Create `workflow_logs_[MONTH]_[YEAR].json` in `Level3 Evidence/`
- Use `metrics-template.json` as a starting point

**Error: "Metrics file is not valid JSON"**
- Solution: Check JSON syntax (missing commas, quotes, brackets)
- Validate at: https://jsonlint.com/

**Agent not producing output**
- Ensure you're using the correct prompt file
- Check that context is filled in correctly
- Review agent requirements

**Git push fails**
- Make sure you have internet connection
- Check git credentials: `git config --list`
- Verify branch: `git branch`

---

## Timeline Example

**June 2026:**
- Jun 1-30: Execute workflows, collect metrics
- Jul 1: Run `./monthly-update.sh june 2026`
- Jul 2-3: Evidence extraction + validation
- Jul 4: Commit to git

**July 2026:**
- Jul 1-31: Execute workflows, collect metrics
- Aug 1: Run `./monthly-update.sh july 2026`
- Aug 2-3: Evidence extraction + validation
- Aug 4: Commit to git

**October 2026:**
- Aggregated evidence from June, July, August, September
- Submit Level 3 assessment with 4 months of validated outcomes

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `metrics-template.json` | Template for monthly metrics |
| `monthly-update.sh` | Main automation script |
| `monthly-orchestrator.py` | Orchestration logic |
| `extraction_prompt_[MONTH].md` | Generated prompt for agent |
| `progress_report_[MONTH].md` | Monthly progress summary |
| `update.log` | Complete execution log |

---

## Questions?

Refer to:
- **Extraction Agent:** `agents/evidence-extraction/prompt.md`
- **Validation Agent:** `agents/evidence-validation/prompt.md`
- **Level 3 Criteria:** `Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf`

All documentation is in the repository for reference.
