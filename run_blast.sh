#!/bin/bash

# ==============================================================================
# Step 2: BLASTn Search
# Usage: bash scripts/run_blast.sh analysis/Obama_2024_16S
# ==============================================================================

PROJECT_DIR=$1

if [ -z "$PROJECT_DIR" ]; then
    echo "Error: Please specify the project directory (e.g., analysis/Obama_2024_16S)"
    exit 1
fi

# --- [USER EDIT] ---
# Step 1 で指定したDBのパスをここに記入
DB_PATH="$HOME/databases/silva/SILVA_138_NR99"
# -------------------

echo "Running BLAST for: $PROJECT_DIR"

blastn \
    -query "${PROJECT_DIR}/repset.fasta" \
    -db "$DB_PATH" \
    -out "${PROJECT_DIR}/blast_raw.tsv" \
    -outfmt "6 qseqid sseqid pident length evalue bitscore stitle qlen" \
    -max_target_seqs 100 \
    -perc_identity 95 \
    -num_threads 4

echo "Search finished. Results saved in ${PROJECT_DIR}/blast_raw.tsv"
