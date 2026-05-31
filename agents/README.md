# Agents Directory

Custom AI agents for automating workflows in the AI Foundation project.

## Agent Types

### 1. Evidence Extraction & Transformation
**Purpose:** Extract real evidence from project work and transform it into valid Level 3 assessment format  
**Location:** `./evidence-extraction/`  
**Triggers:** When evidence needs to be generated from conversation history or project files  
**Output:** Markdown evidence files aligned with 5 evaluation dimensions  
**Status:** ✅ Active (used in evidence portfolio generation)

### 2. Evidence Validation
**Purpose:** Review evidence files against Level 3 criteria and identify gaps  
**Location:** `./evidence-validation/`  
**Triggers:** After evidence files are created or updated  
**Output:** Validation report with gap analysis  
**Status:** 🔄 Planned

### 3. Workflow Execution
**Purpose:** Execute the Thursday morning communication workflow (transcripts → reports → distribution)  
**Location:** `./workflow-execution/`  
**Triggers:** User message "Weekly workflow ready — Week ending [DATE]"  
**Output:** Three stakeholder-specific reports  
**Status:** 🔄 Planned

### 4. Risk Mitigation Auditor
**Purpose:** Identify and document risks in AI workflows  
**Location:** `./risk-auditor/`  
**Triggers:** When designing new AI processes  
**Output:** Risk assessment matrix with mitigations  
**Status:** 🔄 Planned

## How to Use Agents

### Spawning an Agent
```
Agent(
  subagent_type: "general-purpose",
  description: "Brief description of what this agent does",
  prompt: "Detailed instructions including context, constraints, and expected output"
)
```

### Agent Workflow
1. **Define** the agent's purpose and constraints in CLAUDE.md
2. **Document** the prompt and expected output in the agent's folder
3. **Test** with a simple example
4. **Iterate** based on results
5. **Store** the validated prompt for future reference

## File Structure for Each Agent

```
agents/
  agent-name/
    README.md              # Agent purpose, when to use, expected output
    prompt.md              # The full prompt to feed the agent
    schema.json            # Expected output structure (if applicable)
    examples.md            # Example inputs and outputs
    notes.md               # Learning and iteration notes
```

## Agent Management

- **Update agents** when workflow requirements change
- **Document learnings** in notes.md when an agent produces unexpected results
- **Version control** all agent definitions via git
- **Test before production** use—run simple examples first

## Reference

See `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/CLAUDE.md` for Level 3 evaluation criteria that agents working with evidence should follow.
