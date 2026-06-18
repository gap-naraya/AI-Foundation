# Mediquant DOM Sprint Calendar

**Cadence:** 2-week iterations, starting on Fridays; 1-week bye weeks once per quarter  
**Updated:** 2026-06-17

---

## Iteration Definitions

Each iteration row: label, start date (Friday), end date (Thursday), bye-week flag.

**Bye Week Pattern:** One 1-week bye week per quarter (Iterations 370, 377, 384, ...)  
All other iterations are 2-week sprints.

| Iteration Label | Start Date  | End Date    | Bye Week? | Notes                        |
|---|---|---|---|---|
| Iteration 370   | 2026-06-13  | 2026-06-19  | Yes       | Current iteration (1-week bye) |
| Iteration 371   | 2026-06-20  | 2026-07-03  | No        | 2-week                       |
| Iteration 372   | 2026-07-04  | 2026-07-17  | No        | 2-week                       |
| Iteration 373   | 2026-07-18  | 2026-07-31  | No        | 2-week                       |
| Iteration 374   | 2026-08-01  | 2026-08-14  | No        | 2-week                       |
| Iteration 375   | 2026-08-15  | 2026-08-28  | No        | 2-week                       |
| Iteration 376   | 2026-08-29  | 2026-09-11  | No        | 2-week                       |
| Iteration 377   | 2026-09-12  | 2026-09-18  | Yes       | Q4 bye week (1-week)         |
| Iteration 378   | 2026-09-19  | 2026-10-02  | No        | 2-week                       |
| Iteration 379   | 2026-10-03  | 2026-10-16  | No        | 2-week                       |
| Iteration 380   | 2026-10-17  | 2026-10-30  | No        | 2-week                       |
| Iteration 381   | 2026-10-31  | 2026-11-13  | No        | 2-week                       |
| Iteration 382   | 2026-11-14  | 2026-11-27  | No        | 2-week                       |
| Iteration 383   | 2026-11-28  | 2026-12-11  | No        | 2-week                       |
| Iteration 384   | 2026-12-12  | 2026-12-18  | Yes       | Q1 bye week (1-week)         |

---

## Bye Week Definition

A "bye week" is a **1-week iteration** (Friday–Thursday) where planned backlog items are **NOT allocated**. Instead, bye weeks serve as **buffer/flex capacity**.

**Primary uses:**
- Unplanned work (urgent fixes, production issues)
- Technical debt and infrastructure improvements
- Team capacity recovery between quarters
- Schedule contingency / deadline buffer
- Any ad-hoc project needs that emerge between planning cycles

**Planning rule:** When allocating backlog to iterations in `/gantt`, do NOT assign items to bye weeks. Projected completion date is calculated using only 2-week iterations (bye weeks are excluded from the timeline calculation).

**Metrics handling:** Bye week metrics merge with the **next iteration's metrics** for reporting and velocity calculations. Bye weeks do not carry independent capacity or burndown tracking.

**Pattern:** One bye week per quarter, roughly every 7 iterations (370, 377, 384, 391, etc.)

The `/gantt` skill marks bye weeks on the Gantt chart as empty rows for visibility. When reviewing tight timelines, recommend leveraging bye weeks as strategic buffers to mitigate schedule risk.

---

## Iteration Label Convention

Iteration Path in ADO exports as: `DOM\Iteration 370` (or may include a suffix like `DOM\Iteration 370 - Q3`)

**Label matching:** The skill strips the `DOM\` prefix and matches iterations by **substring containing** the iteration number (e.g., matches "Iteration 370" in "Iteration 370 - Q3").

If your Iteration Path uses a completely different format, update this note and the skill's `map_to_sprint()` function may need adjustment.

---

## How to update this file

Before running `/gantt`, if a new iteration has started:
1. Add the new iteration row at the bottom
2. Confirm start/end dates (always Friday → Thursday, 14 days)
3. If a bye week is planned, flip `Bye Week?` to `Yes` and add a note
