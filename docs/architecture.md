## Arquitectura del Pipeline (basada en el código del repositorio)

Este diagrama refleja la arquitectura real implementada en el repo.

<div class="mermaid">
flowchart LR
  subgraph Source
    CSVs[CSV files (datasets/)]
  end

  subgraph Ingest
    %% Staging / Ingest
    Load[load_csvs_to_clickhouse.py]
    Shell[ingest_csvs_with_docker.sh]
  end

  subgraph RawDB
    %% ClickHouse - raw
    Raw[raw tables]
  end

  subgraph Transform
    %% Transforms / Models
    DBT[dbt_project (models/tests)]
  end

  subgraph AnalyticsDB
    %% ClickHouse - analytics
    Analytics[analytics tables]
  end

  subgraph Viz
    %% Visualización
    Streamlit[streamlit_app]
  end

  CSVs --> Load
  CSVs --> Shell
  Load --> Raw
  Shell --> Raw
  Raw --> DBT
  DBT --> Analytics
  Analytics --> Streamlit
  Docker[docker-compose.yml] -.-> Raw
  Docker -.-> Analytics

  %% notes
  %% removed classDef to avoid syntax issues
</div>

<!-- Static fallbacks in case client-side Mermaid fails to render -->
<picture>
  <source type="image/svg+xml" srcset="diagrams/architecture.svg">
  <img src="diagrams/architecture.png" alt="Arquitectura del pipeline (fallback)" style="max-width:100%;height:auto;">
</picture>

Descripción de componentes (referencias reales):

- Origen: `datasets/` (CSV). Los archivos reales están en la carpeta `datasets/` del repo.
- Ingestor (staging): `scripts/load_csvs_to_clickhouse.py` y `scripts/ingest_csvs_with_docker.sh` — crean tablas `raw.raw_<name>` con todas las columnas como `String` y cargan datos inicialmente (ver `scripts/README.md`).
- Warehouse/Transform: `dbt_project/` — contiene modelos que consumen los `raw` tables y generan tablas en la base `analytics`.
- Visualización: `streamlit_app/` (ya presente en el repo) que lee desde la base analítica.
- Orquestación/despliegue local: `docker-compose.yml` levanta `clickhouse` y `dbt-runner` según el repositorio.

Notas importantes observadas en el código:

- La ingestión es intencionalmente de dos pasos: primero cargas en tablas `String` en `raw` para evitar errores de tipo, luego `dbt` hace las castings y validaciones.
- El contenedor `dbt-runner` en `docker-compose.yml` ejecuta `dbt run` y `dbt test` automáticamente en el ejemplo.
