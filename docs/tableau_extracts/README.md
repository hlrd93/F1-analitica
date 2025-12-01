Tableau extracts and starter workbook

Files in this folder:

- `constructor_metrics_top200.csv` — sample/top-200 export used by the example workbook.
- `constructor_time_series_sample.csv` — sample time-series rows used by the example workbook.
- `constructor_metrics_full.csv` — full export of `analytics.constructor_metrics` from ClickHouse (no LIMIT).
- `constructor_time_series_full.csv` — full export of `analytics.constructor_time_series` from ClickHouse (no LIMIT).
- `constructor_workbook.twb` — a minimal Tableau workbook (XML) that references the CSV sample files above. Open it in Tableau Desktop and then save as `.twbx` if you want a packaged workbook.

How to use

1. Open `constructor_workbook.twb` in Tableau Desktop. The workbook refers to the CSV files by relative path under `docs/tableau_extracts/` — if Tableau cannot find them, use File > Open and point the datasource to the matching CSV location.

2. If you want the full datasets, load `constructor_metrics_full.csv` and `constructor_time_series_full.csv` into Tableau (Data > New Data Source > Text File).

3. If you modify the CSVs (for example after re-running dbt or ingesting cost data), refresh the data source in Tableau (Data > Refresh) or re-point the connection to the updated CSV.

Ingesting real cost data (optional)

If you have a CSV with constructor cost information (example name: `constructor_costs.csv` or `raw_constructor_costs.csv`) place it into the `datasets/` folder and run the ingestion script used for other CSVs:

```bash
./scripts/ingest_csvs_with_docker.sh
```

After ingesting, run the optional dbt model to compute real cost-normalized scores:

```bash
docker compose run --rm -v "$PWD/profiles.compose.yml":/workspace/profiles.yml --entrypoint /bin/bash dbt-runner -lc "dbt run --project-dir /workspace/dbt_project --profiles-dir /workspace --select constructor_metrics_with_costs && dbt test --project-dir /workspace/dbt_project --profiles-dir /workspace --select constructor_metrics_with_costs"
```

Notes
- The `.twb` included is minimal — you may want to replace the datasources in Tableau with the full CSVs or a live ClickHouse connection.
- If you prefer I can (A) try to ingest a provided cost CSV and run the dbt model for you, or (B) produce an updated `.twb` that references the full CSVs. Tell me which and I'll proceed.
