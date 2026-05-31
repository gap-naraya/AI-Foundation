# Agents Index

Quick reference for all custom agents in the AI Foundation project.

## Active Agents

### Evidence Extraction & Transformation ✅
- **Status:** Active
- **Purpose:** Generate Level 3 assessment evidence from project work
- **Location:** `./evidence-extraction/`
- **Last Used:** May 30, 2026 (Level 3 evidence portfolio)
- **Files:**
  - `README.md` - Overview and usage
  - `prompt.md` - Full agent prompt (reusable template)

**How to use:**
```
Agent(
  subagent_type: "general-purpose",
  description: "Extract and transform Level 3 evidence from project work",
  prompt: [See ./evidence-extraction/prompt.md]
)
```

---

## Planned Agents (Now Complete)

### Evidence Validation ✅
- **Status:** Ready
- **Purpose:** Validate evidence against Level 3 criteria and identify gaps
- **Location:** `./evidence-validation/`
- **Last Updated:** May 31, 2026
- **Use:** Before formal Level 3 submission (October 2026)
- **Files:**
  - `README.md` - Overview and usage
  - `prompt.md` - Full agent prompt with detailed validation criteria

### Workflow Execution ✅
- **Status:** Ready
- **Purpose:** Execute Thursday morning communication workflow
- **Location:** `./workflow-execution/`
- **Trigger:** User message "Weekly workflow ready — Week ending [DATE]"
- **First Run:** June 6, 2026
- **Files:**
  - `README.md` - Overview and usage
  - `prompt.md` - Complete execution prompt with all report templates

### Risk Mitigation Auditor ✅
- **Status:** Ready
- **Purpose:** Identify and document risks in new AI workflows
- **Location:** `./risk-auditor/`
- **Use:** Design phase of any new AI workflow
- **Files:**
  - `README.md` - Overview and usage
  - `prompt.md` - Comprehensive risk analysis framework

---

## Agent Development Workflow

### When Creating a New Agent

1. **Create subfolder** in `/agents/` with descriptive name
2. **Write README.md** with:
   - Purpose and when to use
   - What it does step-by-step
   - Expected output format
   - Key constraints
3. **Write prompt.md** with:
   - Full, detailed prompt
   - Context requirements
   - Output specifications
   - Usage instructions
4. **Test thoroughly** before marking as "Active"
5. **Document learnings** in notes.md
6. **Commit to git** with clear description

### Agent Prompt Template Structure

```
## Context
[Project background, constraints, user context]

## Your Task
[What the agent should do]

## Requirements/Constraints
[Hard requirements and limitations]

## Output Format
[Exact format expected]

## Reference Documents
[Links to documentation the agent should know about]

## Usage Instructions
[How to invoke, what to customize]
```

---

## Agent Best Practices

### Do ✅
- Ground all evidence in real examples
- Include specific metrics and outcomes
- Validate against authoritative sources (PDFs, documentation)
- Create reusable prompts for future use
- Document learnings and iterations
- Test with examples before production use

### Don't ❌
- Use hypothetical scenarios as evidence
- Make unsupported claims
- Skip validation or human review
- Assume the agent works perfectly first time
- Delete old versions without learning from them
- Hardcode specific data or credentials

---

## Shared References

**All agents should reference:**
- `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/CLAUDE.md` - Level 3 evaluation criteria
- `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf` - Authoritative PDF
- `/Users/naraya/Documents/AI-Foundation/CLAUDE.md` - Global project context

---

## Quick Links

- [Agent Design Document](./README.md)
- [Evidence Extraction Prompt](./evidence-extraction/prompt.md)
- [Communication Workflow Architecture](../Level3\ Evidence/04_AI_System_Design_and_Orchestration.md)
- [Risk Mitigation Examples](../Level3\ Evidence/07_Risk_Mitigation.md)

---

Last updated: May 31, 2026
