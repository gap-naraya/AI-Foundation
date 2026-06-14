# CENFOTEC-AI-FOUNDATION

A structured system for designing, managing, and grading assignments at Universidad Cenfotec using AI-assisted workflows. This project helps Nelson manage teaching across 4+ courses with consistent rubrics, clear grading criteria, and constructive feedback for students.

---

## Overview

**CENFOTEC-AI-FOUNDATION** is an educational project management system that:

- 📋 **Creates rubrics** for assignments with customizable criteria and point distributions
- 📊 **Grades student work** against consistent rubrics with detailed feedback
- 📁 **Organizes courses** with clear folder structures for assignments and evaluations
- 🌍 **Supports multilingual content** (Spanish/English) tailored to Costa Rican context
- 🤝 **Ensures fair evaluation** through criterion-based grading and consistent standards

---

## Quick Start

### Creating a Rubric

To create a rubric for a new assignment:

```bash
/create-rubric
```

The skill will guide you through:
1. Assignment name and type
2. Total points and evaluation criteria
3. Criteria descriptions (what excellence looks like)
4. Iteration and refinement

**Example:**
```
/create-rubric
> Assignment: Plan General de Proyecto
> Type: Document
> Total points: 100
> Course: Proyecto de Ingeniería del Software 3
```

### Grading Student Work

To review and grade student submissions:

```bash
/review-assignment
```

Provide:
- Submission file path (PDF or Word document)
- Student/Group name
- Course name

The skill will:
1. Read the submission
2. Load the corresponding rubric
3. Evaluate against criteria
4. Generate a grade breakdown with feedback

**Example:**
```
/review-assignment
> Student: Maria García
> File: /path/to/submission.pdf
> Course: Proyecto-3
```

---

## Project Structure

```
CENFOTEC-AI-FOUNDATION/
├── README.md                           ← This file
├── CLAUDE.md                           ← Project instructions & teaching philosophy
├── context/                            ← Configuration & reference files
│   ├── courses.md                     ← Course catalog & details
│   ├── academic-calendar.md           ← Term dates & deadlines
│   ├── student-communication.md       ← Tone & feedback guidelines
│   └── institutional-context.md       ← Cenfotec policies & standards
│
├── courses/                            ← Course-specific content
│   ├── README.md                      ← Course folder guidelines
│   ├── proyecto-3/                    ← Curso: Proyecto Ingeniería del Software 3
│   │   └── assignments/
│   │       └── Plan-General-de-Proyecto/
│   │           ├── INSTRUCTIONS.md    ← Student-facing requirements
│   │           ├── RUBRIC.md          ← Grading criteria
│   │           └── README.md          ← Assignment overview
│   │
│   └── ingenieria-requerimientos/     ← Curso: Ingeniería de Requerimientos
│       └── assignments/
│           └── [future assignments]
│
└── .claude/                            ← Claude Code configuration
    └── skills/
        ├── create-rubric/
        └── review-assignment/
```

---

## Courses

Nelson teaches the following courses at Universidad Cenfotec:

### 1. **Proyecto de Ingeniería del Software 3** (BISOFT-22)
- **Level**: Bachelor in Software Engineering
- **Students**: 25–30
- **Focus**: Software Development Life Cycle & Project Management
- **Folder**: `courses/proyecto-3/`
- **Assignment Types**: Documents, project planning materials

### 2. **Ingeniería de Requerimientos** (BISOFT-28)
- **Level**: Bachelor in Software Engineering
- **Students**: 15–20
- **Focus**: Requirements Engineering in Software Development
- **Folder**: `courses/ingenieria-requerimientos/`
- **Assignment Types**: Requirements documents, specifications

See `context/courses.md` for complete course information.

---

## Creating & Managing Assignments

### Step 1: Create the Assignment Folder

```bash
mkdir -p courses/[course-name]/assignments/[assignment-name]
```

### Step 2: Write Assignment Instructions

Create `INSTRUCTIONS.md` with student-facing requirements:
```markdown
# [Assignment Name]

## Overview
[Brief description]

## Requirements
1. [Requirement 1]
2. [Requirement 2]
...

## Submission Format
[File format, deadline, etc.]
```

### Step 3: Create a Rubric

Say `/create-rubric` and provide:
- Assignment name
- Assignment type (essay, document, project, etc.)
- Total points (default: 100)
- Course folder name

The rubric will be saved to: `courses/[course-name]/assignments/[assignment-name]/RUBRIC.md`

### Step 4: Share with Students

Point students to `INSTRUCTIONS.md` with clear deadlines and submission details.

---

## Grading & Feedback

### Grading Process

1. Collect student submissions (PDF, Word, or other formats)
2. Say `/review-assignment` with the file path
3. Skill loads the rubric and evaluates the submission
4. Returns:
   - **Grade breakdown** (points per criterion)
   - **Total score**
   - **Constructive feedback** (what was done well, areas for improvement)

### Feedback Philosophy

Following Nelson's teaching principles:
- **Constructive** — specific, actionable, encouraging
- **Criterion-based** — grounded in the rubric, not subjective
- **Growth-focused** — highlights what the student can improve for next time
- **Respectful** — never punitive, always professional

---

## Configuration & Context

All course-specific and institutional information is stored in the `context/` folder:

- **courses.md** — Course catalog, levels, student counts, focus areas
- **academic-calendar.md** — Term dates, assignment deadlines, grading periods
- **student-communication.md** — Tone, language, feedback style guidelines
- **institutional-context.md** — University policies, grading scales, compliance rules

**Important:** Always check these files before creating assignments or rubrics to ensure alignment with institutional standards and course-specific requirements.

---

## Best Practices

### For Assignment Design

✅ **Do:**
- Create rubrics with 4–6 clear, balanced criteria
- Ground rubric descriptions in actual assignment requirements
- Include a mix of content, structure, and presentation criteria
- Set realistic point distributions (no criterion should be worth >40% of total)

❌ **Don't:**
- Create rubrics without reviewing the assignment instructions
- Use vague criterion descriptions (e.g., "effort" instead of "depth of analysis")
- Weight one criterion too heavily
- Change rubrics after students have submitted work

### For Grading

✅ **Do:**
- Use the rubric consistently across all submissions
- Provide specific examples from the student's work in feedback
- Highlight both strengths and areas for improvement
- Give students actionable suggestions for next time

❌ **Don't:**
- Grade without consulting the rubric
- Provide generic feedback ("good job" or "needs work")
- Mix subjective opinions with criterion-based scores
- Grade while tired or rushed

### For Communication

✅ **Do:**
- Keep feedback in Spanish for Spanish-taught courses
- Be encouraging and respect the student's effort
- Explain the reasoning behind point deductions
- Invite questions and dialogue

❌ **Don't:**
- Use punitive language
- Make assumptions about student intent
- Ignore institutional communication guidelines
- Rush feedback responses

---

## Workflow Examples

### Example 1: Create & Grade an Essay Assignment

```
1. Create folder:
   mkdir -p courses/proyecto-3/assignments/Research-Essay

2. Write INSTRUCTIONS.md
   (document requirements, format, deadline)

3. Say: /create-rubric
   - Assignment: Research Essay
   - Type: Essay
   - Points: 100
   - Course: proyecto-3
   
4. Iterate on rubric (adjust criteria/points)

5. Students submit work

6. Say: /review-assignment
   - File: /path/to/submission.pdf
   - Student: Carlos Mendez
   - Course: proyecto-3
   
7. Receive graded feedback with breakdown & suggestions
```

### Example 2: Grade a Group Project

```
1. Rubric already exists (created earlier)

2. Students submit group work as PDF

3. Say: /review-assignment
   - File: /path/to/group-submission.pdf
   - Group: Group A
   - Course: proyecto-3
   
4. Receive group feedback (addresses the team collectively)
   - Can be modified before sharing to account for individual contributions
```

---

## Technical Details

### Skills Included

- **`/create-rubric`** — Conversational rubric generator
  - Gathers assignment info
  - Proposes balanced criteria
  - Allows iteration & refinement
  - Saves formatted RUBRIC.md

- **`/review-assignment`** — Student work evaluator
  - Reads submission files
  - Loads the corresponding rubric
  - Evaluates against criteria
  - Generates grade breakdown & feedback

### File Formats

- **INSTRUCTIONS.md** — Assignment requirements (Markdown)
- **RUBRIC.md** — Grading criteria table (Markdown)
- **README.md** — Assignment overview (Markdown)
- **Submissions** — PDF, Word (.docx), or other formats

### Storage

- Rubrics are saved in the assignment folder
- Feedback can be saved separately for record-keeping
- All files are version-controlled in git

---

## Troubleshooting

### "Rubric not found"

The `/review-assignment` skill expects the rubric at:
```
courses/[course-folder]/assignments/[assignment-name]/RUBRIC.md
```

Ensure the folder structure matches exactly (use the same names used when creating the rubric).

### "Assignment instructions are unclear"

Before creating a rubric, review the assignment with students. Include the INSTRUCTIONS.md file when running `/create-rubric` so the rubric grounds criteria in actual requirements.

### "Feedback feels too generic"

When grading, always reference specific examples from the student's work. The skill will improve with more detailed rubric descriptions.

---

## Contributing & Updates

This project evolves as Nelson teaches. To update:

1. **Add a new course** → Update `context/courses.md` and create `courses/[course-name]/` folder
2. **Update institutional context** → Edit `context/institutional-context.md`
3. **Change feedback tone** → Update `context/student-communication.md`
4. **Document lessons learned** → Add notes to this README

---

## Related Projects

- **GAP-AI-FOUNDATION** — Nelson's work on the Growth Acceleration Partners consulting side
- **Root CLAUDE.md** — Shared operating system for both projects (values, principles, tools)

---

## Contact & Support

For questions or improvements to this system, refer to:
- `CLAUDE.md` — Teaching philosophy & instructions
- `context/` — Specific course & institutional details
- `/help` — Claude Code help & resources

---

**Last Updated**: June 2026  
**Maintained by**: Nelson Araya Alvarado  
**Institution**: Universidad Cenfotec, Costa Rica
