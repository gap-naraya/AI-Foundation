# Mediquant DOM Sprint Calendar

**Cadence:** 2-week iterations, starting on Fridays  
**Updated:** 2026-06-17

---

## Iteration Definitions

Each iteration row: label, start date (Friday), end date (Thursday two weeks later), bye-week flag.

| Iteration Label | Start Date  | End Date    | Bye Week? | Notes                        |
|---|---|---|---|---|
| Iteration 370   | 2026-06-13  | 2026-06-26  | No        | Current iteration            |
| Iteration 371   | 2026-06-27  | 2026-07-10  | No        |                              |
| Iteration 372   | 2026-07-11  | 2026-07-24  | No        |                              |
| Iteration 373   | 2026-07-25  | 2026-08-07  | No        |                              |
| Iteration 374   | 2026-08-08  | 2026-08-21  | No        |                              |

---

## Bye Week Concept

**[PLACEHOLDER — Nelson to define]**  
A "bye week" is an iteration where the team does not execute (e.g., company holiday, planned downtime, or vacation week). Mark `Bye Week? = Yes` for any iteration that should be skipped in planning.  

The `/gantt` skill reads this file but currently does NOT adjust point capacity or compress iteration timelines around bye weeks. When Nelson defines the full bye-week behavior, update the skill logic.

---

## Iteration Label Convention

Iteration Path in ADO exports as: `DOM\Iteration 370`  
The skill strips the `DOM\` prefix and matches on `Iteration XXX`.  
If your Iteration Path uses a different format, update this note.

---

## How to update this file

Before running `/gantt`, if a new iteration has started:
1. Add the new iteration row at the bottom
2. Confirm start/end dates (always Friday → Thursday, 14 days)
3. If a bye week is planned, flip `Bye Week?` to `Yes` and add a note
