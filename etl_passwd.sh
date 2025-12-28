#!/bin/bash

# Define file paths
INPUT_FILE="/etc/passwd"
EXTRACTED_FILE="extracted-data.txt"
TRANSFORMED_FILE="transformed.txt"
OUTPUT_FILE="data_for_analytics.csv"

# --- Extract phase ---
echo "Inside Extract"
cut -d':' -f1,3,6 "$INPUT_FILE" > "$EXTRACTED_FILE"

# --- Transform phase ---
echo "Inside Transform"
tr ':' ',' < "$EXTRACTED_FILE" > "$TRANSFORMED_FILE"

# --- Load phase ---
echo "Inside Load"
cp "$TRANSFORMED_FILE" "$OUTPUT_FILE"

# --- Check phase ---
echo "Inside Check"
cat "$OUTPUT_FILE"
