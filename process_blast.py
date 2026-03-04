import pandas as pd
import os

# ==========================================
# CONFIGURATION
# ==========================================
# Input: raw BLAST output (outfmt 6)
# Output: Processed CSV with taxonomy separation
INPUT_FILE = "blast_raw_2024.tsv"
OUTPUT_FILE = "blast_processed_2024.csv"

def process_blast_taxonomy(input_path, output_path):
    """
    Parses BLAST results and extracts taxonomy levels (Phylum, Genus, Species)
    specifically formatted for SILVA database headers.
    """
    
    # Define BLAST outfmt 6 columns used in the analysis
    columns = [
        "qseqid",    # Query Seq-id
        "sseqid",    # Subject Seq-id
        "pident",    # Percentage of identical matches
        "length",    # Alignment length
        "evalue",    # Expect value
        "bitscore",  # Bit score
        "stitle",    # Subject Title (Contains taxonomy)
        "qlen"       # Query length
    ]

    # Load the BLAST TSV file
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    df = pd.read_csv(input_path, sep="\t", names=columns)

    # Calculate Query Coverage (%)
    # Formula: (alignment length / total query length) * 100
    df["coverage_percent"] = (df["length"] / df["qlen"]) * 100

    # --- Taxonomy Extraction Logic ---
    # SILVA headers usually follow the format: "Accession Taxonomy;String;..."
    # We split by the first space to separate the Accession ID from the Taxonomy.
    df["taxonomy_full"] = df["stitle"].str.split(" ", n=1).str[1]

    # Split the taxonomy string by semicolon into a list, removing empty strings
    tax_lists = df["taxonomy_full"].apply(lambda x: [t.strip() for t in str(x).split(";") if t.strip()])

    # Extract specific levels safely:
    # Species: Last element
    df["species"] = tax_lists.apply(lambda x: x[-1] if len(x) >= 1 else None)
    
    # Genus: Second to last element
    df["genus"] = tax_lists.apply(lambda x: x[-2] if len(x) >= 2 else None)
    
    # Phylum: 4th element (Index 3) in the SILVA hierarchy
    df["phylum"] = tax_lists.apply(lambda x: x[3] if len(x) > 3 else None)

    # Save results to a CSV file
    df.to_csv(output_path, index=False)
    print(f"Processing complete. Results saved to: {output_path}")

if __name__ == "__main__":
    process_blast_taxonomy(INPUT_FILE, OUTPUT_FILE)
