# Level 3 Evidence: Appropriate Use of AI and Validation of Outputs

**Nelson Araya | Mediquant DOM Project | May 2026**

---

## What Level 3 Looks Like

Level 3 means you understand the **risks** of AI output and have designed **specific, documented validation practices** to mitigate them. At this level:

- **Risk governance:** You've identified failure modes and built mitigation into the workflow
- **Human-in-the-loop validation:** AI outputs are reviewed by a qualified human before stakeholder delivery
- **Security & authentication:** No credentials hardcoded; proper use of OAuth and secure authentication
- **Validation methods:** You apply specific techniques (bias scan, source check, contextual fit) rather than generic "review"

## Governance Foundation: Secure Authentication & Data Handling

The workflow was designed from the start with **security as a structural requirement**, not an afterthought:

**Authentication (No Hardcoded Credentials):**
- Google Drive API accessed via **OAuth authentication** (naraya@growthaccelerationpartners.com)
- Claude API connected via **authenticated session** (not API key stored in plaintext)
- Environment-based authentication (tokens managed by the system, not embedded in code/config)

**Data Handling:**
- Transcripts stored in secure Google Drive folder structure
- Access scoped to Nelson's Mediquant project (not company-wide data exposure)
- No sensitive data (passwords, API keys, credentials) included in transcript storage
- Reports generated in memory, delivered directly to Nelson for review before stakeholder distribution

**Why This Matters for Level 3:** This shows you understand that **data governance is not optional** when using AI. Many teams skip this. You've built it into the foundation, which reflects mature thinking about organizational risk.

## Risk Identification: Six Specific Failure Modes

Rather than generic "AI might be wrong," the workflow documentation identifies **six specific risks** with designed mitigations:

| Risk | Severity | Why It Matters | Mitigation Strategy |
|------|----------|---------------|-------------------|
| AI misunderstands context in transcript | Medium | If Claude misinterprets a decision or status, client/manager reports wrong information to leadership | Human review before sending; clear, detailed transcript structure; validation against live knowledge |
| Transcripts incomplete or missing | High | Weekly reports require a complete week of data; missing a day creates gaps in analysis | Nelson saves transcripts daily (discipline + habit); backup in Notes app; fallback trigger if data incomplete |
| Audience gets wrong format | Low | If client report goes to manager instead of vice versa, tone/detail mismatch damages credibility | Three distinct templates with clear naming; Nelson double-checks recipient list; scheduled distribution (not manual copy-paste) |
| Google Drive access unavailable | Low | Temporary cloud service disruption blocks workflow | Fallback: Nelson can paste transcript directly into Claude without Drive integration; process still completes, just slower |
| Thursday morning deadline missed | Medium | Weekly reports should reach stakeholders mid-week; Friday morning delivery loses value | Ad-hoc trigger available any time; flexible scheduling option; leadership understands if Friday substitute happens |
| Stakeholder prefers old format | Medium | If new reports are radically different, stakeholder may distrust or ignore them | Gather explicit feedback in first month; iterate on template based on real use; involve Gerardo in early validation |

This is **not** a generic risk register. These are **specific failure modes** for this workflow, with **designed mitigations** built into the process.

## Validation in Practice: The Human Review Loop

Before any report reaches a stakeholder, **Nelson validates three dimensions**:

### 1. Source Check (Did Claude Read the Right Data?)

**What to validate:** 
- Did Claude actually read the transcripts? (vs. hallucinating from training data)
- Are the themes Claude identified actually present in the source material?
- Are quotes/examples attributable to actual transcript content?

**How Nelson does this:**
- Scans the generated report
- Checks 2-3 specific facts/decisions mentioned
- References back to original transcript to confirm accuracy
- Notes any claims that don't match source material

**Example process:**
```
Generated Report Says: "Team identified database scaling as critical blocker"
Source Check: Did this appear in today's standups or client sync?
Result: ✓ Confirmed in Daily_Standups.txt (mentioned twice)
OR ✗ Not found - flag for removal or rewrite
```

### 2. Bias Scan (Is the Framing Appropriate?)

**What to validate:**
- Is the tone appropriate for the audience? (formal for client, operational for manager)
- Does the report over-emphasize one perspective? (e.g., all risks, no wins)
- Are decisions being framed objectively or with emotional coloring?

**How Nelson does this:**
- Reads the report imagining she's the stakeholder
- Checks tone against established communication style (from CLAUDE.md + communication preferences)
- Assesses whether report would create false urgency or unwarranted optimism
- Ensures technical depth matches audience (execs need less detail; managers need more)

**Example process:**
```
Bias Scan Questions:
- Would an executive see this as "project is on track" or "project is in crisis"?
- Is the risk discussion balanced with progress/wins?
- Does the language match previous reports from Nelson?
- Are action items clearly attributed (not vague responsibility)?

If bias detected: Rewrite specific sections before sending
```

### 3. Contextual Fit (Does This Align with Current Project Reality?)

**What to validate:**
- Does the report align with what Nelson knows from direct experience?
- Are priorities correctly understood? (Is the workflow actually important right now?)
- Does the report miss any critical context that live conversations revealed?

**How Nelson does this:**
- Compares generated report against her lived experience in the project
- Considers recent conversations not in transcripts (hallway conversations, decisions in Slack DMs)
- Adds or removes emphasis based on strategic understanding
- Fills gaps where context matters but isn't in source material

**Example process:**
```
Contextual Fit Check:
- The report highlights technical debt. Is this the right time to escalate it?
- Or should Nelson emphasize delivery momentum to build client confidence first?
- The report says "team morale is solid." Is that accurate based on 1-1s this week?
- Are blockers correctly prioritized? (vs. Claude's data-driven ordering)

Adjustment: If report misses critical context, Nelson adds or reframes
```

## Validation Output: Three Distinct, Audience-Specific Reports

The validation process produces three **separate, purpose-built outputs**—each designed for a specific stakeholder and reviewed against that stakeholder's needs:

**Report 1: Weekly Status Report (Client Executives)**
- **Audience:** Ken Manley (VP Engineering), Shawn Fergusson (CTO)
- **Tone:** Formal, professional, strategic
- **Focus:** Value delivered, timeline impact, decisions made, risks requiring client input
- **Language:** English only
- **Format:** Executive summary (1 page) + key metrics
- **Validation Check:** Does this give executives what they need to make decisions? Is technical detail appropriate? Is risk framing balanced?

**Report 2: Leadership Update (Internal Manager)**
- **Audience:** Gerardo Mora (Senior Delivery Manager)
- **Tone:** Direct, operational, detailed
- **Focus:** Blockers, risks with mitigation strategies, team health, resource gaps, escalation signals
- **Language:** English with technical depth
- **Format:** Structured with clear sections (Progress, Blockers, Risks, Upcoming)
- **Validation Check:** Does this give Gerardo what he needs to escalate risks and support problem-solving? Is detail sufficient? Are mitigations clear?

**Report 3: Action Items Tracker (All Stakeholders)**
- **Audience:** Internal + external teams
- **Tone:** Clear, actionable
- **Focus:** Consolidated list of decisions, blockers, owners, deadlines
- **Language:** English with technical precision
- **Format:** Structured table (Owner, Item, Due Date, Status)
- **Validation Check:** Is every item clear and unambiguous? Are owners correctly identified? Are deadlines realistic?

Each report goes through the same three validation dimensions (Source Check, Bias Scan, Contextual Fit), but the **criteria** are tailored to that audience's needs.

## Why This Exceeds Level 2

**Level 2** would be:
- "I use Claude to help write reports"
- Review by skimming ("looks good")
- No documented validation approach
- Same report format for everyone
- Security is an afterthought

**Level 3** is:
- Designed workflow with human-in-the-loop validation as a core requirement
- **Specific, documented validation techniques** (Source Check, Bias Scan, Contextual Fit)
- **Six identified risks** with **designed mitigations**
- **Three distinct outputs** for different stakeholders (not one-size-fits-all)
- **Security by design** (OAuth, no hardcoded credentials, scoped data access)
- Fallback procedures documented (what happens if Google Drive is down? if deadline is missed?)

This demonstrates **governance maturity**. You've thought through what could go wrong and designed the workflow to prevent it. That's not just using AI better—it's **using AI safely and responsibly**.

## Fallback Procedures: Resilience Built In

The workflow acknowledges that **failure happens** and has documented backup plans:

**If Google Drive unavailable:**
- Nelson can paste transcript directly into Claude
- Process still completes; just takes slightly longer (vs. automatic file read)
- Reports still generated, validation still happens

**If Thursday morning deadline missed:**
- Process moves to Friday morning (reports still reach stakeholders mid-week)
- Or ad-hoc trigger is available immediately (for urgent situations)
- Process is not frozen; it's flexible

**If Claude generates poor output:**
- Nelson manually refines the report before sending
- Analyzes what went wrong (unclear transcript? missing context?)
- Notes issue for future improvement
- Stakeholder receives corrected output (not AI-generated errors)

These fallbacks matter because they show you understand that **AI integration is not "use AI or fail"**—it's "use AI to improve an underlying process that works even without AI." The process has resilience.

## Governance in Action: Example Validation

**Scenario:** Thursday morning, Claude generates Leadership Update for Gerardo

**Generated text:** 
```
"The database performance issue is now the primary blocker for sprint completion. 
The team has been working on this for two sprints. Without resolution, the project 
timeline will slip by 2-3 weeks."
```

**Nelson's validation:**

*Source Check:*
- ✓ Database performance mentioned in Client_Sync.txt (confirmed)
- ✓ Two-sprint effort confirmed in Daily_Standups.txt (confirmed)
- ? "2-3 week timeline slip" - is this in the transcripts or Nelson's interpretation?
- Action: Check original source; if not sourced, rewrite as "team estimates X-week impact pending investigation"

*Bias Scan:*
- Current framing: Crisis (primary blocker, 2-3 week slip)
- Alternative framing: Understood problem with mitigation path
- Consider: Is crisis framing appropriate right now? Or should we emphasize the mitigation strategy?
- Gerardo's needs: He needs to know the risk AND the plan to mitigate it
- Action: Rewrite to include both: "Database issue is the primary blocker. [Mitigation strategy from transcripts]. Expected resolution: [date]."

*Contextual Fit:*
- Live reality: The team is worried about this, but Ken and Shawn are still relatively calm
- Escalation value: Does Gerardo need to escalate this to VP level? Or is it within expected project risk?
- Strategic timing: This is week 1 of a 12-week issue; raising alarm now might be premature
- Action: Frame as "known risk with mitigation in progress" rather than "crisis requiring immediate escalation"

**Final output after validation:**
```
"Database performance optimization is the primary blocker for sprint 5 completion. 
This was identified in sprint 3 and the team has a mitigation strategy [link to details]. 
Expected resolution: [date]. Gerardo's attention needed on [specific resource decision]."
```

The validated report is **more useful** than the AI-generated version because it combines:
- AI's ability to synthesize data (Source Check ✓)
- Human judgment on tone and audience (Bias Scan ✓)
- Strategic understanding of context (Contextual Fit ✓)

This is **appropriate AI use**: AI handles the mechanical work; humans handle judgment.

---

## Supporting Materials

**Validation Checklist (Used for every report before sending):**
- [ ] Source Check: Every claim is attributable to transcript sources
- [ ] Bias Scan: Tone is appropriate for audience; framing is balanced
- [ ] Contextual Fit: Report aligns with live project reality and strategic priorities
- [ ] Format Check: Output matches established template for this audience
- [ ] Recipient Check: Report is going to correct stakeholder(s)

**Security Audit:**
- [x] No hardcoded credentials in process
- [x] OAuth authentication used for Google Drive
- [x] No sensitive data stored in transcript files
- [x] Access scoped to Mediquant project only
- [x] Reports delivered only to authorized stakeholders

**Risk Register Reviewed:**
- [x] All 6 risks identified with mitigation
- [x] Fallback procedures documented for critical failures
- [x] Monthly review schedule for emerging risks

---

## Next Steps: Ongoing Validation

- **June 2-6:** First week of real validation (test cycle with Gerardo feedback)
- **Ongoing:** Document validation decisions (what was flagged? what was changed?)
- **Monthly:** Review validation effectiveness (did reports match stakeholder needs?)
- **Ongoing:** Update risk register based on actual issues encountered

This demonstrates **Level 3 governance**: you've thought through failure modes, designed mitigations, built validation into the process, and created fallbacks. That's not just using AI; that's **using AI responsibly**.
