# Metabarcoding BLAST Classifier

Parse BLAST outfmt6 results with taxonomy string and split into taxonomic ranks.

## Input

Tab-delimited BLAST output including:
- qseqid
- sseqid
- pident
- length
- evalue
- bitscore
- stitle
- qlen
- coverage_percent
- taxonomy_full

## Usage

python process_blast.py input.tsv output.csv

## Output

Adds:
- domain
- supergroup
- clade
- phylum
- subphylum
- class
- genus
- species
