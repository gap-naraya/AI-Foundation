---
name: review-assignment
description: Use this skill when the user wants to grade student work. Triggers on "grade Group [Name]", "review [Student Name]'s assignment", "evaluate submission", "give feedback on", or similar phrases.
---

# Review Assignment Skill

When triggered, read a student or group submission, apply the rubric (if one exists), and produce a graded feedback file with a grade breakdown and written feedback.

---

## Step 1 — Auto-Discover Courses, Assignments & Submissions

This step auto-discovers available courses, assignments, and submission files, then asks for only the subject name.

### Step 1a — Discover and Select Course

Run:
```bash
find /Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses \
  -mindepth 1 -maxdepth 1 -type d ! -name ".gitkeep"
```

Parse the output into course folder names. Present as a numbered list:

```
Which course is this for?
1. ingenieria-requerimientos
2. proyecto-3
```

If 0 results → error: "No courses found under courses/. Check the folder structure."

Store the selected course as: `COURSE`

---

### Step 1b — Discover and Select Assignment

Run:
```bash
find /Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[COURSE]/assignments \
  -mindepth 1 -maxdepth 1 -type d
```

Parse the output into assignment folder names. Present as a numbered list:

```
Which assignment?
1. plan-general-de-proyecto
```

If 0 results → error: "No assignments found for [COURSE]. Create a folder under courses/[COURSE]/assignments/."

If 1 result → auto-select it and confirm with Nelson.

Store the selected assignment as: `ASSIGNMENT`

---

### Step 1c — Discover and Select Submission File

Run:
```bash
find /Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/submissions/[ASSIGNMENT] \
  -maxdepth 1 -type f \( -iname "*.pdf" -o -iname "*.docx" -o -iname "*.doc" \)
```

**If the submissions/[ASSIGNMENT] folder does not exist or is empty:**

```
No submission files found for [ASSIGNMENT].

Create the folder and drop your submission files:
  /Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/submissions/[ASSIGNMENT]/

Then run the skill again.
```

Stop and wait for Nelson to create the folder and drop files in it.

**If 1+ files exist:**

Present as a numbered list:

```
Which submission file?
1. Grupo-A.pdf
2. Grupo-B.pdf
```

If 1 file → auto-select it and confirm.

Store the full path to the selected file as: `SUBMISSION_FILE`

---

### Step 1d — Ask for Subject Name (Manual Input Only)

Ask Nelson:
```
¿Cuál es el nombre del sujeto? (ej: Grupo A, María García)
```

Store as: `SUBJECT_NAME`

---

### Step 1e — Confirmation Summary

Before proceeding to grading, display a summary for Nelson to confirm:

```
=== Confirmación ===
Curso:      [COURSE]
Entregable: [ASSIGNMENT]
Archivo:    [SUBMISSION_FILE]
Sujeto:     [SUBJECT_NAME]

¿Procedemos? (sí / no)
```

If Nelson says "no" → stop and ask him to re-run the skill.

If Nelson says "sí" → proceed to Step 3.

---

## Step 3 — Read the Submission

Load:
- **Submission file** (PDF or Word) → extract and read the full content
- **Rubric** (if exists) → load from `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/assignments/[Assignment-Name]/RUBRIC.md`

If no rubric exists, proceed with holistic evaluation (0–100 scale with disclaimer).

---

## Step 4 — Evaluate the Submission

1. Evaluate the submission against the rubric (or holistically if no rubric)
2. Calculate grade breakdown (see format below)
3. Write personalized feedback for the subject

---

## Step 5 — Create Grade Breakdown Table

Produce a table showing:
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

```
/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/reviews/[COURSE]/[ASSIGNMENT]/feedback/[SubjectName].md
```

Create the `reviews/[COURSE]/[ASSIGNMENT]/feedback/` folder if it doesn't exist.

---

## Step 8 — File Format

**Feedback file structure:**

```markdown
# [Assignment Name] — [Subject Name]

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
✓ Feedback saved to: reviews/[COURSE]/[ASSIGNMENT]/feedback/[SubjectName].md
  Grade: 82/100
  Status: Ready for Nelson to review / send to student
```

---

## Special Cases

### Submissions Folder Missing or Empty

If the `submissions/[ASSIGNMENT]/` folder does not exist or contains no PDF/docx files, the skill will display:

```
No submission files found for [ASSIGNMENT].

Create the folder and drop your submission files:
  /Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/submissions/[ASSIGNMENT]/

Then run the skill again.
```

**How to use:**
1. Create the folder: `submissions/[assignment-slug]/` (use the same slug as the assignment folder name)
2. Drop all submission PDF or Word files into it (one per student/group)
3. Run the skill again — it will now list the files

File names become the default subject name (e.g., `Grupo-A.pdf` → subject: "Grupo A"). Nelson can confirm or change this in Step 1d.

---

### No Rubric Available

If no rubric exists for the selected assignment, proceed with holistic evaluation:
1. Read the submission carefully
2. Evaluate against the assignment description (what was asked)
3. Score 0–100 based on:
   - Does it meet the requirements?
   - Is the quality high?
   - How complete is it?
4. **Include a note:** "Evaluated holistically (no rubric). Consider creating a rubric for consistency."

---

### Invalid File Selection

If the selected file is unreadable or corrupted:
- Ask Nelson to check the file
- Offer to select a different file from the submissions/ folder
- Do not proceed without a readable file

---

## Rules

- **Always use the rubric if it exists** — it ensures consistent grading
- **Every point lost needs a reason** — this helps students understand their score
- **Feedback is for growth** — focus on what they can improve, not what they did wrong
- **Default Spanish** — write feedback in Spanish if courses are taught in Spanish (check context/courses.md)
- **File organization matters** — always save to the correct path so Nelson can find grades later
