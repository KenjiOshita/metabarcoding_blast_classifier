#!/bin/bash

# ==============================================================================
# Step 2: BLASTn Search
# ==============================================================================
# Usage: ./run_blast.sh 2025
# ==============================================================================

YEAR=$1

if [ -z "$YEAR" ]; then
    echo "Error: Please provide a year (e.g., ./run_blast.sh 2025)"
    exit 1
fi

## Your Analysis Workspace
WORK_DIR="## path/to/your/analysis_folder/$YEAR"
DB_PATH="## path/to/your/db_directory/SILVA_138_NR99"

cd "$WORK_DIR" || exit

echo "Starting BLASTn for $YEAR..."

blastn \
    -query "repset${YEAR}.fasta" \
    -db "$DB_PATH" \
    -out "blast_raw_${YEAR}.tsv" \
    -outfmt "6 qseqid sseqid pident length evalue bitscore stitle qlen" \
    -max_target_seqs 100 \
    -perc_identity 95 \
    -num_threads 4

echo "Search finished. Output: blast_raw_${YEAR}.tsv"
