Metabarcoding BLAST Classifier

Overview

This script performs BLAST (blastn) searches for metabarcoding data and extracts selected taxonomic ranks from a semicolon-delimited taxonomy string (SILVA-style annotation assumed).
It converts BLAST results into a taxonomy-resolved table suitable for downstream ecological or community analysis.
________________________________________
Expected Input

The script requires:

・A query FASTA file

・A BLAST database containing taxonomy information in sequence titles

The BLAST database sequence titles must contain a semicolon-separated lineage string, for example:

Eukaryota;SAR;Stramenopiles;Ochrophyta;Diatomea;Bacillariophytina;Mediophyceae;Chaetoceros;Chaetoceros neogracile

SILVA-like rank ordering is assumed.
________________________________________
BLAST Output Format

The script internally runs BLAST with:
-outfmt "6 qseqid sseqid pident length evalue bitscore stitle"
The resulting raw BLAST table contains:

・qseqid
・sseqid
・pident
・length
・evalue
・bitscore
・stitle

________________________________________
Output

Two files are generated:

1. Raw BLAST result
output_prefix_raw.tsv
2. Processed taxonomy table
output_prefix_processed.csv

The processed file contains:

・seqid
・sseqid
・pident
・length
・evalue
・bitscore
・stitle
・phylum
・genus
・species

Only phylum, genus, and species are extracted.
Original BLAST columns are preserved.
________________________________________
Usage

Basic usage:
python process_blast.py query.fasta database output_prefix

Example:
python process_blast.py ASV_2025.fasta silva_db results_2025
________________________________________
Requirements

・Python 3.9 or later
・pandas
・BLAST+ installed and accessible in PATH

Install dependency:
pip install pandas

Confirm BLAST installation:
blastn -version
________________________________________
Notes and Assumptions

・The taxonomy string must follow consistent rank ordering.

・Missing ranks may result in NA values.

・Species-level annotations may include "uncultured", "environmental sample", or "sp." entries.

・No best-hit filtering is performed.

・No identity or coverage filtering is applied.
________________________________________
Limitations

・Designed primarily for SILVA-style taxonomy strings.

・Does not perform LCA or confidence-based classification.

・Assumes fixed rank structure.
________________________________________
Recommended Workflow

１．Prepare a BLAST database containing taxonomy in sequence titles.

２．Run this script to perform BLAST and extract taxonomy.

３．Perform filtering (identity threshold, coverage filtering, best-hit selection) downstream in R or Python.

