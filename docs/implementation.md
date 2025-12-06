## Implementación — referencias al código existente

Esta sección documenta los artefactos ya implementados en el repositorio.

1) Scripts de ingestión

- `scripts/ingest_csvs_with_docker.sh` — script shell que llama a `clickhouse-client` dentro del contenedor para crear tablas `raw.raw_<name>` y cargar CSVs.
- `scripts/load_csvs_to_clickhouse.py` — loader Python con `clickhouse-connect`. Lee el encabezado para construir la tabla con todas las columnas como `String`, reemplaza `\\N` y hace inserts por lotes (BATCH_SIZE = 10000).

2) Configuración de despliegue local

- `docker-compose.yml` — levanta servicio `clickhouse` y el contenedor `dbt-runner` (que ejecuta `dbt run` y `dbt test` en la configuración del repo). El `docker-compose.yml` incluye un volumen `clickhouse_data`.

3) dbt

- `dbt_project/` — contiene `dbt_project.yml` y modelos. El perfil está configurado para `clickhouse` según `dbt_project/dbt_project.yml`.

4) Visualización

- `streamlit_app/` — aplicación de ejemplo que lee los modelos analíticos y muestra dashboards interactivos.

Notas operacionales extraídas del código:

- Autenticación: `scripts/.env` contiene variables para conectar con ClickHouse; `load_csvs_to_clickhouse.py` lee estas variables con `dotenv`.
- Bases de datos utilizadas: `raw` (staging) y `analytics` (resultados) — estas bases se crean en el loader Python si no existen.
