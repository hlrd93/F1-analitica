## Arquitectura del Pipeline (basada en el código del repositorio)

Este diagrama refleja la arquitectura real implementada en el repo.

```mermaid
flowchart LR
  A[CSV files in datasets/] -->|scripts/load_csvs_to_clickhouse.py| B[Raw DB: ClickHouse (database: raw)]
  A -->|scripts/ingest_csvs_with_docker.sh| B
  B -->|dbt models (dbt_project/)| C[Analytics DB: ClickHouse (database: analytics)]
  C -->|streamlit_app/| D[Dashboard / Visualización]
  E[docker-compose.yml] -.-> B
  E -.-> C
  style E stroke-dasharray: 5 5
```

Descripción de componentes (referencias reales):

- Origen: `datasets/` (CSV). Los archivos reales están en la carpeta `datasets/` del repo.
- Ingestor (staging): `scripts/load_csvs_to_clickhouse.py` y `scripts/ingest_csvs_with_docker.sh` — crean tablas `raw.raw_<name>` con todas las columnas como `String` y cargan datos inicialmente (ver `scripts/README.md`).
- Warehouse/Transform: `dbt_project/` — contiene modelos que consumen los `raw` tables y generan tablas en la base `analytics`.
- Visualización: `streamlit_app/` (ya presente en el repo) que lee desde la base analítica.
- Orquestación/despliegue local: `docker-compose.yml` levanta `clickhouse` y `dbt-runner` según el repositorio.

Notas importantes observadas en el código:

- La ingestión es intencionalmente de dos pasos: primero cargas en tablas `String` en `raw` para evitar errores de tipo, luego `dbt` hace las castings y validaciones.
- El contenedor `dbt-runner` en `docker-compose.yml` ejecuta `dbt run` y `dbt test` automáticamente en el ejemplo.
