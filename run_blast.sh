#!/bin/bash

YEAR=$1

blastn \
-query ${YEAR}/BLAST_${YEAR}/repset${YEAR}.fasta \
-db ~/silva_db/silva123_ssu_nr99 \
-out ${YEAR}/BLAST_${YEAR}/blast_raw_${YEAR}.tsv \
-outfmt "6 qseqid sseqid pident length evalue bitscore stitle qlen" \
-max_target_seqs 100 \
-perc_identity 95 \
-num_threads 4
