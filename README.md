Metabarcoding BLAST Classifier (SILVA-based)
このリポジトリは、メタバーコーディング解析で得られた配列データ（ASV/OTU）に対し、SILVAデータベースを用いて属・種レベルの系統分類を自動で行うためのツール一式です。

0. 事前準備 (Preparation)
解析を始める前に、以下のソフトウェアがインストールされていることを確認してください。

NCBI BLAST+: blastn コマンドが使える状態。

Python 3.9+: pandas ライブラリが必要です。

Bash
pip install pandas
WSLユーザーへ:
データベース作成は、Windows側のフォルダ（/mnt/c/...）ではなく、必ず Linux側のホームディレクトリ（~/） で行ってください。そうしないと、メモリ不足エラーで失敗します。

1. フォルダ構成の推奨 
解析をスムーズに行うため、以下のようなフォルダ構成を推奨します。

Plaintext
my_project/
├── scripts/             # GitHubからダウンロードしたスクリプト
│   ├── setup_db.sh
│   ├── run_blast.sh
│   └── process_blast.py
├── databases/           # SILVAの巨大なデータを入れる場所
└── analysis/            # 自分の解析データを入れる場所
    └── 2025/
        └── repset_16S_2025.fasta
2. 【Step 1】 データベースの構築 ＊1回のみ実行
SILVAのFASTAファイルを、BLASTが高速検索できる形式に変換します。

操作手順：
SILVA公式サイトから SILVA_XXX_SSURef_NR99_tax_silva.fasta をダウンロードし、databases/ フォルダに置きます。

setup_db.sh を開き、上部のパス設定を自分の環境に書き換えます。

ターミナルで実行：

Bash
bash scripts/setup_db.sh
スクリプト修正版 (setup_db.sh):
Bash
#!/bin/bash
# --- Settings ---
# WSLユーザーは必ず ~/ 以下のパスを指定してください
DB_DIR="$HOME/databases/silva"
INPUT_FASTA="$HOME/databases/SILVA_138.2_SSURef_NR99_tax_silva.fasta"
DB_NAME="$DB_DIR/SILVA_138_NR99"

# --- Process ---
mkdir -p "$DB_DIR"
makeblastdb -in "$INPUT_FASTA" -dbtype nucl -out "$DB_NAME"
3. 【Step 2】 BLAST検索の実行
自分の配列データ（Query）を、Step 1で作ったデータベースに照らし合わせます。

操作手順：
解析したいファイルを analysis/2025/ などに配置します。

run_blast.sh を実行します。この際、**「年度」と「ファイル名の接頭辞」**を引数として渡せるように改良しました。

例：repset_16S_2025.fasta を解析する場合

Bash
bash scripts/run_blast.sh 2025 repset_16S
スクリプト修正版 (run_blast.sh):
Bash
#!/bin/bash
YEAR=$1
PREFIX=${2:-"repset"} # 第2引数がない場合はデフォルトで "repset"

# --- Settings ---
# Step 1で作ったDBの場所を指定
DB_PATH="$HOME/databases/silva/SILVA_138_NR99"
# 自分の解析フォルダの場所を指定
WORK_DIR="/mnt/c/Users/YourName/Desktop/Project/analysis/${YEAR}"

# --- Process ---
cd "$WORK_DIR" || exit
blastn \
    -query "${PREFIX}_${YEAR}.fasta" \
    -db "$DB_PATH" \
    -out "blast_raw_${YEAR}.tsv" \
    -outfmt "6 qseqid sseqid pident length evalue bitscore stitle qlen" \
    -max_target_seqs 100 \
    -perc_identity 95 \
    -num_threads 4
4. 【Step 3】  Taxoの形成とCSV出力
BLASTの結果から「属（Genus）」と「種（Species）」を抽出し、見やすい表（CSV）にします。

操作手順：
仮想環境を使っている場合は source venv/bin/activate などで起動します。

Pythonスクリプトを実行します。

Bash
python scripts/process_blast.py 2025
スクリプト修正版 (process_blast.py):
※パスをスクリプト冒頭で一括管理できるように改良しました。

Python
import pandas as pd
import os
import sys

# --- Settings ---
# ここを自分の環境に合わせて書き換えてください
BASE_DIR = "/mnt/c/Users/YourName/Desktop/Project/analysis"

def parse_silva_taxonomy(stitle):
    if pd.isna(stitle): return None, None, None
    parts = str(stitle).split(" ", 1)
    if len(parts) < 2: return None, None, None
    
    tax_str = parts[1]
    tax_list = [t.strip() for t in tax_str.split(";") if t.strip()]
    
    species = tax_list[-1] if len(tax_list) >= 1 else None
    genus = tax_list[-2] if len(tax_list) >= 2 else None
    return tax_str, genus, species

def run_processing(year):
    work_dir = os.path.join(BASE_DIR, str(year))
    input_file = os.path.join(work_dir, f"blast_raw_{year}.tsv")
    output_file = os.path.join(work_dir, f"blast_processed_{year}.csv")

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    columns = ["qseqid", "sseqid", "pident", "length", "evalue", "bitscore", "stitle", "qlen"]
    df = pd.read_csv(input_file, sep="\t", names=columns)
    df["coverage"] = df["length"] / df["qlen"]

    print(f"Processing Year {year}...")
    results = df["stitle"].apply(parse_silva_taxonomy)
    df[["taxonomy_full", "genus", "species"]] = pd.DataFrame(results.tolist(), index=df.index)

    df.to_csv(output_file, index=False)
    print(f"Completed! Output: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_processing(sys.argv[1])
    else:
        print("Usage: python process_blast.py [YEAR]")


