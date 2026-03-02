import sys
import pandas as pd

if len(sys.argv) != 3:
    print("Usage: python process_blast.py input.tsv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file, sep="\t")

# taxonomy split
tax_split = df["taxonomy_full"].str.split(";", expand=True)

df["domain"] = tax_split[0]
df["supergroup"] = tax_split[1]
df["clade"] = tax_split[2]
df["phylum"] = tax_split[3]
df["subphylum"] = tax_split[4]
df["class"] = tax_split[5]
df["genus"] = tax_split[7]
df["species"] = tax_split[8]

df.to_csv(output_file, index=False)

print("Processing complete.")
