#!/bin/bash
# PostToolUse Hook: Auto-run pytest after editing Python files in src/
#
# Runs after Edit/Write completes on .py files.
# Shows test results directly in terminal — Claude sees pass/fail.

INPUT=$(cat)
TOOL_NAME="${TOOL_NAME:-}"

if [ "$TOOL_NAME" = "Edit" ] || [ "$TOOL_NAME" = "Write" ]; then
    FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('file_path',''))" 2>/dev/null)

    if echo "$FILE_PATH" | grep -qE '\.py$' && echo "$FILE_PATH" | grep -q 'src/'; then
        echo "--- AUTO-TEST HOOK ---"
        echo "Detected Python file change: $FILE_PATH"
        echo "Running pytest..."
        echo ""

        DEMO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
        cd "$DEMO_DIR/src" && python3 -m pytest test_train.py -v --tb=short 2>&1

        TEST_EXIT=$?
        echo ""
        if [ $TEST_EXIT -eq 0 ]; then
            echo "ALL TESTS PASSED"
        else
            echo "TESTS FAILED — fix before continuing"
        fi
        echo "--- END AUTO-TEST ---"
    fi
fi

exit 0
