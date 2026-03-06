#!/bin/bash


# --- [修正箇所] ---
# パス全体を " " で囲んでください
INPUT_FASTA="/mnt/c/Users/kenzi/Desktop/Taxonomic_classification/database/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_DIR="$HOME/database/silva"
# -----------------

DB_NAME="$DB_DIR/SILVA_138_NR99"

echo "Building BLAST database in $DB_DIR..."
mkdir -p "$DB_DIR"

# ここも重要！変数 $INPUT_FASTA を " " で囲みます
makeblastdb \
    -in "$INPUT_FASTA" \
    -dbtype nucl \
    -out "$DB_NAME"

echo "Setup complete. Database is located at: $DB_NAME"
