#!/bin/bash

##############################################################################
# Monthly Evidence Update Automation Script
#
# Automates the complete monthly evidence portfolio update cycle:
# 1. Validates that metrics file exists
# 2. Runs monthly orchestrator
# 3. Creates prompt for Evidence Extraction Agent
# 4. Generates progress report
# 5. Provides next steps
#
# Usage:
#   ./monthly-update.sh june 2026
#   ./monthly-update.sh july 2026
#   (scheduled via cron)
#
##############################################################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_ROOT="/Users/naraya/Documents/AI-Foundation"
AGENTS_DIR="$PROJECT_ROOT/agents"
EVIDENCE_DIR="$PROJECT_ROOT/Level3 Evidence"
AUTOMATION_DIR="$AGENTS_DIR/evidence-automation"
LOG_FILE="$AUTOMATION_DIR/update.log"

# Arguments
MONTH=${1:-$(date +%B | tr '[:upper:]' '[:lower:]')}
YEAR=${2:-$(date +%Y)}

# Timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

##############################################################################
# Functions
##############################################################################

log() {
    echo -e "${BLUE}[$(date '+%H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}✓ $1${NC}" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}✗ $1${NC}" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}⚠ $1${NC}" | tee -a "$LOG_FILE"
}

header() {
    echo "" | tee -a "$LOG_FILE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"
    echo -e "${BLUE}$1${NC}" | tee -a "$LOG_FILE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"
}

##############################################################################
# Pre-flight Checks
##############################################################################

header "MONTHLY EVIDENCE UPDATE: $MONTH $YEAR"

log "Starting at: $TIMESTAMP"
log "Project root: $PROJECT_ROOT"

# Check Python
if ! command -v python3 &> /dev/null; then
    error "Python3 not found. Install Python 3.7+"
    exit 1
fi
success "Python3 available"

# Check git
if ! command -v git &> /dev/null; then
    error "Git not found"
    exit 1
fi
success "Git available"

# Check directories exist
if [ ! -d "$EVIDENCE_DIR" ]; then
    error "Evidence directory not found: $EVIDENCE_DIR"
    exit 1
fi
success "Evidence directory found"

if [ ! -d "$AUTOMATION_DIR" ]; then
    error "Automation directory not found: $AUTOMATION_DIR"
    exit 1
fi
success "Automation directory found"

##############################################################################
# Check Metrics File
##############################################################################

header "Checking Metrics File"

METRICS_FILE="$EVIDENCE_DIR/workflow_logs_${MONTH}_${YEAR}.json"

if [ ! -f "$METRICS_FILE" ]; then
    error "Metrics file not found: workflow_logs_${MONTH}_${YEAR}.json"
    warning "Expected location: $EVIDENCE_DIR/"
    warning ""
    warning "To create metrics file:"
    warning "1. Copy: $AUTOMATION_DIR/metrics-template.json"
    warning "2. Rename to: workflow_logs_${MONTH}_${YEAR}.json"
    warning "3. Fill in actual data from your workflows"
    warning "4. Place in: $EVIDENCE_DIR/"
    warning ""
    warning "Then re-run: $0 $MONTH $YEAR"
    exit 1
fi
success "Metrics file found: $METRICS_FILE"

# Validate JSON
if ! python3 -m json.tool "$METRICS_FILE" > /dev/null 2>&1; then
    error "Metrics file is not valid JSON"
    exit 1
fi
success "Metrics file is valid JSON"

##############################################################################
# Run Orchestrator
##############################################################################

header "Running Evidence Orchestrator"

cd "$AUTOMATION_DIR"

python3 monthly-orchestrator.py --month "$MONTH" --year "$YEAR" 2>&1 | tee -a "$LOG_FILE"

if [ $? -ne 0 ]; then
    error "Orchestrator failed"
    exit 1
fi

success "Orchestrator completed"

##############################################################################
# Summary and Next Steps
##############################################################################

header "Monthly Update Cycle Summary"

log ""
log "✓ Pre-flight checks passed"
log "✓ Metrics validated: workflow_logs_${MONTH}_${YEAR}.json"
log "✓ Evidence extraction prompt generated"
log "✓ Progress report created"
log ""
log "NEXT STEPS:"
log ""
log "1️⃣  Run Evidence Extraction Agent:"
log "   Open agents/evidence-automation/extraction_prompt_${MONTH}_${YEAR}.md"
log "   Invoke with: Agent(subagent_type: 'general-purpose', description: '...', prompt: [...])"
log ""
log "2️⃣  After extraction completes:"
log "   - Review updated evidence files"
log "   - Move them to: Level3 Evidence/"
log ""
log "3️⃣  Run Evidence Validation Agent:"
log "   Reference: agents/evidence-validation/prompt.md"
log ""
log "4️⃣  After validation completes:"
log "   - Review validation report"
log "   - Address any critical issues"
log ""
log "5️⃣  Commit to git:"
log "   git add Level3\ Evidence/"
log "   git commit -m 'Update Level 3 evidence with $MONTH $YEAR outcomes'"
log "   git push origin main"
log ""
log "Full documentation: agents/evidence-automation/README.md"
log "Progress report: Level3\ Evidence/progress_report_${MONTH}_${YEAR}.md"
log "Log file: $LOG_FILE"
log ""

header "Automation Complete"

success "Monthly automation cycle initialized for $MONTH $YEAR"
log "All steps logged to: $LOG_FILE"

exit 0
