#!/bin/bash

# ==============================================================================
# Step 1: SILVA Database Construction
# ==============================================================================

# --- [USER EDIT] ---
# WSLユーザーは、高速化とエラー回避のため DB_DIR には Linux側のパス (~/) を推奨します
INPUT_FASTA="/mnt/c/Users/kenzi/Desktop/Taxonomic classification/database/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_DIR="$HOME/databases/silva"
# -------------------

DB_NAME="$DB_DIR/SILVA_138_NR99"

echo "Building BLAST database in $DB_DIR..."
mkdir -p "$DB_DIR"

makeblastdb \
    -in "$INPUT_FASTA" \
    -dbtype nucl \
    -out "$DB_NAME"

echo "Setup complete. Database is located at: $DB_NAME"
