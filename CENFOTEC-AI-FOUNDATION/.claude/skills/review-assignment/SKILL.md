---
name: review-assignment
description: Use this skill when the user wants to grade student work. Triggers on "grade Group [Name]", "review [Student Name]'s assignment", "evaluate submission", "give feedback on", or similar phrases.
---

# Review Assignment Skill

When triggered, read a student or group submission, apply the rubric (if one exists), and produce a graded feedback file with a grade breakdown and written feedback.

---

## Step 1 — Determine the Mode

Ask Nelson (or infer from context):

| Mode | Trigger | What it means |
|---|---|---|
| **Group** | "grade Group A", "review Group assignment", "evaluate [GroupName]" | One file for a whole group → all members get same grade |
| **Individual** | "review [StudentName]'s assignment", "grade [name]", "individual feedback" | One file for one student → personalized grade and feedback |

If ambiguous (e.g., "cenfotec review", "grade assignment"), ask: **"Is this for a group or an individual student?"**

---

## Step 2 — Gather Information

Ask Nelson for:

1. **File path** — where is the submission PDF/Word file?
2. **Group or student name** — who submitted this? (for group mode: "Group A"; for individual: "Maria Garcia")
3. **Course name** — which course is this for? (so Claude can find the roster if it's a group)
4. **Assignment name** — what's the assignment called? (so Claude can find the rubric)

---

## Step 3 — Read the Submission

Load:
- **Submission file** (PDF or Word) → extract and read the full content
- **Rubric** (if exists) → load from `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/rubric-[Assignment-Name].md`
- **Roster** (group mode only) → load from `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/roster.md` to confirm member names

If no rubric exists, proceed with holistic evaluation (0–100 scale with disclaimer).

---

## Step 4A — Group Mode: Read Roster and Evaluate

1. Find the group in the roster
2. Extract all member names
3. Read and evaluate the submission against the rubric (or holistically if no rubric)
4. Calculate grade breakdown (see format below)
5. **All members receive the same grade**

---

## Step 4B — Individual Mode: Evaluate

1. Read the submission
2. Evaluate against the rubric (or holistically if no rubric)
3. Calculate grade breakdown
4. Personalize feedback for this student

---

## Step 5 — Create Grade Breakdown Table

For **both modes**, produce a table showing:
- **Criterion name**
- **Max points**
- **Points lost** (as negative, e.g., -5)
- **Points earned** (calculated: max − lost)
- **Notes** (reason for each deduction)

**Format:**

```
| Criterion         | Max | Lost | Earned | Notes                              |
|-------------------|-----|------|--------|------------------------------------|
| Content depth     |  30 |   -5 |     25 | Missing analysis on topic X        |
| Structure         |  20 |    0 |     20 | Clear and well-organized           |
| Sources/Evidence  |  20 |  -10 |     10 | Only 2 references, needed 5+       |
| Presentation      |  15 |   -3 |     12 | Minor formatting inconsistencies   |
| Conclusions       |  15 |    0 |     15 | Strong and well-argued             |
|                   | 100 |  -18 | **82** |                                    |
```

**Rules:**
- Every deduction has a reason — never silent point drops
- Reasons are 1 line, specific, and actionable
- Total row shows: total max, total lost, total earned (final grade)

---

## Step 6 — Write Feedback

After the grade breakdown table, write **2–3 paragraphs of personalized feedback**:

1. **Strengths** — what the student/group did well (specific, not generic)
2. **Areas for improvement** — what needs work, with concrete suggestions
3. **Encouragement** — how they can improve next time

**Tone:**
- Constructive (focus on growth, not punishment)
- Specific (reference actual work, not general statements)
- Kind but honest (if something is weak, name it clearly)
- Supportive (assumes the student wants to improve)

**Example for a weak essay:**

```
### Feedback

**Strengths:** You clearly understand the main concept and your introduction sets up the argument well. The examples you provided from the case study are directly relevant.

**Areas for improvement:** The essay needs stronger evidence. You cited only two sources when the assignment asks for at least five. Additionally, your conclusion rushes the main argument—consider expanding it to synthesize your key points more thoroughly. Pay attention to citation formatting; APA style requires specific formatting for quotes.

**Next steps:** For your next essay, spend time finding sources early so you have variety in your evidence. Outline your conclusion before writing so you have space to fully develop it.
```

---

## Step 7 — Save the Feedback File

**Group mode:**
```
/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/reviews/[Assignment-Name]/feedback/[GroupName].md
```

**Individual mode:**
```
/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/reviews/[Assignment-Name]/feedback/[StudentName].md
```

Create the `reviews/[Assignment-Name]/feedback/` folder if it doesn't exist.

---

## Step 8 — File Format

**Feedback file structure:**

```markdown
# [Assignment Name] — [Group Name / Student Name]

## Members (Group mode only)
- María García
- Carlos Rodríguez
- Ana López

## Grade Breakdown

| Criterion | Max | Lost | Earned | Notes |
|-----------|-----|------|--------|-------|
| ... |

## Final Grade: **82 / 100**

### Feedback

[Your feedback paragraphs here]
```

**Individual student:**

```markdown
# [Assignment Name] — [Student Name]

## Grade Breakdown

| Criterion | Max | Lost | Earned | Notes |
|-----------|-----|------|--------|-------|
| ... |

## Final Grade: **82 / 100**

### Feedback

[Your feedback paragraphs here]
```

---

## Step 9 — Confirm & Report

Once saved, report:

```
✓ Feedback saved to: reviews/[Assignment]/feedback/[Name].md
  Grade: 82/100
  Status: Ready for Nelson to review / send to student
```

---

## Special Cases

### No Rubric Available

If no rubric exists, proceed with holistic evaluation:
1. Read the submission carefully
2. Evaluate against the assignment description (what was asked)
3. Score 0–100 based on:
   - Does it meet the requirements?
   - Is the quality high?
   - How complete is it?
4. **Include a note:** "Evaluated holistically (no rubric). Consider creating a rubric for consistency."

### Missing File

If Nelson provides an invalid file path:
- Ask for the correct path
- Do not proceed without a readable file

### Group Member Not in Roster

If Nelson says "Grade Group X" but Group X doesn't exist in the roster:
- Ask Nelson to confirm the group name or provide the member list
- Update or create the roster entry before grading

---

## Rules

- **Always use the rubric if it exists** — it ensures consistent grading
- **Every point lost needs a reason** — this helps students understand their score
- **Feedback is for growth** — focus on what they can improve, not what they did wrong
- **Default Spanish** — write feedback in Spanish if courses are taught in Spanish (check context/courses.md)
- **File organization matters** — always save to the correct path so Nelson can find grades later
