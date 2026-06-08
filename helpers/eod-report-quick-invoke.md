# EoD Report Helper — Quick Invoke

## Shortest possible command

Copy and paste this into Claude Code:

```
Run EoD helper for Mediquant. Raw notes: [paste notes here]
```

That's it. I'll use the standard helper settings and generate both Slack + Client Email versions.

## Even shorter (if you have prior day's report for slippage detection)

```
Run EoD helper for Mediquant with prior day context. Raw notes: [paste today] Previous report: [paste yesterday]
```

## Options

- Add `Also generate OPTIMIZED` if you want to see the trajectory tags version too
- I'll ask for clarification if progress numbers are missing

## Files involved

- `helpers/eod-report.md` — generic template
- `projects/mediquant/eod-report.context.md` — project context (stakeholders, workstreams, etc.)
- `projects/mediquant/client-email-template.html` — HTML formatting reference
