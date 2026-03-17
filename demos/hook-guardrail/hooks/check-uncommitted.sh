#!/bin/bash
# Stop Hook: Check for uncommitted experiment results before session ends
#
# Warns if data/ or src/ have uncommitted changes.
# Does NOT block — just alerts.

echo "--- SESSION END CHECK ---"

DEMO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DEMO_DIR"

# Check if we're in a git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "WARNING: Not a git repository. Experiment results may not be tracked."
    echo "--- END CHECK ---"
    exit 0
fi

UNCOMMITTED=$(git status --porcelain data/ src/ 2>/dev/null)

if [ -n "$UNCOMMITTED" ]; then
    echo "WARNING: Uncommitted experiment files detected!"
    echo ""
    echo "$UNCOMMITTED"
    echo ""
    echo "Consider committing before ending this session."
else
    echo "All experiment files are committed. Safe to exit."
fi

echo "--- END CHECK ---"
exit 0
