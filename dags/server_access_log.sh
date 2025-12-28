#!/bin/bash

# ensure we operate relative to the script file's directory
script_dir="$(cd "$(dirname "$0")" && pwd)"

# Define file paths (use absolute paths)
Download_file_URL="https://example.com/server_access_log.txt"
EXTRACTED_FILE="$script_dir/extracted-log.txt"

# fail fast and print commands for debugging
set -ex

# --- Extract phase ---
echo "Inside Extract"
echo "Will save to: $EXTRACTED_FILE"

# Check if extracted file already exists; if not, download it
if [ -f "$EXTRACTED_FILE" ]; then
    echo "File '$EXTRACTED_FILE' already exists — skipping download."
else
    echo "Downloading '$Download_file_URL' to '$EXTRACTED_FILE'..."
    if curl -fL --show-error -o "$EXTRACTED_FILE" "$Download_file_URL"; then
        echo "Download completed: $EXTRACTED_FILE"
    else
        echo "Download failed." >&2
        exit 1
    fi
fi

