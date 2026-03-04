import pandas as pd
import os
import sys

# ==============================================================================
# Step 3: Taxonomy Processing
# ==============================================================================

def parse_silva_taxonomy(stitle):
    """
    Splits the SILVA header to extract the full taxonomy string, 
    then identifies the Genus and Species.
    Example: 'ID Eukaryota;SAR;...;Chaetoceros;Chaetoceros neogracilis'
    """
    if pd.isna(stitle):
        return None, None, None
    
    # Split the title: [Accession ID] [Taxonomy String]
    parts = str(stitle).split(" ", 1)
    if len(parts) < 2:
        return None, None, None
    
    tax_str = parts[1]
    # Split by semicolon and remove empty elements
    tax_list = [t.strip() for t in tax_str.split(";") if t.strip()]
    
    # Extract levels safely from the end of the list
    # Species is the last element; Genus is the second to last.
    species = tax_list[-1] if len(tax_list) >= 1 else None
    genus = tax_list[-2] if len(tax_list) >= 2 else None
    
    return tax_str, genus, species

def run_processing(year):
    ## Your Work Place
    input_file = f"## path/to/your/results/blast_raw_{year}.tsv"
    output_file = f"## path/to/your/results/blast_processed_{year}.csv"

    columns = ["qseqid", "sseqid", "pident", "length", "evalue", "bitscore", "stitle", "qlen"]

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    # Load data
    df = pd.read_csv(input_file, sep="\t", names=columns)

    # Calculate Coverage
    df["coverage"] = df["length"] / df["qlen"]

    # Apply taxonomy extraction
    print("Extracting taxonomy...")
    results = df["stitle"].apply(parse_silva_taxonomy)
    df[["taxonomy_full", "genus", "species"]] = pd.DataFrame(results.tolist(), index=df.index)

    # Export to CSV
    df.to_csv(output_file, index=False)
    print(f"Success! Processed data saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_processing(sys.argv[1])
    else:
        print("Usage: python process_blast.py [YEAR]")
