Metabarcoding BLAST Classifier
Overview
This script parses BLAST outfmt6 results generated from metabarcoding data and extracts taxonomic ranks from a semicolon-delimited taxonomy string (e.g., SILVA-style annotation).
It converts a flat BLAST table into a taxonomy-resolved table suitable for downstream ecological or community analysis.
________________________________________
Expected Input Format
Tab-delimited BLAST output including the following columns:
・qseqid
・sseqid
・pident
・length
・evalue
・bitscore
・stitle
・qlen
・coverage_percent
・taxonomy_full
taxonomy_full must be a semicolon-separated lineage string, for example:
Eukaryota;SAR;Stramenopiles;Ochrophyta;Diatomea;Bacillariophytina;Mediophyceae;Chaetoceros;Chaetoceros neogracile
The script assumes SILVA-like rank order.
________________________________________
Output
The script appends the following columns:
・domain
・supergroup
・clade
phylum
subphylum
class
genus
species
Original BLAST columns are preserved.
________________________________________
Usage
Basic usage:
python process_blast.py input.tsv output.csv
Example:
python process_blast.py blast_raw_2025.tsv blast_processed_2025.csv
If no arguments are provided, default filenames inside the script will be used.
________________________________________
Requirements
Python ≥ 3.9
pandas
Install dependency:
pip install pandas
________________________________________
Notes and Assumptions
•	The taxonomy string must follow consistent rank ordering.
•	Missing ranks may result in NA values.
•	Species-level annotation may include "uncultured", "environmental sample", or "sp." entries.
•	No best-hit filtering is performed; this script only parses taxonomy.
________________________________________
Limitations
•	Designed primarily for SILVA-style taxonomy strings.
•	Does not perform LCA or confidence-based classification.
•	No identity or coverage filtering is applied.
________________________________________
Recommended Workflow
１．Run BLAST with taxonomy annotation included.
２．Process output with this script.
３．Perform filtering (identity, coverage, best-hit selection) downstream in R or Python.
