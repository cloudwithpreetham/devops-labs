#!/bin/bash
set -euo pipefail

echo "Strict mode demo started"

echo "Testing set -u with undefined variable"
# Uncomment the below line to test set -u
# echo "$UNDEFINED_VARIABLE"

echo "Testing set -e with failed command"
# Uncomment the below line to test set -e
# ls /not-existing-directory

echo "Testing pipefail"
# Uncomment the below line to test pipefail
# grep "ERROR" missing-file.log | wc -l

echo "Strict mode demo completed"
