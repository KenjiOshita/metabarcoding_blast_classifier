Metabarcoding BLAST Classifier

Overview
This script performs two steps:

Runs BLAST (blastn)

Extracts phylum, genus, and species from the taxonomy string in stitle

The taxonomy string is assumed to follow SILVA-style semicolon-delimited format.

Usage

python process_blast.py query.fasta database output_prefix

Example

python process_blast.py ASV_2025.fasta silva_db results_2025

This will produce:

results_2025_raw.tsv
results_2025_processed.csv

Output Columns

qseqid
sseqid
pident
length
evalue
bitscore
stitle
phylum
genus
species

Requirements

Python 3.9+
pandas
BLAST+ installed and available in PATH

Install pandas:

pip install pandas

Notes

Only phylum, genus, and species are extracted.

No identity or coverage filtering is applied.

Taxonomy extraction assumes SILVA-style ordering.

The script reflects the classification logic used in the 2024–2025 analysis.
