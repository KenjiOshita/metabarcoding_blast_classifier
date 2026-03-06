import pandas as pd
import os
import sys

# ==============================================================================
# Step 3: Taxonomy Processing
# Usage: python scripts/process_blast.py analysis/Obama_2024_16S
# ==============================================================================

def parse_silva_taxonomy(stitle):
    if pd.isna(stitle): return None, None, None
    parts = str(stitle).split(" ", 1)
    if len(parts) < 2: return None, None, None
    
    tax_str = parts[1]
    tax_list = [t.strip() for t in tax_str.split(";") if t.strip()]
    
    # Species: Last element, Genus: Second to last
    species = tax_list[-1] if len(tax_list) >= 1 else None
    genus = tax_list[-2] if len(tax_list) >= 2 else None
    return tax_str, genus, species

def run_processing(project_dir):
    input_file = os.path.join(project_dir, "blast_raw.tsv")
    output_file = os.path.join(project_dir, "repset.csv")

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    cols = ["qseqid", "sseqid", "pident", "length", "evalue", "bitscore", "stitle", "qlen"]
    df = pd.read_csv(input_file, sep="\t", names=cols)
    
    # Calculate Coverage
    df["coverage"] = df["length"] / df["qlen"]

    # Taxonomy processing
    print(f"Processing data in {project_dir}...")
    results = df["stitle"].apply(parse_silva_taxonomy)
    df[["taxonomy_full", "genus", "species"]] = pd.DataFrame(results.tolist(), index=df.index)

    # Export to CSV
    df.to_csv(output_file, index=False)
    print(f"Done! Results saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_processing(sys.argv[1])
    else:
        print("Usage: python scripts/process_blast.py [PROJECT_DIRECTORY]")
