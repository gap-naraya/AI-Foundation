# Evidence Scan Snapshot

**Purpose:** Lightweight state tracker for the portfolio builder agent. Records when the last scan ran, to avoid re-scanning old commits.

**Pattern:** Reuses the same design as `projects/mediquant/eod-report.previous.md` — minimal content, updated after each scan.

---

## Current State

```
Last scan: 2026-07-05 21:43 UTC
Last approval: 2026-07-05 21:45 UTC
Scan window: 2026-07-05 21:00 to 2026-07-05 21:43 UTC
Items staged: 2
Items approved: 2
Status: All items promoted to evidence-log.md (items 4.9, 4.10 in Dimension 4)
Archive: evidence-log-2026-07-05-2.md created
```

---

## How It Works

1. Agent reads this file to find `last_scan` date
2. Agent runs git log from [last_scan] to now
3. Agent runs find for files modified since [last_scan]
4. After scan completes, agent overwrites this file with new timestamp
5. On next run, agent reads the new timestamp and scans only the delta

---

**Do not edit manually.** The `/portfolio` skill updates this automatically after each scan.
