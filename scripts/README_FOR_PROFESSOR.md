Ingest CSVs into ClickHouse — Reproducible steps

This document explains exactly how the CSV files in `datasets/` were moved
into ClickHouse for the course assignment. You can give this file to your
professor as a short walkthrough.

Prerequisites
- Docker and docker-compose available on the machine.
- The repository checked out and working directory at the project root.
- (Optional) A conda environment `f1_eda` if you want to run the Python
  loader variant instead of the docker approach.

Files of interest
- `docker-compose.yml` — ClickHouse service used in the example.
- `scripts/.env` — environment variables used by compose and scripts.
- `scripts/ingest_csvs_with_docker.sh` — the reproducible shell script that
  creates `raw.raw_<name>` tables and inserts CSV content via
  `clickhouse-client` inside the container.
- `scripts/load_csvs_to_clickhouse.py` — alternative Python loader using
  `clickhouse-connect` (installed into `f1_eda`).

Quick reproduction steps (recommended)

1) Start ClickHouse with the provided compose file:

```bash
docker compose --env-file ./scripts/.env up -d
```

2) Run the reproducible ingest script (this is the exact loop used):

```bash
chmod +x scripts/ingest_csvs_with_docker.sh
./scripts/ingest_csvs_with_docker.sh
```

3) Verify counts (example):

```bash
docker exec -i clickhouse clickhouse-client --query "SELECT table, sum(rows) AS rows FROM system.parts WHERE database='raw' GROUP BY table ORDER BY table;"
```

Notes and rationale
- The ingest script intentionally creates raw tables with all columns as
  `String` to avoid type and parsing issues at first ingestion. This is a
  safe staging step: subsequent transformations (dbt) will cast and
  validate types.
- Literal `\\N` values in the CSVs are replaced with empty strings prior
  to insertion to avoid ClickHouse interpreting them incorrectly.
- I also created a Python loader `scripts/load_csvs_to_clickhouse.py` that
  performs the same operations via `clickhouse-connect`; use that if you
  prefer a Python demonstration.

Outcome observed when run on this dataset (example counts):

```
raw_circuits: 77
raw_constructor_results: 12,625
raw_constructor_standings: 13,391
raw_constructors: 212
raw_driver_standings: 34,863
raw_drivers: 861
raw_lap_times: 589,081
raw_pit_stops: 11,371
raw_qualifying: 10,494
raw_races: 1,125
raw_results: 26,759
raw_seasons: 75
raw_sprint_results: 360
raw_status: 139
```

If you want a longer write-up or a short slide describing the pipeline, I
can prepare that as well.

-- end
