#!/bin/bash

YEAR=$1

blastn \
-query ${YEAR}/BLAST_${YEAR}/repset${YEAR}.fasta \
-db ~/SILVA_138.2_SSURef_NR99_tax_silva \
-out ${YEAR}/BLAST_${YEAR}/blast_raw_${YEAR}.tsv \
-outfmt "6 qseqid sseqid pident length evalue bitscore stitle qlen" \
-max_target_seqs 100 \
-perc_identity 95 \
-num_threads 4
