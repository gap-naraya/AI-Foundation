---
name: draft-message
description: Use this skill when the user wants to draft any professional message — Slack message, email, or communication — to a specific person. Triggers on "draft a message to", "write an email to", "how do I tell [name]", "write to Shawn", "write to Ken", "message to Gerardo", "message to Steven", "write to the team", or any request to compose a communication for work. Also use when the user asks how to communicate something sensitive, deliver bad news, or frame a difficult topic.
---

# Stakeholder Communication Drafter Skill

Nelson has a defined communication matrix. Auto-select tone, language, and depth based on the recipient before drafting anything.

## Audience Matrix

| Recipient | Tone | Language | Depth | Notes |
|---|---|---|---|---|
| **Shawn Fergusson** (Client CTO) | Formal | English | Value-driven, data-focused | Approval authority. Cares about macro tech strategy and escalation resolution. |
| **Ken Manley** (Client VP Engineering) | Formal | English | Predictable value delivery, timeline focus | Cares about scope constraints and baseline compliance. |
| **Gerardo Mora** (Senior Delivery Manager) | Professional, direct | English | Operational, risk-focused, metrics | Your manager. Cares about risk data flows and account stability. Use escalation scripts when blocked. |
| **Steven Yelton** (VP Engineering) | Professional | English | High-level, margin and relationship focused | Skip-level. Cares about client retention and gross margin. |
| **Jeff Gebhart** (EA team / CI/CD) | Work casual | English | High technical detail | External partner. Direct and specific. |
| **Sean Smith** (Architect) | Work casual | English | High technical detail | Internal architect. Can go deep on implementation. |
| **Bonnie Bordelon** (PM) | Work casual | English | Process-focused, team coordination | Internal PM. |
| **Engineering team** (Aristides, Roberto, Cesar, Jean Pierre, Jose) | Casual, direct | **Spanish** | Technical depth included | Direct reports. Protect from client chaos, give operational clarity. |

## Drafting rules

1. **Identify recipient first** — if not stated, ask.
2. **Apply the right tone and language** from the matrix above.
3. **Causal framing** — don't just state what happened; say why it matters or what it unblocks.
4. **No softening of facts** — do not water down status, risk, or bad news. State it clearly, then offer context or a path forward.
5. **For client messages** — formal English, no internal jargon, acronyms defined on first use.
6. **For bad news to clients** — lead with the fact, follow with impact, close with the mitigation or next step. Never bury the bad news.
7. **For escalations to Gerardo** — use the escalation skill instead (`escalate-gerardo`).

## Output format
Present the draft message ready to copy-paste or send. If Slack or Gmail tools are available and the user says "send it", use them. Always confirm before sending.
