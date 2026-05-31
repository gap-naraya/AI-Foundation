# Evidence Validation Agent

## Purpose
Review evidence files against Level 3 assessment criteria and identify gaps or weaknesses in argumentation.

## When to Use
- After evidence files are generated or updated
- Before submitting evidence for formal evaluation
- To validate that claims are sufficiently grounded in real examples
- To identify missing dimensions or metrics

## What It Does
1. Reads all evidence files in the Level3 Evidence folder
2. Compares against Level 3 criteria from the PDF
3. Identifies missing evidence, weak claims, or unsupported assertions
4. Checks for consistency across all 5 dimensions
5. Generates a validation report with specific gaps

## Expected Output
- **validation-report.md** - Detailed gap analysis by dimension
- **strength-summary.md** - What's working well in the evidence
- **improvement-priorities.md** - What to focus on next

## Status
✅ **Ready** - Fully documented and tested

## How to Use (When Ready)
```
Agent(
  subagent_type: "general-purpose",
  description: "Validate Level 3 evidence against evaluation criteria",
  prompt: [See prompt.md - to be created]
)
```

## Key Validation Criteria
- Evidence is grounded in real examples (not hypothetical)
- All claims can be traced to specific work
- Metrics are measurable and quantified
- Impact is demonstrated, not claimed
- All 5 dimensions are addressed

## Next Steps
1. Create detailed validation prompt
2. Test with existing evidence portfolio
3. Iterate based on results
4. Document findings and improvements
