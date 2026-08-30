#!/bin/bash

set -e

markers="not integration"
rm -rf reports

# Find all test files recursively
find . -type f -name "test_*.py" | while read -r file; do
    set -x

    # Get the directory path relative to tests/ (e.g., "auth/api")
    folder=$(dirname "${file}")
    
    # Extract the base filename without extension (e.g., "test_login")
    base_name=$(basename "${file}" .py)
    
    # Create matching nested structure inside the reports folder
    mkdir -p "reports/${folder}"
    
    # Execute pytest for the individual file
    PYTHONPATH=. pytest "${file}" -m "${markers}" --junitxml="reports/${folder}/junit-${base_name}.xml" || true

    set +x
done

set +e
