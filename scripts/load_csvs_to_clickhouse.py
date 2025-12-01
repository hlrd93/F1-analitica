#!/usr/bin/env python3
"""
Load CSV files from datasets/ into ClickHouse raw tables.
- Creates a table raw_<filename> with all String columns to be safe for initial ingestion.
- Uses CSVWithNames format and replaces literal "\\N" with empty string to avoid ClickHouse treating it literally.

Requires: clickhouse-connect (pip install clickhouse-connect)
Run with: source scripts/.env && python3 scripts/load_csvs_to_clickhouse.py
"""

import os
import sys
import glob
import csv
import pathlib
from clickhouse_connect import get_client

# Load env
from dotenv import load_dotenv
load_dotenv(dotenv_path=pathlib.Path(__file__).parent / '.env')

CH_HOST = os.getenv('CH_HOST', 'localhost')
CH_PORT = int(os.getenv('CH_PORT', 9000))
CH_USER = os.getenv('CH_USER', 'default')
_ch_pass_raw = os.getenv('CH_PASS')
# Treat empty string as no password (so client may connect without sending an empty auth header)
CH_PASS = None if (_ch_pass_raw is None or _ch_pass_raw == '') else _ch_pass_raw
CH_DB_RAW = os.getenv('CH_DB_RAW', 'raw')
CH_DB_ANALYTICS = os.getenv('CH_DB_ANALYTICS', 'analytics')
CSV_DIR = os.getenv('CSV_DIR', './datasets')

if not os.path.isdir(CSV_DIR):
    print(f"CSV_DIR does not exist: {CSV_DIR}")
    sys.exit(1)

client = get_client(host=CH_HOST, port=CH_PORT, username=CH_USER, password=CH_PASS)

# Ensure databases exist
client.command(f"CREATE DATABASE IF NOT EXISTS {CH_DB_RAW}")
client.command(f"CREATE DATABASE IF NOT EXISTS {CH_DB_ANALYTICS}")

csv_files = glob.glob(os.path.join(CSV_DIR, '*.csv'))
if not csv_files:
    print(f"No CSV files found in {CSV_DIR}")
    sys.exit(0)

for path in csv_files:
    base = os.path.basename(path)
    name, _ = os.path.splitext(base)
    table = f"{CH_DB_RAW}.raw_{name}"
    print(f"Processing {base} -> {table}")

    # Read header to get columns
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        reader = csv.reader(fh)
        try:
            header = next(reader)
        except StopIteration:
            print(f"Empty file: {path}, skipping")
            continue

    # Create table with all columns as String
    cols = ', '.join([f"`{c}` String" for c in header])
    create_sql = f"CREATE TABLE IF NOT EXISTS {table} ({cols}) ENGINE = MergeTree() ORDER BY tuple()"
    print("Creating table if not exists...")
    client.command(create_sql)

    # Read and upload in chunks
    BATCH_SIZE = 10000
    rows = []
    total = 0
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            # Replace literal \N with empty string
            clean = {k: (v if v != '\\N' else '') for k, v in r.items()}
            rows.append(clean)
            if len(rows) >= BATCH_SIZE:
                client.insert(table, rows, column_names=header)
                total += len(rows)
                print(f"Inserted {total} rows so far...")
                rows = []
        if rows:
            client.insert(table, rows, column_names=header)
            total += len(rows)
    print(f"Finished {base}: inserted approx {total} rows")

print("All done.")
