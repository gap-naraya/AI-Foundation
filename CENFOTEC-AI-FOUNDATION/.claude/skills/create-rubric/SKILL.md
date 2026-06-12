---
name: create-rubric
description: Use this skill when the user wants to create a rubric for an assignment. Triggers on "create rubric", "generate rubric", "I need a rubric for [assignment]", "build rubric for", or similar phrases.
---

# Create Rubric Skill

When triggered, help Nelson generate a rubric for an assignment. This skill is conversational — iterates with Nelson until the rubric is perfect, then saves it to the correct location.

---

## Step 1 — Gather Information

Ask Nelson for:
1. **Assignment name** (e.g., "Final Essay", "Group Presentation", "Code Project")
2. **Assignment type** (e.g., Essay, Presentation, Code project, Mixed)
3. **Total points** (default: 100; allows custom)
4. **Course name** (to know where to save the rubric)
5. **Assignment instructions file** (optional — path to PDF or Word doc with the assignment description)

---

## Step 2 — Read the Assignment Instructions (if provided)

If Nelson provided an assignment instructions file:
1. Read and extract the full content
2. Identify key requirements and learning objectives
3. Note any specific evaluation criteria mentioned in the instructions

If no file was provided, skip to Step 3.

---

## Step 3 — Propose a Rubric

Based on the assignment type and instructions (if available), propose a rubric with a balanced number of criteria based on the amount of work needed.

If instructions were provided, ground the criteria in the actual requirements described. If not, use a generic template for the assignment type.

### Structure

Each criterion must have:
- **Name** (what's being evaluated)
- **Max Points** (the maximum for this criterion)
- **Description** (what excellence looks like)

## Step 4 — Iterate with Nelson

After proposing the rubric, ask: **"Any adjustments?"**

Nelson can say things like:
- "Adjust X to Y points" → recalculate other criteria proportionally if needed
- "Add a criterion for Z" → add it and adjust point distribution
- "Remove [criterion]" → remove it, redistribute points
- "That looks good" → proceed to save

**Key rule:** The total must always equal the target points (default 100).

---

## Step 5 — Save the Rubric

Once Nelson approves, save to:

```
/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/rubric-[Assignment-Name].md
```

Create the course subfolder if it doesn't exist.

**File format:**

```markdown
# [Assignment Name] — Rubric

Total Points: 100

| Criterion         | Max Points | Description                        |
|-------------------|------------|------------------------------------|
| [Name]            | [Points]   | [Description]                      |
| [Name]            | [Points]   | [Description]                      |
```

---

## Step 6 — Confirm & Close

Report:
- **Path**: where the rubric was saved
- **Status**: "Rubric saved. Ready to use in your next review."

Example:
```
✓ Rubric saved to: courses/Software-Dev-101/rubric-Final-Essay.md

Ready to use in your next review! When you're ready to grade, say:
- "grade Group A's Final Essay" (if it's a group submission)
- "review [Student Name]'s Final Essay" (if individual)
```

---

## Important Rules

- **Always proportional**: If Nelson changes points for one criterion, ensure the total still equals the target
- **Descriptions matter**: They guide grading. Make them specific enough that Claude can evaluate student work against them
- **Be flexible**: Nelson can iterate as many times as needed before saving
- **Default Spanish**: Keep criterion names and descriptions in Spanish if courses are taught in Spanish (check context/courses.md)
