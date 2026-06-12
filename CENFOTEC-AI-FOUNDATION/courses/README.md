# Courses Directory

This folder contains course-specific files for Nelson's Cenfotec teaching.

---

## File Structure

For each course, create a subfolder with:

```
courses/
├── [Course-Name]/
│   ├── rubric-[assignment].md  ← Rubric for each assignment (created by create-rubric skill)
│   └── ...
```

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

Optionally provide the assignment instructions document (PDF or Word) so the rubric is grounded in the actual assignment requirements.

The `create-rubric` skill will:
1. Ask for assignment type (essay, presentation, etc.) and total points
2. If you provided instructions, read them and extract key requirements
3. Propose a 4–6 criterion rubric (grounded in actual requirements, or generic if no instructions)
4. Let you adjust criteria and point values
5. Save to `courses/[Course-Name]/rubric-[Assignment-Name].md`

---

## Using a Rubric for Grading

Say: **"grade [Group Name]"** or **"review [StudentName]'s assignment"**

Provide:
- File path to the submission (PDF or Word document)
- Subject name (group name or student name)
- Course name

The `review-assignment` skill will:
1. Read the submission file
2. Load the rubric (if it exists)
3. Evaluate against the rubric (or holistically if none exists)
4. Produce a grade breakdown with:
   - Points earned per criterion
   - Points lost (with reason)
   - Final grade
   - Written feedback

---

## Example Workflow

1. **Create rubric**: "create rubric for Final Essay, 100 points"
   - Optionally provide the assignment instructions document
   - Saves to: `courses/Software-Dev-101/rubric-Final-Essay.md`

2. **Grade submissions** (same workflow for groups or individuals):
   
   **Group submission:**
   - Say: "grade Group A's essay submission" + provide file path
   - Saves feedback to: `reviews/Final-Essay/feedback/Group-A.md`
   - Includes: grade breakdown, final grade, feedback
   
   **Individual submission:**
   - Say: "review Maria's essay" + provide file path
   - Saves feedback to: `reviews/Final-Essay/feedback/Maria.md`
   - Includes: grade breakdown, final grade, personalized feedback

Both use the same evaluation process — the only difference is the subject name.
