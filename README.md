Metabarcoding BLAST Classifier (SILVA-based)
Overview
This workflow performs taxonomic assignment of metabarcoding sequences using a locally constructed SILVA-based BLAST database. The pipeline is divided into three functional steps: database construction, sequence alignment, and taxonomy parsing.

Directory Structure and Setup
Before execution, organize your workspace as follows:

## Project Root Directory
├── scripts/
│   ├── setup_db.sh
│   ├── run_blast.sh
│   └── process_blast.py
├── databases/
│   └── (SILVA FASTA file here)
└── analysis/
    └── [YEAR]/
        └── repset[YEAR].fasta
Note for WSL Users
To prevent "Database memory map file error," do not perform database construction on a Windows-mounted drive (e.g., /mnt/c/). Use your Linux native home directory (~/) for the database location.

Step 1: Database Construction
This is a one-time setup to create a reusable BLAST database from the SILVA reference FASTA.

Open setup_db.sh and set the following paths:

INPUT_FASTA: Path to your downloaded SILVA FASTA file.

DB_DIR: Directory where the BLAST index files will be stored.

Run the script:

Bash
bash scripts/setup_db.sh
This generates multiple index files (e.g., .nhr, .nin, .nsq). Once completed, this database can be referenced by any analysis for any year.

Step 2: BLASTn Search
Perform sequence alignment for a specific dataset.

Open run_blast.sh and set the DB_PATH to the location defined in Step 1.

Ensure your query FASTA is named repset[YEAR].fasta and placed in the corresponding year folder.

Run the script by specifying the year:

Bash
bash scripts/run_blast.sh 2025
This generates a raw BLAST output: blast_raw_2025.tsv.

Step 3: Taxonomy Processing
Extract Genus and Species information from the BLAST results.

Run the Python script by specifying the year:

Bash
python scripts/process_blast.py 2025
The script performs the following:

Extracts the full taxonomy string from the SILVA header.

Identifies the last rank as Species and the second-to-last as Genus.

Calculates query coverage.

Saves the result as blast_processed_2025.csv.

Requirements
NCBI BLAST+: Must be accessible in your system PATH.

Python 3.9+

pandas: Install via pip install pandas or pip install -r requirements.txt.

Summary of Operations
One-time: Build the database using setup_db.sh.

Per Dataset: Execute run_blast.sh followed by process_blast.py.

Downstream: Perform ecological filtering (identity/coverage thresholds) in R or Python using the generated CSV.
