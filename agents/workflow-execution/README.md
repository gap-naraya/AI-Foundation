# Workflow Execution Agent

## Purpose
Execute the Thursday morning communication workflow: read transcripts from Google Drive, generate Claude analyses, produce three stakeholder-specific reports, and prepare them for distribution.

## When to Use
Triggered by user message: **"Weekly workflow ready — Week ending [DATE]"**

Example: `"Weekly workflow ready — Week ending June 6"`

## What It Does
1. Accesses Google Drive folder structure for the specified week
2. Reads meeting transcripts (daily standups, client sync, leadership sync)
3. Sends transcripts to Claude for analysis
4. Generates three separate reports:
   - **Weekly Status Report** (for Ken/Shawn) - Executive summary, formal tone
   - **Leadership Update** (for Gerardo) - Operational detail, transparent
   - **Action Items Tracker** (for all) - Table format, factual
5. Prepares for distribution via email/Slack
6. Logs metrics (processing time, summary of findings)

## Expected Output
Three markdown files ready for distribution:
- `Weekly_Status_Report_[DATE].md`
- `Leadership_Update_[DATE].md`
- `Action_Items_Tracker_[DATE].md`

## Status
🔄 **Planned** - Not yet implemented

## How to Use (When Ready)
Simply message: `"Weekly workflow ready — Week ending June 6"`

The agent will:
1. Read current week's transcripts
2. Generate all three reports
3. Prepare them for review before distribution
4. Track processing metrics

## Configuration Needed
- Google Drive folder path pattern
- API credentials for reading Drive files
- Claude API configuration for analysis
- Stakeholder contact lists for distribution

## Key Constraints
- ✅ Read-only access to Google Drive transcripts
- ✅ Human review before any distribution
- ✅ Validation of all outputs before sending
- ✅ Fallback: manual processing if system fails

## Next Steps
1. Finalize Google Drive integration details
2. Create detailed execution prompt
3. Test with first week's actual data (June 6)
4. Refine based on real-world performance
5. Document any adjustments needed

## Reference
See `/Users/naraya/Documents/AI-Foundation/Level3 Evidence/04_AI_System_Design_and_Orchestration.md` for detailed workflow architecture.
