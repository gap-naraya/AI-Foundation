# Evidence Extraction & Transformation Agent Prompt

## Context

You are helping Nelson Araya prepare Level 3 AI Impact Evaluation evidence for her management role at Mediquant.

[INSERT PROJECT CONTEXT HERE - Include:]
- What AI workflow/process was implemented
- Key metrics and outcomes
- Design decisions made
- How it differs from previous approach
- Any stakeholder feedback

## Your Task

Extract real evidence from the conversation history and project files, then generate 5 markdown files—one for each Level 3 evaluation dimension. Each file should:

1. **Be grounded in REAL examples**, not hypothetical scenarios
2. **Include measurable metrics** where available
3. **Address the specific dimension** from the AI Impact Evaluation for Managers PDF
4. **Map to the Level 3 criteria** for that dimension
5. **Demonstrate strategic thinking and impact**, not just tool usage

## The 5 Evaluation Dimensions

### 1. AI Integration in Your Daily Management Workflow
- How AI became part of standard practice
- How repeatable processes were designed
- How freed time is reinvested in high-leverage work

### 2. Appropriate Use of AI and Validation of Outputs
- Validation approach and governance
- Risk mitigation and security considerations
- Human-in-the-loop architecture

### 3. Productivity and Measurable Impact on Delivery Outcomes
- Before/after metrics (time, quality, throughput)
- Multiple metric categories showing improvement
- Strategic reinvestment of freed time

### 4. Capacity to Design and Orchestrate AI-Driven Processes
- Multi-step workflow design
- Tools combined and integrated
- Documented system architecture

### 5. Use of AI as a Multiplier Across Teams and the Organization
- How others can adopt this workflow
- Knowledge artifacts and reusable frameworks
- Scaling pathway and organizational impact

## Output Format

Create 5 markdown files:
- `01_AI_Integration_Daily_Workflow.md`
- `02_Validation_and_Governance.md`
- `03_Measurable_Impact_and_Outcomes.md`
- `04_AI_System_Design_and_Orchestration.md`
- `05_Multiplier_Effect_and_Scaling.md`

Each file should be 500-800 words with:
- Clear statement of what Level 3 looks like for this dimension
- Specific examples from the actual workflow
- Real metrics and evidence
- Explanation of why this demonstrates Level 3 thinking
- How it exceeds Level 2 criteria

## Important Notes

- Use real examples from the conversation and files created
- Include actual metrics (avoid approximations)
- Explain the strategic thinking, not just the tool usage
- Show how this translates to team/organizational impact
- Avoid exaggeration—stick to what's actually been demonstrated
- Make it clear if this is ongoing work (measurement will continue, impact will be proven over time)

## Reference Documents

**Must read before analyzing:**
- `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/AI Impact Evaluation for MANAGERS.pdf`
- Pages 6-11: Level 3 definition and evaluation dimensions
- Pages 12-14: Evaluation standards and evidence requirements

---

## Usage Instructions

1. **Replace [INSERT PROJECT CONTEXT HERE]** with specific details about the implementation
2. **Provide project files or conversation history** that the agent should analyze
3. **Specify output location** where evidence files should be written
4. **Run agent** and review output
5. **Iterate** if evidence needs refinement

## Example Invocation

```
Agent(
  subagent_type: "general-purpose",
  description: "Extract and transform Level 3 evidence from project work",
  prompt: [This prompt with context filled in]
)
```
