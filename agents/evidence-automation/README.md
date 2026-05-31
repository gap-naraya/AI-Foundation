# Evidence Automation Pipeline

Automated monthly updates to Level 3 evidence portfolio.

## What Gets Automated

### 1. Data Collection (Weekly)
- Workflow execution metrics (time spent, reports generated)
- Risk events (what actually happened)
- Metrics tracking (before/after comparisons)

### 2. Evidence Generation (Monthly)
- Evidence Extraction Agent runs automatically with collected data
- Generates updated evidence files incorporating real outcomes
- Integrates new metrics with existing evidence

### 3. Evidence Validation (Monthly)
- Evidence Validation Agent runs automatically
- Produces validation report
- Identifies gaps or weaknesses
- Flags what needs manual attention

### 4. Git Commits (Monthly)
- Automatically commits updated evidence
- Pushes to repository
- Creates audit trail of evolution

### 5. Dashboard & Reporting (Monthly)
- Generates progress report
- Shows metrics trends
- Tracks validation scores
- Alerts on issues needing attention

## Architecture

```
Weekly: Data Collection
   ↓
Monthly (1st week):
   ├─ Data Aggregation
   ├─ Evidence Extraction Agent
   └─ Evidence Validation Agent
   ↓
Monthly (2nd week):
   ├─ Dashboard Update
   ├─ Git Commit
   └─ Summary Report
```

## Status
🔄 **In Development** - Components being built

## Files in This Directory
- `metrics-collector.py` - Weekly data collection script
- `evidence-updater.py` - Monthly evidence update orchestration
- `dashboard-generator.py` - Progress dashboard creation
- `monthly-job.sh` - Main automation script (runs monthly)
- `weekly-job.sh` - Weekly data collection script
