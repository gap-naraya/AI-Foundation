# Level 3 Evidence: Capacity to Design and Orchestrate AI-Driven Processes

**Nelson Araya | Mediquant DOM Project | May 2026**

---

## What Level 3 Looks Like

Level 3 demonstrates that you can **design complex, multi-step AI workflows** from scratch, not just use AI as a point tool. At this level:

- **System architecture:** You understand data flows, integration points, and how components connect
- **Tool orchestration:** You choose and combine tools to solve a problem (not just use one tool)
- **Documented design:** The workflow is articulated clearly (so others could implement it)
- **Design justification:** You can explain *why* each choice was made (vs. "this seemed easy")
- **Scalability thinking:** The design would work for variations of the same problem

## The Communication Workflow: Multi-Step System Architecture

This is not "I use Claude to write reports." It's a **designed system** with multiple components that work together:

```
Input Layer
    ↓
    Meeting Transcripts (Teams, Slack)
    ↓
Storage Layer
    ↓
    Google Drive Folder Structure
    /Mediquant Weekly Reports/2026/[Month]/Week_[DATE]/
    ├── Daily_Standups.txt
    ├── Client_Sync.txt
    └── Leadership_Sync.txt
    ↓
Processing Layer (Trigger Point)
    ↓
    Weekly Trigger: "Weekly workflow ready — Week ending [DATE]"
    OR Ad-hoc Trigger: "AD-HOC REPORT - Meeting: [detail], Audience: [stakeholders]"
    ↓
Analysis & Generation Layer
    ↓
    Claude AI processes:
    - Reads all files from current week folder
    - Identifies themes: decisions, risks, blockers, progress
    - Applies audience-specific framing
    - Generates three distinct outputs
    ↓
Validation Layer (Human-in-the-Loop)
    ↓
    Nelson reviews each report:
    - Source Check (did Claude read the right data?)
    - Bias Scan (is framing appropriate for audience?)
    - Contextual Fit (does this match live project reality?)
    ↓
Output Layer
    ↓
    Three Audience-Specific Reports:
    1. Weekly Status Report (client executives)
    2. Leadership Update (manager)
    3. Action Items Tracker (all stakeholders)
    ↓
Distribution Layer
    ↓
    Teams message (formal channels)
    Email (executive stakeholders)
    Drive folder (archived for reference)
```

This is **not** a simple "ChatGPT write me a report" interaction. It's a **system** where:
- Multiple inputs flow through a storage layer
- A trigger activates processing
- AI handles mechanical analysis
- Humans validate before output
- Multiple output formats serve different needs
- Results are distributed appropriately

## Design Decision: Why Each Choice Was Made

The workflow reflects deliberate choices, each justified by requirements:

### Storage: Google Drive (vs. GitHub, Slack, SharePoint)

**Decision:** Google Drive folder structure organized by Year/Month/Week

**Why Google Drive?**
| Factor | Google Drive | GitHub | Slack | SharePoint |
|--------|-------------|--------|-------|-----------|
| **Intuitive folder structure** | ✓ Natural hierarchy | ✗ File paths are code-like | ✗ No hierarchy | ~ Possible but complex |
| **Easy transcript upload** | ✓ Drag-and-drop | ✗ Git commands | ✗ Messages clutter | ✗ Approval workflows |
| **Claude can read files** | ✓ Via Google Drive integration | ✓ Via GitHub API | ✗ Chat-based only | ✓ Via SharePoint API |
| **Familiar to non-technical teams** | ✓ Everyone knows Folders | ✗ Engineers only | ✓ Everyone on Slack | ~ IT manages SharePoint |
| **Search/browse later** | ✓ Easy to navigate | ✓ Good but technical | ✗ Buried in chat history | ~ Possible but slow |
| **Zero learning curve** | ✓ Existing behavior | ✗ New tool | ✓ Existing tool | ~ New tool for most |

**Conclusion:** Google Drive solves the **storage and retrieval problem** without requiring technical sophistication. The workflow needed a place where Nelson could put transcripts that Claude could access without difficulty. Drive fits perfectly.

Alternative considered: GitHub would be more "technical" but would require Nelson to learn git, create branches, and manage files technically. **Overkill for transcript storage.**

### Processing: Claude AI (vs. ChatGPT, Copilot, Custom Script)

**Decision:** Claude AI as the analysis and generation engine

**Why Claude?**
| Factor | Claude | ChatGPT | Copilot | Custom Script |
|--------|--------|---------|---------|---------------|
| **Context awareness** | ✓ Excellent | ~ Good | ~ Medium | ✓ Perfect but requires coding |
| **Multiple output formats** | ✓ Easy (text, markdown, structured) | ✓ Good | ✗ Limited | ✓ Requires custom code |
| **Bilingual capability** | ✓ Spanish/English fluent | ✓ Good | ✓ Good | ✓ If you code it |
| **API integration** | ✓ Clean API | ✓ API available | ~ Limited | N/A (you'd write it) |
| **Audience-specific framing** | ✓ Can maintain multiple voices | ~ Possible with prompting | ~ Limited | ✓ But requires coding |
| **No additional setup** | ✓ Already authenticated | ✓ ChatGPT account | ✓ Microsoft integration | ✗ Requires development |
| **Cost** | $ Reasonable per use | $ Requires API or Plus subscription | Included in Microsoft | 0 but requires time |

**Conclusion:** Claude balances **capability** (everything needed is possible) with **simplicity** (no development required). The integrated Google Drive access meant Claude could read the transcript folder without additional integration work.

Alternative considered: Custom script would give perfect control but would require **ongoing maintenance, testing, and debugging**. The problem (generating reports) is not novel enough to justify custom code.

### Validation: Human-in-the-Loop (vs. Automated or No Validation)

**Decision:** Nelson reviews all reports before sending; specific validation techniques (Source Check, Bias Scan, Contextual Fit)

**Why human-in-the-loop?**

**Automated validation only (no human review):**
- ✓ Faster (human review is bottleneck)
- ✗ No judgment about contextual fit (is this the right message at the right time?)
- ✗ No catch for AI hallucinations or misunderstandings
- ✗ Stakeholders receive unreviewed AI output (reputational risk)
- ✗ Nelson loses visibility into what's being communicated
- **Verdict:** Too risky for executive communication

**No validation (raw AI output):**
- ✓ Fastest (no review)
- ✗ High risk of errors reaching stakeholders
- ✗ Inconsistent quality
- ✗ Nelson has no control over message
- **Verdict:** Unacceptable for professional PM communication

**Human-in-the-loop with structured validation:**
- ✓ Maintains quality and accuracy
- ✓ Nelson stays in control of narrative
- ✓ Catches AI misunderstandings before damage
- ✓ Enables customization for strategic purposes
- ~ Adds 10 min per report (acceptable cost)
- **Verdict:** Right balance of efficiency and safety

**Conclusion:** The 10-minute validation is **not overhead**—it's **essential risk management**. The workflow is designed so that validation happens quickly (because it's structured) but thoroughly (because Nelson knows what to look for).

### Output: Three Distinct Reports (vs. One Generic Report)

**Decision:** Separate reports for client, manager, and action items

**Why three outputs?**

**One generic report for everyone:**
- ✓ Faster to write (one report, not three)
- ✗ Satisfies nobody
- ✗ Executives get too much operational detail
- ✗ Manager gets too much client-facing narrative
- ✗ Action items get buried in context
- **Result:** Stakeholders ignore because it's not tailored to their needs

**Three audience-specific reports:**
- Each stakeholder gets exactly what they need
- Executives see strategic context (value, timeline, decisions)
- Manager sees operational detail (blockers, risks, escalation signals)
- Everyone has clear action items with owners and deadlines
- Slightly more work to generate (but Claude handles it easily)
- **Result:** Higher stakeholder satisfaction, better decisions

**Conclusion:** The extra generation work (10 seconds for Claude) is worth the difference in stakeholder value. This is why **architectural thinking matters**. You're not minimizing the report-generation work; you're optimizing for **stakeholder understanding**.

### Trigger: Message-Based (vs. Scheduled, File-Based, Button-Based)

**Decision:** Nelson sends a simple message ("Weekly workflow ready — Week ending [DATE]") to trigger processing

**Why message trigger?**

**Scheduled (Tuesday at 9am automatically):**
- ✓ Truly automatic (no user action)
- ✗ Not flexible (what if meeting schedule changes?)
- ✗ No human decision point (what if data is incomplete?)
- ✗ Runs whether or not Nelson is ready
- **Result:** Risk of processing incomplete data

**File-based (upload a "trigger.txt" to Drive):**
- ✓ Integrated with storage layer
- ✗ Awkward UX (have to create a file?)
- ✗ Not clear whether it worked
- ✗ No confirmation before processing

**Button-based (click a button in app):**
- ✓ Clear action
- ✗ Requires application/interface
- ✗ Additional setup and maintenance
- ✗ Learning curve for users

**Message-based (send a text message):**
- ✓ Low friction (just send a message)
- ✓ Natural confirmation (message confirms you did it)
- ✓ Flexible (can send anytime, not just Tuesday)
- ✓ No additional tools needed
- ✓ Nelson makes conscious decision to trigger
- **Result:** Good UX, flexibility, human judgment retained

**Conclusion:** The message-based trigger is **intentionally simple**. It keeps the human in control (you decide when to trigger) while making the activation trivial.

## Orchestration: How Components Work Together

The workflow doesn't just use individual tools—it **orchestrates them** to solve a problem:

### Weekly Workflow Orchestration

```
1. INPUT: Throughout the week, Nelson saves transcripts
   - Teams meetings → Daily_Standups.txt
   - Client sync → Client_Sync.txt
   - Leadership meetings → Leadership_Sync.txt
   - All stored in Google Drive folder

2. TRIGGER: Thursday morning, Nelson sends:
   "Weekly workflow ready — Week ending June 6"

3. PROCESSING: Claude AI (orchestrated by human instruction)
   - Reads all files from Week_06-07 folder
   - Identifies key themes from each file
   - Synthesizes across files (what patterns emerge?)
   - Applies audience-specific framing
   - Generates three distinct outputs simultaneously

4. VALIDATION: Nelson reviews each report
   - Checks facts against source material
   - Assesses tone and framing
   - Confirms alignment with strategic priorities
   - Notes any edits needed

5. DISTRIBUTION: Nelson sends to stakeholders
   - Teams message for client execs
   - Email for Gerardo
   - Drive folder for archived reference

6. FOLLOW-UP: Nelson notes metrics
   - Time spent this week: __ minutes
   - Ad-hoc reports triggered: __ count
   - Strategic work time available: __ hours
```

Each step depends on the previous one. Claude can't process without transcripts. Distribution can't happen without validation. The workflow is **interdependent**, not just sequential.

### Ad-Hoc Workflow Orchestration

```
TRIGGER: Unplanned situation
Nelson sends: "AD-HOC REPORT - Meeting: [what happened], Audience: [Ken/Shawn, Gerardo, or Both]"

PROCESSING: Claude (rapid)
- Scans current week folder (all files)
- Includes data from the ad-hoc meeting (Nelson mentions specifics in trigger)
- Synthesizes what's new vs. what was already known
- Generates custom report for specified audience

VALIDATION: Nelson (quick)
- Skim report for accuracy
- Confirm tone is appropriate
- Customization if needed

DISTRIBUTION: Immediate
- Teams message or direct email
- Urgent stakeholders get notified
```

This is **lighter weight** than the weekly workflow because it's responsive to real urgency. The system adapts to both routine (Thursday weekly) and exceptional (ad-hoc urgent) situations.

## Scalability: How This Design Works for Other PM Tasks

The workflow was intentionally designed to be **generalizable**:

**Pattern:** Data Collection → Processing → Audience-Specific Output → Validation → Distribution

This same pattern could solve other PM problems:

**Example 1: Sprint Retrospectives**
- Collection: Standups + team feedback from Retro meeting
- Processing: Claude identifies themes (what went well, blockers, improvements)
- Output: Retro summary + action items for next sprint
- Validation: Team reviews before sharing
- Distribution: Documented for future reference

**Example 2: Escalation Reports**
- Collection: Issue description + context from emails + resolution steps
- Processing: Claude creates executive summary + technical detail + timeline
- Output: Executive escalation summary + technical deep-dive
- Validation: Nelson reviews accuracy + tone
- Distribution: Client and internal leadership

**Example 3: Project Health Dashboards**
- Collection: Weekly metrics (velocity, burn-down, blockers, risks)
- Processing: Claude analyzes trends + identifies concerns + generates commentary
- Output: Executive dashboard + detailed analysis + risk register updates
- Validation: Nelson confirms accuracy
- Distribution: Stakeholder reports

**Why this matters for Level 3:** You've designed a **reusable architecture**, not just solved one specific problem. This demonstrates **scalable thinking**—the ability to see a pattern and apply it broadly.

## Design Documentation: How Others Could Implement This

The workflow is **documented well enough for others to implement**:

### For Another PM to Use This Workflow

**Required inputs:**
1. Google Drive folder with transcripts organized by week
2. Clear trigger message (message text)
3. Three audience definitions (who is client? manager? all-hands?)

**Required systems:**
1. Google Drive access (free, everyone has it)
2. Claude AI access (API authentication)
3. No additional tools needed

**Process steps:**
1. Follow the weekly trigger (message Claude on Thursday)
2. Receive three reports
3. Review using validation checklist
4. Send to stakeholders

**Success metrics:**
1. Reports arrive by Thursday morning
2. Stakeholders report reports are useful
3. Time spent <70 min/week

### For Engineering to Scale This Workflow

**Architecture for broader deployment:**
1. Templated Google Drive structure (could be created automatically)
2. Standard Claude prompt (could be stored in shared docs)
3. Validation checklist (could be checklist app or doc)
4. Metrics dashboard (could be shared sheet)

**Scaling considerations:**
- Multiple PMs using same pattern (different projects, same structure)
- Shared prompt templates (consistency across teams)
- Centralized validation (could be peer-review rather than self-review)
- Automated metrics collection (could track time across multiple users)

**Why this matters:** The design is not "magic." It's a **repeatable process** that other people could implement.

## Why This Exceeds Level 2

**Level 2** would be:
- "I use Claude to help write reports"
- One tool, simple prompt, minimal documentation
- No integration with other systems
- No validation process
- No measurement framework

**Level 3** is:
- **Multi-step system architecture** (storage → processing → validation → distribution)
- **Orchestrated components** (Google Drive + Claude + validation + measurement)
- **Deliberate design decisions** (why Google Drive? why three reports? why message trigger?)
- **Documented workflows** (weekly + ad-hoc, both fully specified)
- **Scalable pattern** (could be applied to other PM problems)
- **Human judgment integrated** (validation, strategic customization, timing decisions)
- **Measurement built in** (metrics collection, ongoing improvement)

This demonstrates **architectural thinking**. You didn't just use AI; you **designed a system that uses AI as one component in a larger process**.

---

## Supporting Materials

**System Architecture Diagram (Detailed):**

```
WEEKLY WORKFLOW
┌─────────────────┐
│  Input: Transcripts
│  (Daily, throughout week)
│  - Teams meetings
│  - Slack conversations
│  - Notes from meetings
└────────────┬────┘
             │
             ↓
┌─────────────────┐
│  Storage Layer
│  Google Drive/2026/Month/Week_XX/
│  - Daily_Standups.txt
│  - Client_Sync.txt
│  - Leadership_Sync.txt
└────────────┬────┘
             │
             ↓
┌─────────────────────────────┐
│ Trigger: Thursday Morning   │
│ Message: "Weekly workflow   │
│ ready — Week ending [DATE]" │
└────────────┬────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Processing Layer: Claude AI          │
│ - Read all files from current week   │
│ - Identify themes & key points       │
│ - Apply audience framing             │
│ - Generate three report versions     │
└────────────┬─────────────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Validation Layer: Nelson             │
│ - Source Check                       │
│ - Bias Scan                          │
│ - Contextual Fit                     │
│ - Customization if needed            │
└────────────┬─────────────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Output: Three Reports                │
│ 1. Weekly Status (Client)            │
│ 2. Leadership Update (Manager)       │
│ 3. Action Items (All)                │
└────────────┬─────────────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Distribution                         │
│ - Teams messages to clients          │
│ - Email to Gerardo                   │
│ - Drive archive for reference        │
└──────────────────────────────────────┘


AD-HOC WORKFLOW
┌─────────────────────────────┐
│ Trigger: Unplanned Situation│
│ Message: "AD-HOC REPORT -   │
│ Meeting: [detail]           │
│ Audience: [who]"            │
└────────────┬────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Processing Layer: Claude (Rapid)     │
│ - Scan current week folder           │
│ - Include new context from trigger   │
│ - Generate for specified audience    │
└────────────┬─────────────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Quick Validation: Nelson             │
│ - Check accuracy                     │
│ - Confirm tone                       │
└────────────┬─────────────────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│ Immediate Distribution               │
│ - Teams or Email to urgent audience  │
└──────────────────────────────────────┘
```

**Design Decision Matrix (All Choices Documented):**

| Component | Choice | Alternatives Considered | Why This One |
|-----------|--------|------------------------|-------------|
| Storage | Google Drive | GitHub, Slack, SharePoint | Intuitive + no learning curve |
| Processing | Claude AI | ChatGPT, Copilot, Script | Context + capability + ease |
| Validation | Human review | Automated, None | Risk management + quality control |
| Output | 3 reports | 1 generic report | Stakeholder-specific value |
| Trigger | Message | Scheduled, File, Button | Flexibility + control + simplicity |

---

## Next Steps: Demonstrating Scalability

- **June 2-6:** First implementation (weekly + ad-hoc)
- **June 9+:** Document workflow exactly (for others to follow)
- **July:** Identify a second PM task that could use this pattern
- **August:** Design variation of workflow for different PM problem
- **September:** Document how the pattern generalizes (scalability proof)

The Level 3 case is complete when you can show: "I designed a system that solves one problem (communication reports) in a way that could be applied to other problems (retrospectives, escalations, dashboards, etc.)." That's **architectural thinking**.
