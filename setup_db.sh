#!/bin/bash
# --- Settings ---
DB_DIR="$HOME/databases/silva"
# --- 修正箇所 ---
#データベースを置いたファイルを指定してください。以下は一例です。
INPUT_FASTA="/mnt/c/Users/kenzi/Desktop/Taxonomic classification/database/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_OUT_DIR="$HOME/SILVA_DB" # Linux側に保存（推奨）
# ----------------

# --- Process ---
mkdir -p "$DB_DIR"
makeblastdb -in "$INPUT_FASTA" -dbtype nucl -out "$DB_NAME"
