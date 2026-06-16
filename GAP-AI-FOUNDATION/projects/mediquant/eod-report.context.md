# Mediquant Project — EoD Report Context

**Purpose:** Project-specific context for the End-of-Day status report
helper at `helpers/eod-report.md`. This file is loaded together with
the helper when Nelson generates a daily report for the Mediquant
project.

**Reusability:** Other helpers (meeting prep, weekly summary, etc.)
that touch the same project can also load this file for the
stakeholder cast, acronyms, and recurring themes.

**Last updated:** 2026-06-08

---

## Project codename

**DOM**

---

## Client

**Mediquant** (referred to as **MQ** in internal Slack)

---

## Workstreams

### 1. Core Team Execution

- **Objective:** Fully functional, testable environment
  (HiTrust/HIPAA-compliant) by **June 5**
  *(currently OFF TRACK; do not change the objective text unless
  officially re-baselined)*
- **Most recent reported state:** OFF TRACK, 83% complete (20 of 23
  tasks) as of Jun 05, 2026

### 2. Compliance & Architecture Review

- **Objective:** Complete the first 10 tasks group of HIPAA remediation plan by
  **June 19**
  *(do not change unless officially re-baselined — ask me for new objective when complete)*
- **Most recent reported state:** ON TRACK, 1 of 10 weekly tasks complete as of Jun 15, 2026

---

## Client email recipients

**To (Client stakeholders):**
- Shawn Fergason <sfergason@mediquant.com> (approval authority)
- Ken Manley <kenm@mediquant.com> (client executive)

**Cc (GAP team members):**
- Gerardo Mora <gmora@growthaccelerationpartners.com> (GAP leadership)
- Sean Smith <ssmith@growthaccelerationpartners.com> (Architecture/compliance lead)
- Milagro Prado Vasquez <mprado@growthaccelerationpartners.com>
- Matt Veitch <matt.veitch@growthaccelerationpartners.com>
- Steven Yelton <syelton@growthaccelerationpartners.com>

**From:** Nelson Araya Alvarado <naraya@growthaccelerationpartners.com> (or sent by delivery manager on behalf of team)

---

## Stakeholder cast

| Name | Role | Side |
|---|---|---|
| Sean | Architecture / compliance lead | GAP (internal) |
| Shawn F | Client executive — approval authority | Mediquant |
| Ken | Client executive | Mediquant |
| Jeff | EA team contact (CI/CD agents) | External / GAP partner |
| Nelson | PM (the report author) | GAP (internal) |

---

## Acronym glossary

- **NTR** — Nothing To Report
- **MQ** — Mediquant (client)
- **EA** — EA team (CI/CD infrastructure contact; Jeff is the contact)
- **GAP** — Growth Acceleration Partners (Nelson's employer)
- **PROD** — Production environment
- **CI/CD** — Continuous integration / deployment
- **HIPAA** — Health Insurance Portability and Accountability Act
- **EastinIT** — External consultancy doing architecture assessment
- **DOM** — Project codename

---

## Recurring themes (so the helper recognizes context)

- Pipeline performance (CI/CD speed, parallel build jobs)
- HIPAA compliance progress and policy baseline negotiation with MQ
- EastinIT architecture review (preliminary outcomes received Jun 5;
  feedback was positive — "architecturally sound")
- Databricks setup, security, and connection fixes
- Resource Group / subscription-based architecture proposal (raised by
  Eastin, to be approved by Shawn F)
