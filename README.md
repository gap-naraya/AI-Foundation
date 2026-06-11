# AI-Foundation — Dual Operating Systems

Nelson Araya's **Claude OS** — a dual-project structure managing work at Growth Acceleration Partners (GAP/Mediquant) and teaching at Universidad Cenfotec, with shared foundational rules and isolated project contexts.

---

## Architecture Overview

```
AI-Foundation/                                    ← GitHub repo root
├── CLAUDE.md                                    ← SHARED: hard rules + Nelson's identity
├── README.md                                    ← This file
├── GAP-AI-FOUNDATION/                           ← OS 1: Mediquant project
│   ├── CLAUDE.md                                GAP-specific instructions
│   ├── context/                                 Who Nelson is as a PM (5 files)
│   ├── helpers/                                 Reusable EoD report tools
│   ├── projects/
│   │   ├── mediquant/                           Daily status, client email, snapshots
│   │   └── ai_impact_evaluation/                Level 3 portfolio evidence
│   └── .claude/skills/                          4 GAP-only skills
│       ├── eod-report/
│       ├── escalate-gerardo/
│       ├── draft-message/
│       └── level3-portfolio/
└── CENFOTEC-AI-FOUNDATION/                      ← OS 2: Teaching (NEW)
    ├── CLAUDE.md                                Teaching-specific instructions
    ├── context/                                 Teaching context (4 stub files)
    │   ├── courses.md                           Courses, subjects, levels
    │   ├── student-communication.md             How to write feedback
    │   ├── academic-calendar.md                 Semester dates, deadlines
    │   └── institutional-context.md             Grading scale, policies
    ├── courses/                                 Course rosters and rubrics
    │   └── README.md                            Conventions and formats
    ├── reviews/                                 Grade feedback files (created at runtime)
    └── .claude/skills/                          2 Cenfotec-only skills (NEW)
        ├── create-rubric/                       Generate rubrics
        └── review-assignment/                   Grade with breakdown + feedback
```

---

## How It Works

### File Loading Cascade

When you open a project folder in Claude Code, it loads CLAUDE.md files in this order:

**In GAP-AI-FOUNDATION:**
1. `/Users/naraya/Documents/AI-Foundation/CLAUDE.md` (shared: hard rules + identity)
2. `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/CLAUDE.md` (GAP-specific context)

**In CENFOTEC-AI-FOUNDATION:**
1. `/Users/naraya/Documents/AI-Foundation/CLAUDE.md` (shared: hard rules + identity)
2. `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/CLAUDE.md` (Cenfotec-specific context)

**Result:** Hard rules and Nelson's identity apply everywhere. Domain-specific context loads only when relevant.

### Skills Isolation

- GAP skills (eod-report, escalate-gerardo, draft-message, level3-portfolio) **only activate in GAP-AI-FOUNDATION**
- Cenfotec skills (create-rubric, review-assignment) **only activate in CENFOTEC-AI-FOUNDATION**
- No skill bleeding between projects

### Context-Switching in VS Code

1. **To work on GAP/Mediquant**: Open `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/` in VS Code
2. **To work on Cenfotec/Teaching**: Open `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/` in VS Code

Each folder is a separate project — only its skills and context are available.

---

## Shared Foundation (Root CLAUDE.md)

The root `CLAUDE.md` contains:

1. **Hard Rules** — apply everywhere
   - Do not assume prior knowledge
   - Drive decisions by data
   - Ask clarifying questions

2. **Nelson's Identity** — who he is (unchanged across domains)
   - Core values: empathy, loyalty, presence, teamwork
   - Operational principles: the Pause, courageous proactivity, the Black List
   - Vision: reliable pillar of support for loved ones

---

## GAP-AI-FOUNDATION — Mediquant Project

**Purpose:** Senior PM at GAP, managing critical Mediquant DOM automation project.

**Context files:**
- 2026 Goals Context
- Career Context
- Communication Style (audience matrix)
- Business Context

**Skills:**
- `/eod` — Daily status report (Slack + client email)
- `/escalate-gerardo` — Escalation to manager
- `/draft-message` — Professional communication drafting
- `/level3-portfolio` — AI maturity certification evidence

**Projects:**
- `projects/mediquant/` — daily reporting, client templates, snapshots
- `projects/ai_impact_evaluation/` — Level 3 evidence log

---

## CENFOTEC-AI-FOUNDATION — Teaching (NEW)

**Purpose:** University instructor at Cenfotec, designing and grading student assignments.

**Context files (stubs — fill as needed):**
- `courses.md` — list your courses, subjects, academic levels
- `student-communication.md` — how you write feedback to students
- `academic-calendar.md` — semester structure and deadlines
- `institutional-context.md` — grading scale and policies

**Skills:**
- `/create-rubric` — generate assignment rubrics (conversational)
- `/review-assignment` — grade student work with score breakdown + feedback

**Workflow:**
1. Create a rubric for an assignment → saved to `courses/[Course]/rubric-[Assignment].md`
2. Create a roster file listing student groups → saved to `courses/[Course]/roster.md`
3. Review a student/group submission → saved to `reviews/[Assignment]/feedback/[Name].md`

**Output:**
- Grade breakdown table (criterion → max points → lost → reason)
- Final grade (e.g., 82/100)
- Written feedback (strengths, areas to improve, next steps)

---

## Getting Started

### If you're new to Cenfotec:

1. Open `CENFOTEC-AI-FOUNDATION/` in VS Code
2. Fill in the 4 context files with your teaching info
3. Use `/create-rubric` to build your first rubric
4. Use `/review-assignment` to grade student work

### If you're working on GAP/Mediquant:

1. Open `GAP-AI-FOUNDATION/` in VS Code
2. All existing skills work as before (paths updated to new locations)
3. Use `/eod` for daily status, `/draft-message` for communications, etc.

---

## Key Files & Paths

| Need | Location |
|---|---|
| Shared rules & identity | `/Users/naraya/Documents/AI-Foundation/CLAUDE.md` |
| GAP project context | `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/CLAUDE.md` |
| Cenfotec teaching context | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/CLAUDE.md` |
| My courses info | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/context/courses.md` |
| My feedback style | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/context/student-communication.md` |
| Student rosters | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/roster.md` |
| Assignment rubrics | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/courses/[Course-Name]/rubric-[Assignment].md` |
| Student feedback | `/Users/naraya/Documents/AI-Foundation/CENFOTEC-AI-FOUNDATION/reviews/[Assignment]/feedback/[Name].md` |

---

## GitHub & Version Control

- **Single repo**: `AI-Foundation/` on GitHub
- **Two isolated projects**: GAP-AI-FOUNDATION/ and CENFOTEC-AI-FOUNDATION/
- All changes tracked together; can view history per project

---

## Updates & Maintenance

- **Root CLAUDE.md**: Update when your core values, hard rules, or identity changes (rarely)
- **Project CLAUDE.md**: Update when project context shifts (e.g., new stakeholders, new goals)
- **Context files**: Update as your courses, calendar, or communication style evolves
- **Skills**: Create new skills as you build new tools (e.g., a grading template, rubric builder)

---

## Questions?

- **How do I add a new Cenfotec course?** → Edit `context/courses.md` and create a `courses/[Course-Name]/` folder with `roster.md` and rubrics
- **How do I switch between projects?** → Close one VS Code window, open the other project folder
- **How do I update my feedback style?** → Edit `CENFOTEC-AI-FOUNDATION/context/student-communication.md`
- **How do I create a rubric?** → Say "create rubric for [Assignment Name]" in CENFOTEC-AI-FOUNDATION context
- **How do I grade student work?** → Say "review [Student Name]'s assignment" or "grade Group A" (file path required)
