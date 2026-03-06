Metabarcoding BLAST Classifier (SILVA-based)
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
# 作業ディレクトリへ移動

cd "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

# 仮想環境の作成（初回のみ）

# python3 -m venv venv

# 仮想環境の起動（解析を始める時は必ず実行）

source venv/bin/activate

# 必要なライブラリのインストール(初回のみ)

# pip install pandas


② SILVAデータベースの準備

SILVAの公式サイトからダウンロードしたファイルは .gz 形式で圧縮されています。BLASTではそのまま使えないため、必ず解凍してください。

Bash
# databaseフォルダへ移動

cd database

# ファイルを解凍（.gz を消して .fasta にする）

gunzip SILVA_138.2_SSURef_NR99_tax_silva.fasta.gz

# 元の場所に戻る
cd  "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

③ データベースの構築（インデックス作成）

一度構築すれば、他の解析にもずっと使い回せます。

Bash
# scripts/setup_db.sh 内のパスが正しいか確認してから実行

bash scripts/setup_db.sh

成功のサイン: Adding sequences from FASTA; added 510495 sequences... と表示されれば完了です。


2. 解析の実行手順（新しいデータが来るたびに実行）
   
解析したいデータ（ファイルの例：Obama_2024_16S内にrepset.fasta）がある場合の手順です。

ルール

analysis/ の中にプロジェクトごとのフォルダを作る。

入力ファイル名は必ず repset.fasta に統一する。

実行コマンド例

Bash
# 1. BLAST検索の実行

# 指定したフォルダ内の repset.fasta を読み込み、blast_raw.tsv を出力します。

bash scripts/run_blast.sh analysis/Obama_2024_16S
#一番最後のanalysis/Obama_2024_16Sを適宜変更すること。

# 2. タクソノミー整形の実行

# blast_raw.tsv を読み込み、属・種を抽出した repset.csv を出力します。

python scripts/process_blast.py analysis/Obama_2024_16S



【実際の操作シミュレーション】（ターミナル起動後）

Bash

# 1. 起動と移動

cd "/mnt/c/Users/kenzi/Desktop/Taxonomic_classification"

# 2. 仮想環境

source venv/bin/activate

# 3. 解析（フォルダ名を変えること）

bash scripts/run_blast.sh analysis/Obama_2024_16S

python scripts/process_blast.py analysis/Obama_2024_16S

# 4. 終わったら仮想環境を抜ける
deactivate


