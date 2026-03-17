#!/bin/bash
# PreToolUse Hook: Block deletion of files in data/ directory
#
# Claude Code passes tool input as JSON on stdin.
# For Bash tool: {"command": "rm data/results.csv"}
# For Write tool: {"file_path": "..."}
#
# Exit 2 = BLOCK the tool call with a message to Claude

INPUT=$(cat)
TOOL_NAME="${TOOL_NAME:-}"

# Check Bash commands that delete data/ files
if [ "$TOOL_NAME" = "Bash" ]; then
    COMMAND=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('command',''))" 2>/dev/null)

    if echo "$COMMAND" | grep -qE '(rm|rm -rf|rm -r|rmdir|unlink).*data/'; then
        echo "BLOCKED: Cannot delete files in data/ directory."
        echo "This directory contains experiment results that must be preserved."
        echo ""
        echo "Attempted command: $COMMAND"
        exit 2
    fi
fi

# Check Edit/Write tools targeting data/ files
if [ "$TOOL_NAME" = "Write" ] || [ "$TOOL_NAME" = "Edit" ]; then
    FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('file_path',''))" 2>/dev/null)

    if echo "$FILE_PATH" | grep -q '/data/'; then
        echo "BLOCKED: Cannot modify files in data/ directory."
        echo "Experiment data is read-only. Create new files instead."
        echo ""
        echo "Attempted target: $FILE_PATH"
        exit 2
    fi
fi

exit 0
