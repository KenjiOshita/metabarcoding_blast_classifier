# Metabarcoding BLAST Classifier (SILVA-based)

This repository provides a suite of tools for automatically performing taxonomic classification at the genus and species levels using the SILVA database on sequence data (ASVs/OTUs) obtained from metabarcoding analyses.

1. Folder Structure (Recommended)
To ensure smooth processing, the following folder structure is recommended:

my_project/

├── scripts/             # Scripts downloaded from GitHub

│   ├── setup_db.sh

│   ├── run_blast.sh

│   └── process_blast.py

├── databases/           # Location for storing the large SILVA dataset

└── analysis/            # Location for storing your analysis data

 └── Obama_2025_18S/
    
   └── repset.fasta # Ensure all FASTA filenames are identical.
    
　└── Obama_2024_18S/

　　 └── repset.fasta

   
2. Database Construction ＊Run only once

Converts SILVA FASTA files into a format suitable for BLAST searches.

Procedure:
Download SILVA_XXX_SSURef_NR99_tax_silva.fasta from the official SILVA website and place it in the databases/ folder.

1. Setup Procedure (First time only, or when updating the DB)
   
After launching the terminal, first navigate to the working directory and set up the environment.

① Navigating to the directory and activating the virtual environment

Bash

Navigate to the working directory

cd ‘/mnt/c/Users/kenzi/Desktop/Taxonomic_classification’

Create the virtual environment (only on the first run)
#python3 -m venv venv

Activate the virtual environment (must be run before starting analysis)
source venv/bin/activate

Install required libraries (first time only)
#pip install pandas



Translated with DeepL.com (free version)

② Preparing the SILVA Database

Files downloaded from the official SILVA website are compressed in .gz format. As BLAST cannot use them directly, you must decompress them.

Bash

Navigate to the database folder
cd database

Decompress the file (remove the .gz extension to create a .fasta file)
gunzip SILVA_138.2_SSURef_NR99_tax_silva.fasta.gz

Return to original location
cd ‘/mnt/c/Users/kenzi/Desktop/Taxonomic_classification’

③ Database Construction (Index Creation)
Once constructed, it can be reused indefinitely for other analyses.
Bash

Verify paths within scripts/setup_db.sh are correct before execution
bash scripts/setup_db.sh

2. Analysis execution procedure (run each time new data arrives)  
   
Procedure when you have data to analyse (e.g., repset.fasta within Obama_2024_16S).  

Rules  
Create a project-specific folder within analysis/.  
Input filenames must be uniformly named repset.fasta.

Example Execution Commands
Bash
 1. Run BLAST Search
    
Reads repset.fasta from the specified folder and outputs blast_raw.tsv.

bash scripts/run_blast.sh analysis/Obama_2024_16S


Replace the final analysis/Obama_2024_16S as appropriate.


2. Run taxonomy formatting

Reads blast_raw.tsv and outputs repset.csv containing extracted genus and species.

python scripts/process_blast.py analysis/Obama_2024_16S


# 【Simulated actual operation】 (After launching terminal)

Bash

1. Launch and navigate

cd ‘/mnt/c/Users/kenzi/Desktop/Taxonomic_classification’

2. Virtual environment

source venv/bin/activate

3. Analysis (change folder name)

bash scripts/run_blast.sh analysis/Obama_2024_16S

python3 scripts/process_blast.py analysis/Obama_2024_16S

4. Exit virtual environment upon completion
deactivate




Translated with DeepL.com (free version)


# Metabarcoding BLAST Classifier (SILVA-based)


このリポジトリは、メタバーコーディング解析で得られた配列データ（ASV/OTU）に対し、SILVAデータベースを用いて属・種レベルの系統分類を自動で行うためのツール一式です。

1. フォルダ構成（推奨） 
解析をスムーズに行うため、以下のようなフォルダ構成を推奨します。

my_project/

├── scripts/             # GitHubからダウンロードしたスクリプト

│   ├── setup_db.sh

│   ├── run_blast.sh

│   └── process_blast.py

├── databases/           # SILVAの巨大なデータを入れる場所

└── analysis/            # 自分の解析データを入れる場所

 └── Obama_2025_18S/
    
   └── repset.fasta # FASTA形式のファイル名は全て同一にしてください。
    
　└── Obama_2024_18S/

　　 └── repset.fasta

   
2. データベースの構築 ＊1回のみ実行

SILVAのFASTAファイルを、BLAST検索できる形式に変換します。

操作手順：
SILVA公式サイトから SILVA_XXX_SSURef_NR99_tax_silva.fasta をダウンロードし、databases/ フォルダに置きます。

1. セットアップ手順（初回、またはDB更新時のみ）
   
ターミナルを立ち上げたら、まずは作業ディレクトリに移動して環境を整えます。

① ディレクトリへの移動と仮想環境の起動

Bash

作業ディレクトリへ移動

cd "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

仮想環境の作成（初回のみ）
#python3 -m venv venv

仮想環境の起動（解析を始める時は必ず実行）
source venv/bin/activate

必要なライブラリのインストール(初回のみ)
#pip install pandas

② SILVAデータベースの準備

SILVAの公式サイトからダウンロードしたファイルは .gz 形式で圧縮されています。BLASTではそのまま使えないため、必ず解凍してください。

Bash

databaseフォルダへ移動
cd database

ファイルを解凍（.gz を消して .fasta にする）
gunzip SILVA_138.2_SSURef_NR99_tax_silva.fasta.gz

元の場所に戻る
cd  "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

③ データベースの構築（インデックス作成）
一度構築すれば、他の解析にもずっと使い回せます。
Bash

scripts/setup_db.sh 内のパスが正しいか確認してから実行
bash scripts/setup_db.sh

2. 解析の実行手順（新しいデータが来るたびに実行）
   
解析したいデータ（ファイルの例：Obama_2024_16S内にrepset.fasta）がある場合の手順です。

ルール
analysis/ の中にプロジェクトごとのフォルダを作る。
入力ファイル名は必ず repset.fasta に統一する。

実行コマンド例
Bash
 1. BLAST検索の実行
    
指定したフォルダ内の repset.fasta を読み込み、blast_raw.tsv を出力します。

bash scripts/run_blast.sh analysis/Obama_2024_16S
#一番最後のanalysis/Obama_2024_16Sを適宜変更すること。


2. タクソノミー整形の実行

blast_raw.tsv を読み込み、属・種を抽出した repset.csv を出力します。

python scripts/process_blast.py analysis/Obama_2024_16S


# 【実際の操作シミュレーション】（ターミナル起動後）

Bash

1. 起動と移動

cd "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

2. 仮想環境

source venv/bin/activate

3. 解析（フォルダ名を変えること）

bash scripts/run_blast.sh analysis/Obama_2024_16S

python3 scripts/process_blast.py analysis/Obama_2024_16S

4. 終わったら仮想環境を抜ける
deactivate


