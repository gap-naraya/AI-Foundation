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

---

## Step 2 — Propose a Rubric

Based on the assignment type, propose a rubric with **4–6 criteria**.

### Structure

Each criterion must have:
- **Name** (what's being evaluated)
- **Max Points** (the maximum for this criterion)
- **Description** (what excellence looks like)

### Examples by Assignment Type

**Essay Rubric** (100 points):
| Criterion | Max Points | Description |
|-----------|------------|-------------|
| Content depth | 30 | Coverage, accuracy, and analysis of key concepts |
| Structure | 20 | Organization, logical flow, coherent argument |
| Sources/Evidence | 20 | Use of credible references, proper citations |
| Writing quality | 15 | Grammar, clarity, professional tone |
| Conclusions | 15 | Strength of analysis and takeaways |

**Presentation Rubric** (100 points):
| Criterion | Max Points | Description |
|-----------|------------|-------------|
| Content accuracy | 25 | Information is correct and relevant |
| Organization | 20 | Logical flow, clear structure |
| Visual design | 20 | Engaging slides, professional appearance |
| Delivery | 20 | Clarity, pacing, eye contact, confidence |
| Q&A handling | 15 | Answers questions confidently and thoroughly |

**Code Project Rubric** (100 points):
| Criterion | Max Points | Description |
|-----------|------------|-------------|
| Functionality | 30 | Code runs, meets requirements |
| Code quality | 25 | Clean, readable, well-commented |
| Testing | 20 | Adequate test coverage, edge cases handled |
| Documentation | 15 | README, comments, usage instructions |
| Creativity/extras | 10 | Bonus features, optimization, user experience |

---

## Step 3 — Iterate with Nelson

After proposing the rubric, ask: **"Any adjustments?"**

Nelson can say things like:
- "Adjust X to Y points" → recalculate other criteria proportionally if needed
- "Add a criterion for Z" → add it and adjust point distribution
- "Remove [criterion]" → remove it, redistribute points
- "That looks good" → proceed to save

**Key rule:** The total must always equal the target points (default 100).

---

## Step 4 — Save the Rubric

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

## Step 5 — Confirm & Close

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
