# Courses Directory

This folder contains course-specific files for Nelson's Cenfotec teaching.

---

## File Structure

For each course, create a subfolder with:

```
courses/
├── [Course-Name]/
│   ├── roster.md           ← Student groups (which students work together)
│   ├── rubric-[assignment].md  ← Rubric for each assignment (created by create-rubric skill)
│   └── ...
```

---

## roster.md Format

Create a roster file to define which students belong to which group. This is used by the `review-assignment` skill to assign grades to the correct students.

**Example:**

```markdown
# Course: Software Development 101

## Group A
- María García
- Carlos Rodríguez
- Ana López

## Group B
- José Martínez
- Laura Sánchez

## Individual Students (no group)
- Pedro Jiménez
```

**Important:** Keep group names consistent when you reference them in feedback files.

---

## rubric-[assignment].md Format

Rubrics are created by the `create-rubric` skill and saved automatically. They follow this format:

```markdown
# [Assignment Name] — Rubric

Total Points: 100

| Criterion         | Max Points | Description                        |
|-------------------|------------|------------------------------------|
| Content depth     | 30         | Coverage and accuracy of concepts  |
| Structure         | 20         | Organization, flow, and clarity    |
| Sources/Evidence  | 20         | Use of references and examples     |
| Presentation      | 15         | Formatting, visuals, delivery      |
| Conclusions       | 15         | Quality of final analysis          |
```

Each criterion must have:
1. **Name** — what is being evaluated
2. **Max Points** — the maximum possible for this criterion
3. **Description** — what excellence looks like for this criterion

---

## Creating a Rubric

Say: **"create rubric for [Assignment Name]"**

The `create-rubric` skill will:
1. Ask for assignment type (essay, presentation, etc.) and total points
2. Propose a 4–6 criterion rubric
3. Let you adjust criteria and point values
4. Save to `courses/[Course-Name]/rubric-[Assignment-Name].md`

---

## Using a Rubric for Grading

Say: **"grade Group A"** or **"review [StudentName]'s assignment"**

Provide:
- File path to the submission (PDF or Word document)
- Group name OR student name
- Course name (so Claude can find the roster if needed)

The `review-assignment` skill will:
1. Read the submission file
2. Load the rubric (if it exists)
3. Produce a grade breakdown with:
   - Points earned per criterion
   - Points lost (with reason)
   - Final grade
   - Written feedback

---

## Example Workflow

1. **Create rubric**: "create rubric for Final Essay, 100 points"
   - Saves to: `courses/Software-Dev-101/rubric-Final-Essay.md`

2. **Create roster** (if not done yet):
   - Save manually to: `courses/Software-Dev-101/roster.md`

3. **Grade Group A**: "grade Group A's essay submission" + provide file path
   - Saves feedback to: `reviews/Final-Essay/feedback/GroupA.md`
   - Includes: member list, grade breakdown, final grade, feedback

4. **Grade individual student**: "review Maria's essay" + provide file path
   - Saves feedback to: `reviews/Final-Essay/feedback/Maria.md`
   - Includes: grade breakdown, final grade, personalized feedback
