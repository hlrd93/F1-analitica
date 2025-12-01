dbt project for F1-analitica

This folder contains starter dbt models to transform the clickhouse `raw`
schema into analytics-ready tables. This is a minimal scaffold — update
`profiles.yml` with your ClickHouse connection and adapter (for example,
`dbt-clickhouse` or `clickhouse-dbt` depending on your environment).

How to run (example):

1) Install dbt-core and a ClickHouse adapter (recommended: use a virtualenv or conda env):

```bash
pip install dbt-core dbt-clickhouse
# or use conda environment with dbt already available
```

2) Create a `profiles.yml` in `~/.dbt/` or follow the adapter's docs. You can copy
   the example `profiles.yml.example` in this folder and adapt it.

3) Run dbt models:

```bash
dbt run --profiles-dir dbt_project
```
