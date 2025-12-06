## F1 Analytics — Documentación del Pipeline

Bienvenido a la documentación del proyecto `F1-analitica`.

Este sitio recoge el diseño, la implementación y las decisiones tomadas durante
la construcción del pipeline de datos que carga los CSVs con información de
F1 en ClickHouse y genera modelos analíticos con `dbt`.

Contenido relevante en el repo:

- `datasets/` — CSVs de entrada (drivers, races, lap_times, etc.).
- `scripts/ingest_csvs_with_docker.sh` — script reproducible que inserta CSVs en ClickHouse.
- `scripts/load_csvs_to_clickhouse.py` — loader Python que usa `clickhouse-connect`.
- `docker-compose.yml` — levanta ClickHouse y el contenedor `dbt-runner`.
- `dbt_project/` — modelos y tests dbt para transformar datos desde `raw` hacia `analytics`.
- `streamlit_app/` — aplicación de visualización que consume los datos transformados.

Usa la navegación a la izquierda para explorar arquitectura, ingestión,
implementación y metodologías.
