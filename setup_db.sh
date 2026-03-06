#!/bin/bash

# ==============================================================================
# Step 1: SILVA Database Construction
# ==============================================================================
# This script converts the SILVA FASTA file into a BLAST-searchable database.
# 
# [Note for WSL users] 
# To avoid "Memory map file errors," run this in your Linux home directory (~/) 
# instead of a Windows-mounted drive (/mnt/c/...).

## Your Database Directory
DB_DIR="## path/to/your/db_directory"
mkdir -p "$DB_DIR"

## Input FASTA file (extracted from SILVA_138.2_SSURef_NR99_tax_silva.fasta.gz)
INPUT_FASTA="## path/to/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_NAME="$DB_DIR/SILVA_138_NR99"

echo "Building BLAST database..."

makeblastdb \
    -in "$INPUT_FASTA" \
    -dbtype nucl \
    -out "$DB_NAME"

echo "Setup complete. Database is located at: $DB_NAME"

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

#!/bin/bash
# --- Settings ---
# WSLユーザーは必ず ~/ 以下のパスを指定してください
DB_DIR="$HOME/databases/silva"
INPUT_FASTA="$HOME/databases/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_NAME="$DB_DIR/SILVA_138_NR99"

# --- Process ---
mkdir -p "$DB_DIR"
makeblastdb -in "$INPUT_FASTA" -dbtype nucl -out "$DB_NAME"
