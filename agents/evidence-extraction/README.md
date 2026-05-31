# Evidence Extraction & Transformation Agent

## Purpose
Extract real evidence from project work, conversation history, and project files, then transform it into valid Level 3 AI Assessment format aligned with the 5 evaluation dimensions.

## When to Use
- After implementing a new AI workflow or process
- When preparing Level 3 assessment submissions
- When you have real work/metrics that needs to be articulated as evidence
- When converting operational work into formal assessment documentation

## What It Does
1. Reads conversation history and project context
2. Extracts specific examples, metrics, and outcomes
3. Maps evidence to the 5 Level 3 evaluation dimensions
4. Generates markdown files ready for submission
5. Ensures all evidence is grounded in real work, not hypothetical

## Expected Output
5 markdown files (one per dimension):
- `01_AI_Integration_Daily_Workflow.md`
- `02_Validation_and_Governance.md`
- `03_Measurable_Impact_and_Outcomes.md`
- `04_AI_System_Design_and_Orchestration.md`
- `05_Multiplier_Effect_and_Scaling.md`

## How to Invoke
```
Agent(
  subagent_type: "general-purpose",
  description: "Extract and transform Level 3 evidence from project work",
  prompt: [See prompt.md]
)
```

## Key Constraints
- ✅ **Ground in REAL examples only** - No hypothetical scenarios
- ✅ **Include measurable metrics** where available
- ✅ **Validate against PDF** - Reference `/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf`
- ✅ **Map to dimensions** - Each piece addresses one or more of the 5 dimensions
- ✅ **Avoid exaggeration** - Stick to demonstrated, verifiable facts

## Example Usage Scenario
You've implemented a new AI workflow and want to document it as Level 3 evidence:

1. Gather real metrics (before/after time savings, quality improvements, etc.)
2. Document the design decisions and architecture
3. Spawn this agent with context about your implementation
4. Agent extracts evidence and generates files
5. Review and refine as needed

## Notes
- First used successfully to generate Level 3 evidence portfolio for Nelson's communication workflow project
- Can be reused for any AI integration project requiring assessment documentation
