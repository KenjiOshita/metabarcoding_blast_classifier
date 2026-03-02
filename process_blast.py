import pandas as pd

input_file = #name change "blast_raw_yyyy.tsv"
output_file = #name change "blast_processed_yyyy.csv"

columns = [
    "qseqid",
    "sseqid",
    "pident",
    "length",
    "evalue",
    "bitscore",
    "stitle",
    "qlen"
]

df = pd.read_csv(input_file, sep="\t", header=None)
df.columns = columns

# Coverage (%)
df["coverage_percent"] = (df["length"] / df["qlen"]) 

# Extract taxonomy string
df["taxonomy_full"] = df["stitle"].str.split(" ", n=1).str[1]

tax_lists = df["taxonomy_full"].str.split(";")

# ---- Stable extraction ----

# Species (last)
df["species"] = tax_lists.str[-1]

# Genus (second last if available)
df["genus"] = tax_lists.apply(lambda x: x[-2] if len(x) >= 2 else None)

# Phylum (4th position if available)
df["phylum"] = tax_lists.apply(lambda x: x[3] if len(x) > 3 else None)

df.to_csv(output_file, index=False)

print("Processing complete.")
