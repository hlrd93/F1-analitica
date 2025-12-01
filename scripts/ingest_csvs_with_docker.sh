#!/usr/bin/env bash
# Ingest CSV files in ./datasets into ClickHouse using the clickhouse-client
# inside the running ClickHouse container. Intended as a reproducible script
# you can show your professor describing exactly what you ran.
#
# Behavior:
# - For each CSV in ./datasets/*.csv:
#   - Reads the header and creates a table raw.raw_<basename> with all
#     columns declared as String for safe ingestion.
#   - Replaces literal "\\N" with empty string and pipes the CSV into
#     clickhouse-client using CSVWithNames format.
#
# Pre-reqs: docker running and the `clickhouse` container created from
# the provided docker-compose.yml. Run the compose up step first:
#   docker compose --env-file ./scripts/.env up -d
#
# Usage:
#   chmod +x scripts/ingest_csvs_with_docker.sh
#   ./scripts/ingest_csvs_with_docker.sh
#
# Notes: the script intentionally creates tables with all String columns so
# the initial ingestion is resilient. Later you can create typed staging
# tables with dbt or SQL.

set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
DATA_DIR="$ROOT_DIR/datasets"

if [ ! -d "$DATA_DIR" ]; then
  echo "ERROR: datasets directory not found at $DATA_DIR"
  exit 1
fi

# Ensure database exists (run inside container)
docker exec -i clickhouse clickhouse-client --query "CREATE DATABASE IF NOT EXISTS raw;"

for csv in "$DATA_DIR"/*.csv; do
  [ -e "$csv" ] || continue
  name=$(basename "$csv" .csv)
  echo "\n=== Ingesting: $name (file: $csv) ==="

  header=$(head -n1 "$csv")
  if [ -z "$header" ]; then
    echo "Skipping empty file: $csv"
    continue
  fi

  # Build columns list: `col` String, ...
  cols=$(echo "$header" | awk -F',' '{ for(i=1;i<=NF;i++){ g=$i; gsub(/^\s+|\s+$/,"",g); printf("`%s` String%s", g, (i==NF?"":", ")); } }')

  create_sql="CREATE TABLE IF NOT EXISTS raw.raw_${name} (${cols}) ENGINE = MergeTree() ORDER BY tuple();"
  echo "Creating table raw.raw_${name} if not exists..."
  docker exec -i clickhouse clickhouse-client --query "$create_sql"

  echo "Inserting rows from CSV (literal '\\N' -> empty)..."
  # Replace literal \N with empty string, then insert using CSVWithNames
  sed 's/\\\\N//g' "$csv" | docker exec -i clickhouse clickhouse-client --query "INSERT INTO raw.raw_${name} FORMAT CSVWithNames"

  echo "Done: $name"
done

echo "\nAll CSVs processed. To verify counts, you can run:\n  docker exec -i clickhouse clickhouse-client --query \"SELECT table, sum(rows) FROM system.parts WHERE database='raw' GROUP BY table ORDER BY table;\""
