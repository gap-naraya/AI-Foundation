#!/usr/bin/env python3
"""
Monthly Evidence Update Orchestrator

Automates the monthly update cycle for Level 3 evidence portfolio:
1. Collects metrics from workflow execution
2. Runs Evidence Extraction Agent with new data
3. Runs Evidence Validation Agent
4. Commits updated evidence to git
5. Generates progress report

Usage:
  python3 monthly-orchestrator.py --month june --year 2026
  python3 monthly-orchestrator.py --month july --year 2026
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
LEVEL3_EVIDENCE_DIR = PROJECT_ROOT / "Level3 Evidence"
AGENTS_DIR = PROJECT_ROOT / "agents"

class EvidenceOrchestrator:
    def __init__(self, month, year):
        self.month = month.lower()
        self.year = year
        self.timestamp = datetime.now().isoformat()
        self.metrics = {}
        self.evidence_updated = False
        self.validation_passed = False

    def log(self, message):
        """Print timestamped log message"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def step(self, step_num, message):
        """Print step header"""
        print(f"\n{'='*60}")
        print(f"STEP {step_num}: {message}")
        print(f"{'='*60}\n")

    # ========== STEP 1: Collect Metrics ==========

    def collect_metrics(self):
        """Collect execution metrics from workflow logs"""
        self.step(1, "Collect Workflow Metrics")

        try:
            # Look for workflow execution logs
            log_pattern = LEVEL3_EVIDENCE_DIR / f"workflow_logs_{self.month}_{self.year}.json"

            if log_pattern.exists():
                with open(log_pattern) as f:
                    self.metrics = json.load(f)
                self.log(f"✓ Loaded metrics for {self.month} {self.year}")
                self.log(f"  - Workflows executed: {self.metrics.get('workflows_count', 0)}")
                self.log(f"  - Total time saved: {self.metrics.get('time_saved_minutes', 0)} min")
                self.log(f"  - Reports generated: {self.metrics.get('reports_count', 0)}")
            else:
                self.log(f"⚠ No metrics file found at {log_pattern}")
                self.log(f"  Expected: workflow_logs_{self.month}_{self.year}.json")
                self.log("  Create this file with workflow execution data")
                return False

            return True

        except Exception as e:
            self.log(f"✗ Error collecting metrics: {e}")
            return False

    # ========== STEP 2: Generate Evidence Update Prompt ==========

    def generate_extraction_prompt(self):
        """Generate prompt for Evidence Extraction Agent"""
        self.step(2, "Generate Evidence Extraction Prompt")

        prompt = f"""
You are updating Nelson's Level 3 evidence portfolio with {self.month.capitalize()} {self.year} outcomes.

## New Data from {self.month.capitalize()} {self.year}

### Workflow Execution Metrics
- Workflows executed: {self.metrics.get('workflows_count', 0)}
- Reports generated: {self.metrics.get('reports_count', 0)}
- Time saved (actual): {self.metrics.get('time_saved_minutes', 0)} minutes
- Average per-workflow time: {self.metrics.get('avg_workflow_time', 0)} minutes
- Quality issues: {self.metrics.get('quality_issues', 0)}

### Stakeholder Feedback
{self._format_stakeholder_feedback()}

### Risks That Occurred
{self._format_risks_occurred()}

### Time Reinvestment Evidence
{self._format_time_reinvestment()}

### Additional Evidence
{self._format_additional_evidence()}

## Your Task

Update the Level 3 evidence files with this {self.month.capitalize()} {self.year} data:

1. Integrate real metrics into existing evidence
2. Update affected files:
   - 01_AI_Integration_Daily_Workflow.md (with actual time reinvestment data)
   - 03_Measurable_Impact_and_Outcomes.md (with real metrics)
   - 07_Risk_Mitigation.md (with actual risk events)

3. Add new section: "{self.month.capitalize()} {self.year} Outcomes"
4. Keep original evidence; append new evidence chronologically
5. Ensure consistency across all files

Output the updated markdown files ready for the portfolio.

Reference: /Users/naraya/Documents/AI-Foundation/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf
"""

        self.log("✓ Extraction prompt generated")
        self._save_prompt(f"extraction_prompt_{self.month}_{self.year}.md", prompt)

        return prompt

    def _format_stakeholder_feedback(self):
        """Format stakeholder feedback from metrics"""
        feedback = self.metrics.get('stakeholder_feedback', {})
        formatted = ""

        for stakeholder, comments in feedback.items():
            formatted += f"\n**{stakeholder}:**\n"
            for comment in comments:
                formatted += f"- {comment}\n"

        return formatted if formatted else "- No feedback collected yet"

    def _format_risks_occurred(self):
        """Format risks that actually occurred"""
        risks = self.metrics.get('risks_occurred', [])
        formatted = ""

        for risk in risks:
            formatted += f"\n- **{risk['name']}**\n"
            formatted += f"  - What happened: {risk.get('what_happened', 'N/A')}\n"
            formatted += f"  - Mitigation effectiveness: {risk.get('mitigation_worked', 'Unknown')}\n"
            formatted += f"  - Learnings: {risk.get('learnings', 'N/A')}\n"

        return formatted if formatted else "- No major risks occurred"

    def _format_time_reinvestment(self):
        """Format how freed time was reinvested"""
        reinvestment = self.metrics.get('time_reinvestment', {})
        formatted = ""

        for activity, hours in reinvestment.items():
            formatted += f"- **{activity}**: {hours} hours this month\n"

        return formatted if formatted else "- Time allocation pending"

    def _format_additional_evidence(self):
        """Format any additional evidence"""
        additional = self.metrics.get('additional_evidence', [])
        formatted = ""

        for evidence in additional:
            formatted += f"- {evidence}\n"

        return formatted if formatted else "- None"

    # ========== STEP 3: Run Evidence Extraction Agent ==========

    def run_extraction_agent(self, prompt):
        """Trigger Evidence Extraction Agent (would call Agent tool in Claude)"""
        self.step(3, "Run Evidence Extraction Agent")

        self.log("✓ Ready to invoke Evidence Extraction Agent")
        self.log(f"  Prompt saved: extraction_prompt_{self.month}_{self.year}.md")
        self.log("\nIMPORTANT: This step requires manual agent invocation:")
        self.log(f"""
  Agent(
    subagent_type: "general-purpose",
    description: "Update Level 3 evidence with {self.month.capitalize()} {self.year} outcomes",
    prompt: [See extraction_prompt_{self.month}_{self.year}.md]
  )
        """)

        self.log("\nAgent will:")
        self.log("  1. Read the new metrics and feedback")
        self.log("  2. Update evidence files with real outcomes")
        self.log("  3. Generate updated markdown files")
        self.log("\nAfter agent completes, move updated files to Level3 Evidence folder")

        return True

    # ========== STEP 4: Run Validation Agent ==========

    def run_validation_agent(self):
        """Trigger Evidence Validation Agent"""
        self.step(4, "Run Evidence Validation Agent")

        self.log("✓ Ready to invoke Evidence Validation Agent")
        self.log("\nIMPORTANT: This step requires manual agent invocation:")
        self.log(f"""
  Agent(
    subagent_type: "general-purpose",
    description: "Validate updated Level 3 evidence",
    prompt: [See agents/evidence-validation/prompt.md]
  )
        """)

        self.log("\nAgent will:")
        self.log("  1. Review all 5 evidence files")
        self.log("  2. Check alignment with Level 3 criteria")
        self.log("  3. Identify any gaps or weaknesses")
        self.log("  4. Generate validation report")

        return True

    # ========== STEP 5: Create Progress Report ==========

    def create_progress_report(self):
        """Generate monthly progress report"""
        self.step(5, "Generate Progress Report")

        report = f"""# Evidence Portfolio Progress Report

## {self.month.capitalize()} {self.year}

**Report Generated:** {self.timestamp}

### Workflow Execution Summary
- Workflows executed: {self.metrics.get('workflows_count', 0)}
- Reports generated: {self.metrics.get('reports_count', 0)}
- Time saved: {self.metrics.get('time_saved_minutes', 0)} minutes
- Quality issues: {self.metrics.get('quality_issues', 0)}

### Evidence Updates
- Files updated: [Number to be determined after extraction]
- Validation status: [Pending validation]
- Critical issues: [None identified yet]

### Metrics Progress
| Metric | June Baseline | {self.month.capitalize()} Actual | Trend |
|--------|---------------|-----|-------|
| Time saved/week | 115 min | {self.metrics.get('time_saved_minutes', 0)} min | ↑ if higher |
| Reports quality | Baseline | [Post-validation] | [To be determined] |

### Stakeholder Feedback
[Summary of stakeholder responses]

### Risks Status
- Risks identified: [Number]
- Risks occurred: {len(self.metrics.get('risks_occurred', []))}
- Mitigation effectiveness: [Post-validation]

### Next Steps
1. ✅ Metrics collected
2. ⏳ Evidence extraction (agent pending)
3. ⏳ Evidence validation (agent pending)
4. ⏳ Git commit
5. ⏳ Finalize for October submission

### Timeline to October
- Current month: {self.month.capitalize()} {self.year}
- Months until submission: [Calculate based on current date]
- Evidence completeness: [Pending validation]

---
*This report is part of the automated monthly evidence update cycle.*
*Full evidence portfolio: Level3 Evidence/ folder*
"""

        report_path = LEVEL3_EVIDENCE_DIR / f"progress_report_{self.month}_{self.year}.md"
        report_path.write_text(report)

        self.log(f"✓ Progress report generated: {report_path.name}")

        return report_path

    # ========== STEP 6: Commit to Git ==========

    def commit_to_git(self):
        """Commit updates to git"""
        self.step(6, "Commit to Git")

        try:
            os.chdir(PROJECT_ROOT)

            # Stage files
            subprocess.run(
                ["git", "add", "Level3 Evidence/"],
                check=True,
                capture_output=True
            )

            # Commit
            commit_msg = f"Update Level 3 evidence with {self.month.capitalize()} {self.year} outcomes and metrics\n\nAutomated monthly update cycle"
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                check=True,
                capture_output=True
            )

            self.log("✓ Committed to git")

            # Push
            subprocess.run(
                ["git", "push", "origin", "main"],
                check=True,
                capture_output=True
            )

            self.log("✓ Pushed to remote")

        except subprocess.CalledProcessError as e:
            self.log(f"⚠ Git operation warning: {e}")
            return False

        return True

    # ========== Utilities ==========

    def _save_prompt(self, filename, content):
        """Save prompt to file for reference"""
        filepath = AGENTS_DIR / "evidence-automation" / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

    def run_full_cycle(self):
        """Execute complete monthly cycle"""
        print(f"\n{'#'*60}")
        print(f"# LEVEL 3 EVIDENCE MONTHLY UPDATE CYCLE")
        print(f"# Month: {self.month.capitalize()} {self.year}")
        print(f"# Start time: {self.timestamp}")
        print(f"{'#'*60}\n")

        # Step 1: Collect metrics
        if not self.collect_metrics():
            self.log("\n✗ Cannot proceed without metrics. Exiting.")
            return False

        # Step 2: Generate extraction prompt
        extraction_prompt = self.generate_extraction_prompt()

        # Step 3: Run extraction agent (manual)
        self.run_extraction_agent(extraction_prompt)

        # Step 4: Run validation agent (manual)
        self.run_validation_agent()

        # Step 5: Generate progress report
        self.create_progress_report()

        # Step 6: Commit (after manual steps complete)
        self.log(f"\n{'='*60}")
        self.log("AFTER MANUAL STEPS COMPLETE:")
        self.log("  1. Run Evidence Extraction Agent with the generated prompt")
        self.log("  2. Run Evidence Validation Agent")
        self.log("  3. Review outputs and move files to Level3 Evidence/")
        self.log("  4. Run: python3 monthly-orchestrator.py --month {self.month} --commit")
        self.log(f"{'='*60}\n")

        return True

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Automate monthly Level 3 evidence updates"
    )
    parser.add_argument("--month", required=True, help="Month (june, july, august, september)")
    parser.add_argument("--year", type=int, default=2026, help="Year (default: 2026)")
    parser.add_argument("--commit", action="store_true", help="Only commit (skip agent steps)")

    args = parser.parse_args()

    orchestrator = EvidenceOrchestrator(args.month, args.year)

    if args.commit:
        orchestrator.log("Running commit-only mode...")
        orchestrator.commit_to_git()
    else:
        orchestrator.run_full_cycle()

if __name__ == "__main__":
    main()
