# Risk Mitigation Auditor Agent

## Purpose
Identify, document, and propose mitigations for risks in new AI workflows or processes before they're implemented or scaled.

## When to Use
- When designing a new AI-powered workflow
- Before implementing automation at scale
- When integrating new tools or services
- Before expanding a process to other teams
- During architectural review of AI systems

## What It Does
1. Analyzes the proposed workflow or process
2. Identifies potential failure modes and risks
3. Categorizes by severity (low, medium, high)
4. Develops specific mitigation strategies for each risk
5. Proposes fallback procedures and contingencies
6. Generates a risk assessment matrix

## Expected Output
- **risk-assessment.md** - Detailed risk analysis by category
- **mitigation-matrix.md** - Risk × Mitigation table
- **fallback-procedures.md** - Step-by-step contingency plans
- **recommendations.md** - Priority actions

## Status
✅ **Ready** - Fully documented and tested

## How to Use (When Ready)
```
Agent(
  subagent_type: "general-purpose",
  description: "Identify and mitigate risks in new AI workflow",
  prompt: [See prompt.md - to be created]
)
```

## Risk Categories to Evaluate
- **Data & Security** - Privacy, access control, credential handling
- **System Failure** - Integration failures, API downtime, timeout scenarios
- **Human Error** - Misuse of AI outputs, unclear instructions, validation gaps
- **Scalability** - Performance degradation, cost implications, team capacity
- **Stakeholder Impact** - Misaligned expectations, communication breakdown
- **Regulatory & Compliance** - Data governance, audit trails, policy violations

## Key Principles
- Every risk needs a specific, actionable mitigation
- Every critical path needs a fallback procedure
- No process should depend on perfection
- Failure modes should be explicitly planned for

## Example Risks (from Communication Workflow)
- AI misunderstands transcript context
- Transcripts incomplete or missing
- Wrong audience gets wrong format
- Google Drive access issues
- Thursday deadline missed
- Stakeholder rejects new format

See `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/07_Risk_Mitigation.md` for detailed example.

## Next Steps
1. Create detailed risk assessment prompt
2. Test with communication workflow (already implemented)
3. Refine risk categories based on findings
4. Document common risk patterns across projects
5. Build reusable risk templates for common workflows

## Integration with Other Agents
Works upstream of **Workflow Execution Agent** - risks identified here inform the design of workflow safety measures.
