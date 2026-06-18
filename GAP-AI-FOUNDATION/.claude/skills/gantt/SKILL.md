---
name: gantt
description: Use this skill when the user says "gantt", "generate gantt", "run gantt", "gantt chart", "weekly gantt", "update the gantt", "create the gantt", or anything that implies generating the weekly Gantt chart artifact for the Mediquant DOM project. Also triggers on "what's the timeline", "show me the sprint plan", "Ken needs a Gantt", or "Shawn asked for the schedule".
---

# `/gantt` Skill — Weekly Gantt Chart Generator

Generate a professional Excel Gantt chart from an Azure DevOps CSV export. This artifact shows the strategic detail behind the daily EoD reports: sprint assignments, risk flags, projected completion, and workstream grouping.

**Audience:** Ken Manley and Shawn Fergason (client executives). Answers: "When will this be done?" and "What's at risk?"

---

## Pre-flight Check

Before reading any data, verify the three required files exist:

1. **`/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/ado-export.csv`**  
   — ADO work items export (Nelson drops this weekly)

2. **`/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/sprint-calendar.md`**  
   — Iteration calendar (one-time setup, Nelson updates when iterations begin)

3. **`/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/eod-report.context.md`**  
   — Project context (workstream definitions, team members, blockers)

**If any are missing:**
- If `ado-export.csv` is missing → stop. Tell Nelson: "Drop the ADO export CSV at `/projects/mediquant/gantt/ado-export.csv` first, then run `/gantt` again."
- If `sprint-calendar.md` is missing → stop. Tell Nelson: "Create `/projects/mediquant/gantt/sprint-calendar.md` (use the template in `/projects/mediquant/gantt/sprint-calendar.md`), then run `/gantt` again."
- If `eod-report.context.md` is missing → continue with degraded workstream grouping (use keyword fallback only).

---

## Step 1: Read Input Files

Read in this order:

1. **ADO Export CSV**  
   `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/ado-export.csv`  
   Expects columns: ID, Work Item Type, Title, State, Assigned To, Iteration Path, Story Points, Parent, Tags

2. **Sprint Calendar**  
   `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/sprint-calendar.md`  
   Markdown table with: Iteration Label, Start Date, End Date, Bye Week?, Notes

3. **EoD Context**  
   `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/eod-report.context.md`  
   For workstream groupings (WS1 = Infrastructure, WS2 = HIPAA Compliance)

---

## Step 2: Parse and Analyze

Claude will parse the CSV, compute sprint assignments, detect risks, and group by workstream. Present the analysis summary **before** generating Excel:

```
GANTT ANALYSIS SUMMARY — [date]

Iteration range: Iteration 370 (Jun 13–Jun 26) through Iteration 374 (Aug 8–Aug 21)
Total work items: [X] (Features: X, Stories: X, Tasks: X, Bugs: X)

WORKSTREAM 1 — INFRASTRUCTURE
  Features: X  |  Stories/Tasks: X  |  Points: X
  Projected completion: Iteration 372

WORKSTREAM 2 — HIPAA COMPLIANCE
  Features: X  |  Stories/Tasks: X  |  Points: X
  Projected completion: Iteration 373

RISK FLAGS ([count] items):
  - [ID] [Title] — REASON (Blocked / Orphaned / Overloaded assignee)
  - ...

OVERALL PROJECTED COMPLETION: Iteration [N] ([date range])

Ready to generate Excel?
```

**Wait for Nelson to confirm.** If he says "yes", "go", "generate", "proceed" — continue to Step 3. If he says "no" or "hold" — stop and wait for feedback.

---

## Step 3: Check / Install openpyxl

Before generating Excel, ensure the Python library openpyxl is installed:

```bash
python3 -c "import openpyxl" 2>&1 || pip3 install openpyxl
```

If the check passes, continue. If pip install is needed, run it and confirm success.

---

## Step 4: Write and Execute Python Script

Write the complete Python script to `/tmp/gantt_gen.py` (as a heredoc), then execute it:

```bash
python3 /tmp/gantt_gen.py
```

The script handles all the logic: parsing CSV, building hierarchy, calculating risk flags, generating Excel with colors and formatting.

**Python Script Contents:**

```python
#!/usr/bin/env python3
"""
Mediquant DOM Gantt Chart Generator
Reads ADO CSV export + sprint calendar, writes gantt-chart.xlsx
"""
import csv
import sys
import re
from datetime import datetime, timedelta
from pathlib import Path
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Paths
ADO_CSV_PATH = Path("/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/ado-export.csv")
SPRINT_CAL_PATH = Path("/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/sprint-calendar.md")
OUTPUT_PATH = Path("/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/gantt-chart.xlsx")

# Workstream keywords (adjust for your project's workstreams)
# For Data Platform: WS1 = Backend/Core, WS2 = Portal/UI
# For Mediquant DOM: WS1 = Infrastructure, WS2 = HIPAA Compliance
WS1_KEYWORDS = ["backend", "core", "data", "pipeline", "ingestion", "automation", "infrastructure", "databricks", "ci/cd", "devops", "terraform"]
WS2_KEYWORDS = ["portal", "ui", "frontend", "interface", "hipaa", "compliance", "policy", "remediation", "audit", "security"]

# Overloaded resources
OVERLOADED_ASSIGNEES = ["roberto", "cesar"]

# Risk threshold
HIGH_POINTS_THRESHOLD = 8

# Color palette (openpyxl hex, no #)
COLOR_WS1_HEADER = "2C3E50"
COLOR_WS2_HEADER = "1A5276"
COLOR_WS1_FILL = "D6EAF8"
COLOR_WS2_FILL = "D5F5E3"
COLOR_SPRINT_ACTIVE = "2ECC71"
COLOR_SPRINT_CURRENT = "F39C12"
COLOR_RISK_FILL = "FADBD8"
COLOR_HEADER_BG = "2C3E50"
COLOR_RISK_FLAG = "E74C3C"

def parse_sprint_calendar(path: Path) -> tuple[list, int]:
    """Parse sprint calendar markdown. Returns (list of sprint dicts, current_sprint_idx)."""
    with open(path, 'r') as f:
        lines = f.readlines()
    
    sprints = []
    today = datetime.now().date()
    current_idx = 0
    
    in_table = False
    for i, line in enumerate(lines):
        if '| Iteration Label |' in line:
            in_table = True
            continue
        if in_table:
            if line.strip().startswith('|---'):
                continue
            if not line.strip().startswith('|'):
                break
            
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) < 4:
                continue
            
            try:
                label = parts[0]
                start = datetime.strptime(parts[1], "%Y-%m-%d").date()
                end = datetime.strptime(parts[2], "%Y-%m-%d").date()
                bye = parts[3].lower() == "yes"
                
                sprints.append({
                    "label": label,
                    "start": start,
                    "end": end,
                    "bye": bye
                })
                
                if start <= today <= end:
                    current_idx = len(sprints) - 1
            except (ValueError, IndexError):
                continue
    
    return sprints, current_idx

def parse_ado_csv(path: Path) -> list:
    """Parse ADO export CSV. Returns list of item dicts. Handles title hierarchy."""
    items = []
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row is None:
                    continue
                clean_row = {k.strip(): v.strip() if v else "" for k, v in row.items()}
                
                # Merge title hierarchy: prefer Title 3 (story), then Title 2 (feature), then Title 1 (project)
                title3 = clean_row.get('Title 3', '').strip()
                title2 = clean_row.get('Title 2', '').strip()
                title1 = clean_row.get('Title 1', '').strip()
                
                merged_title = title3 if title3 else (title2 if title2 else title1)
                clean_row['Title'] = merged_title
                
                try:
                    clean_row['Story Points'] = int(clean_row.get('Story Points', 0) or 0)
                except ValueError:
                    clean_row['Story Points'] = 0
                
                items.append(clean_row)
    except Exception as e:
        print(f"ERROR reading CSV: {e}")
        sys.exit(1)
    
    return items

def classify_workstream(item: dict) -> str:
    """Classify item into WS1, WS2, or UNCLASSIFIED."""
    text = (item.get('Title', '') + ' ' + item.get('Tags', '')).lower()
    
    ws2_match = any(kw in text for kw in WS2_KEYWORDS)
    if ws2_match:
        return "WS2"
    
    ws1_match = any(kw in text for kw in WS1_KEYWORDS)
    if ws1_match:
        return "WS1"
    
    return "UNCLASSIFIED"

def map_to_sprint(iteration_path: str, sprints: list) -> str:
    """Extract iteration label from Iteration Path. Handles both old and new ADO formats."""
    if not iteration_path:
        return None
    
    # Extract the last path segment (e.g., 'Data Platform\Backlog\Current\Iteration 370 - Bye Week 2' -> 'Iteration 370 - Bye Week 2')
    parts = iteration_path.split('\\')
    label = parts[-1].strip() if len(parts) > 0 else iteration_path.strip()
    
    # Match against sprint calendar using substring (handles suffixes like "- Bye Week 2")
    for sprint in sprints:
        if sprint['label'].lower() in label.lower():
            return sprint['label']
    
    return None

def detect_risk(item: dict, sprints: list) -> tuple[bool, str]:
    """Detect risk flags. Returns (is_risk, reason_string)."""
    reasons = []
    
    state = item.get('State', '').lower()
    tags = item.get('Tags', '').lower()
    
    if state == 'blocked' or 'blocked' in tags:
        reasons.append("BLOCKED")
    
    points = item.get('Story Points', 0)
    assignee = item.get('Assigned To', '').lower()
    if points >= HIGH_POINTS_THRESHOLD and any(name in assignee for name in OVERLOADED_ASSIGNEES):
        reasons.append("HIGH EFFORT + OVERLOADED ASSIGNEE")
    
    iteration = item.get('Iteration Path', '').strip()
    work_type = item.get('Work Item Type', '')
    if not iteration and work_type != 'Feature':
        reasons.append("NO SPRINT ASSIGNED")
    
    return (len(reasons) > 0, ' | '.join(reasons))

def build_hierarchy(items: list, sprints: list) -> list:
    """Build Feature -> Story/Task hierarchy. Returns flat list of row descriptors."""
    item_map = {str(item.get('ID', '')): item for item in items}
    
    features = [item for item in items if item.get('Work Item Type') == 'Feature']
    non_features = [item for item in items if item.get('Work Item Type') != 'Feature']
    
    rows = []
    processed = set()
    
    for feature in features:
        f_id = str(feature.get('ID', ''))
        processed.add(f_id)
        
        ws = classify_workstream(feature)
        sprint = map_to_sprint(feature.get('Iteration Path', ''), sprints)
        is_risk, risk_reason = detect_risk(feature, sprints)
        
        rows.append({
            "type": "feature",
            "item": feature,
            "ws": ws,
            "sprint": sprint,
            "risk": is_risk,
            "risk_reason": risk_reason
        })
        
        for non_feature in non_features:
            parent_id = str(non_feature.get('Parent', ''))
            if parent_id == f_id and str(non_feature.get('ID', '')) not in processed:
                processed.add(str(non_feature.get('ID', '')))
                
                ws = classify_workstream(non_feature)
                sprint = map_to_sprint(non_feature.get('Iteration Path', ''), sprints)
                is_risk, risk_reason = detect_risk(non_feature, sprints)
                
                rows.append({
                    "type": "child",
                    "item": non_feature,
                    "ws": ws,
                    "sprint": sprint,
                    "risk": is_risk,
                    "risk_reason": risk_reason
                })
    
    for non_feature in non_features:
        nf_id = str(non_feature.get('ID', ''))
        if nf_id not in processed:
            processed.add(nf_id)
            
            ws = classify_workstream(non_feature)
            sprint = map_to_sprint(non_feature.get('Iteration Path', ''), sprints)
            is_risk, risk_reason = detect_risk(non_feature, sprints)
            
            rows.append({
                "type": "child",
                "item": non_feature,
                "ws": ws,
                "sprint": sprint,
                "risk": is_risk,
                "risk_reason": risk_reason
            })
    
    return rows

def create_gantt_workbook(rows: list, sprints: list, current_sprint_idx: int) -> openpyxl.Workbook:
    """Create Excel workbook with Gantt chart."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Gantt Chart"
    ws.freeze_panes = "F2"
    
    # Header row
    header_font = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
    header_fill = PatternFill("solid", fgColor=COLOR_HEADER_BG)
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    ws["A1"] = "ID"
    ws["B1"] = "Type"
    ws["C1"] = "Title"
    ws["D1"] = "Assignee"
    ws["E1"] = "Points"
    
    for col in ["A1", "B1", "C1", "D1", "E1"]:
        ws[col].font = header_font
        ws[col].fill = header_fill
        ws[col].alignment = header_align
    
    # Sprint columns
    for i, sprint in enumerate(sprints):
        col = 6 + i
        cell = ws.cell(row=1, column=col)
        start_str = sprint["start"].strftime("%b %d")
        end_str = sprint["end"].strftime("%b %d")
        cell.value = f"{sprint['label']}\n{start_str} – {end_str}"
        cell.font = header_font
        cell.fill = PatternFill("solid", fgColor=COLOR_SPRINT_CURRENT if i == current_sprint_idx else COLOR_HEADER_BG)
        cell.alignment = header_align
    
    # Risk column
    risk_col = 6 + len(sprints)
    risk_cell = ws.cell(row=1, column=risk_col)
    risk_cell.value = "Risk / Notes"
    risk_cell.font = header_font
    risk_cell.fill = header_fill
    risk_cell.alignment = header_align
    
    # Data rows
    for row_idx, row_desc in enumerate(rows, start=2):
        item = row_desc["item"]
        is_feature = row_desc["type"] == "feature"
        ws_label = row_desc.get("ws", "UNCLASSIFIED")
        assigned_sprint = row_desc.get("sprint")
        is_risk = row_desc.get("risk", False)
        risk_reason = row_desc.get("risk_reason", "")
        
        if is_feature:
            fill_hex = COLOR_WS1_HEADER if ws_label == "WS1" else COLOR_WS2_HEADER
            font_color = "FFFFFF"
            indent = 0
        else:
            fill_hex = COLOR_WS1_FILL if ws_label == "WS1" else COLOR_WS2_FILL
            font_color = "000000"
            indent = 1
        
        row_fill = PatternFill("solid", fgColor=fill_hex) if is_feature else None
        if is_risk and not is_feature:
            row_fill = PatternFill("solid", fgColor=COLOR_RISK_FILL)
        
        # Static columns
        ws.cell(row=row_idx, column=1).value = str(item.get("ID", ""))
        ws.cell(row=row_idx, column=2).value = item.get("Work Item Type", "")
        
        title_cell = ws.cell(row=row_idx, column=3)
        title_cell.value = ("    " * indent) + item.get("Title", "")
        title_cell.alignment = Alignment(wrap_text=True, indent=indent)
        
        ws.cell(row=row_idx, column=4).value = item.get("Assigned To", "")
        ws.cell(row=row_idx, column=5).value = item.get("Story Points", 0)
        
        # Apply row fill to first 5 columns
        for col_idx in range(1, 6):
            cell = ws.cell(row=row_idx, column=col_idx)
            if row_fill:
                cell.fill = row_fill
            cell.font = Font(name="Calibri", bold=is_feature, color=font_color)
        
        # Sprint columns
        for i, sprint in enumerate(sprints):
            col_idx = 6 + i
            cell = ws.cell(row=row_idx, column=col_idx)
            if assigned_sprint and sprint["label"].lower() == assigned_sprint.lower():
                cell.fill = PatternFill("solid", fgColor=COLOR_SPRINT_ACTIVE)
                cell.value = "●"
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                if is_feature:
                    cell.fill = PatternFill("solid", fgColor=fill_hex)
        
        # Risk column
        if risk_reason:
            risk_cell = ws.cell(row=row_idx, column=risk_col)
            risk_cell.value = risk_reason
            risk_cell.font = Font(name="Calibri", bold=True, color=COLOR_RISK_FLAG)
            risk_cell.fill = PatternFill("solid", fgColor=COLOR_RISK_FILL)
    
    # Column widths
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 42
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 8
    
    for i in range(len(sprints)):
        ws.column_dimensions[get_column_letter(6 + i)].width = 16
    ws.column_dimensions[get_column_letter(risk_col)].width = 32
    
    ws.row_dimensions[1].height = 36
    
    # Tab color
    ws.sheet_properties.tabColor = "2C3E50"
    
    return wb

def main():
    try:
        print("Reading sprint calendar...")
        sprints, current_idx = parse_sprint_calendar(SPRINT_CAL_PATH)
        print(f"  Found {len(sprints)} iterations")
        
        print("Reading ADO export...")
        items = parse_ado_csv(ADO_CSV_PATH)
        print(f"  Found {len(items)} work items")
        
        print("Analyzing work items...")
        risk_count = 0
        for item in items:
            is_risk, _ = detect_risk(item, sprints)
            if is_risk:
                risk_count += 1
        print(f"  Risk items flagged: {risk_count}")
        
        print("Building hierarchy...")
        rows = build_hierarchy(items, sprints)
        
        print("Generating Excel workbook...")
        wb = create_gantt_workbook(rows, sprints, current_idx)
        wb.save(str(OUTPUT_PATH))
        
        print(f"\nSUCCESS: Gantt chart written to {OUTPUT_PATH}")
        print(f"  Rows: {len(rows)} | Iterations: {len(sprints)} | Risk items: {risk_count}")
    except Exception as e:
        print(f"FATAL ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## Step 5: Post-Generation Report

After the Python script completes successfully, confirm to Nelson:

```
✓ Gantt chart generated successfully

File: /Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/gantt-chart.xlsx

Summary:
  - Total rows: [X]
  - Iterations: [X]
  - Risk items flagged: [X]

The file is ready to share with Ken and Shawn. Use `/draft-message` to compose the email.
```

If the script fails, print the error and stop. Tell Nelson to check:
1. ADO CSV format (is `Iteration Path` column present?)
2. Sprint calendar dates (are they in YYYY-MM-DD format?)
3. File permissions (can Python write to `/tmp/` and the output folder?)

---

## ADO Export Instructions (Tell Nelson This)

**Save a query in Azure DevOps, export as CSV weekly:**

### Query Configuration
- **Query type:** Flat list
- **Project:** Mediquant DOM
- **Filter:** `Work Item Type In (Feature, User Story, Task, Bug) AND State Not In (Removed)`

### Columns to Export (in order)
| Field Name |
|---|
| ID |
| Work Item Type |
| Title |
| State |
| Assigned To |
| Iteration Path |
| Story Points |
| Parent |
| Tags |

### Export Steps
1. Run the query in ADO
2. Click "Export to CSV" (top right menu)
3. Save file as `ado-export.csv`
4. Drop in: `/Users/naraya/Documents/AI-Foundation/GAP-AI-FOUNDATION/projects/mediquant/gantt/ado-export.csv`
5. Run `/gantt` in Claude Code

**Note:** ADO's CSV export sometimes includes a UTF-8 BOM. The Python script handles this automatically.

---

## Bye Week Planning Logic

**Key principle:** Do NOT allocate planned backlog items to bye weeks. Bye weeks are flex/buffer capacity.

**How it works in the Gantt:**
- Bye weeks (1-week iterations like 370, 377, 384) appear as **empty rows with no assigned work**
- Work is only assigned to 2-week iterations
- Projected completion date is calculated using **only 2-week iterations** (bye weeks excluded from the calculation)

**Strategic use of bye weeks:**
- Unplanned work (urgent fixes, production issues)
- Technical debt and infrastructure improvements
- Team capacity recovery
- Schedule buffer / deadline contingency
- Any ad-hoc project needs that emerge between planning cycles

**Recommendation:** When reviewing the Gantt, if the projected completion date is tight, flag to Nelson that bye weeks (370, 377, 384, etc.) provide additional buffer capacity that can absorb overruns or unplanned work without slipping the final deadline.

---

## One-Time Setup Checklist

Before running `/gantt` for the first time, Nelson needs:

- [ ] Folder exists: `projects/mediquant/gantt/`
- [ ] File created: `projects/mediquant/gantt/sprint-calendar.md` (template provided above)
- [ ] Iterations in calendar match ADO format (e.g., `Iteration 370`)
- [ ] Optionally: `pip3 install openpyxl` in Terminal (skill installs automatically if missing)
- [ ] First ADO export saved to `projects/mediquant/gantt/ado-export.csv`
- [ ] CLAUDE.md updated to list `/gantt` skill

All done, run `/gantt`!
