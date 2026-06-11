---
name: eod-report
description: Use this skill when the user says "eod", "end of day", "run eod", "generate status report", "daily report", or anything that implies generating a daily project status update for the Mediquant DOM project. Triggers on "eod helper", "status update", "run the helper", or similar phrases.
---

# EoD Report Skill

When this skill is triggered:

1. Read `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/helpers/eod-report.md` for format rules, voice rules, and working sequence.
2. Read `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/eod-report.context.md` for project context (workstreams, stakeholders, acronyms).
3. Read `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/eod-report.previous.md` for yesterday's snapshot (slippage detection).
4. Read `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/client-email-template.html` for the HTML email template.

## Date rule (CRITICAL)
Always date reports for **tomorrow**, not today. Nelson schedules both to send early the next morning.
- Increment today's date by one day
- **Verify the day of the week** before generating (calculate it, do not assume)
- Format: `Mon DD, YYYY` (e.g., `Jun 12, 2026`)
- Apply this to BOTH the Slack message header and email subject/body

## Default behavior
Generate both outputs without being asked:
- **STANDARD** (Slack) — internal format with emojis, progress %, status labels
- **CLIENT EMAIL** (HTML) — formal, client-facing, rendered using the HTML template

## After the report is approved
- Send STANDARD via Slack DM to Nelson (user ID: U06M0L66W5P)
- Create Gmail draft for client email (To: Shawn Fergason, Ken Manley; Cc: Milagro, Matt, Steven)
- Update `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/eod-report.previous.md` with today's snapshot

Follow all format, voice, and content rules from `helpers/eod-report.md` exactly.