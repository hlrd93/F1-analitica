## Arquitectura del Pipeline (basada en el código del repositorio)

Este diagrama refleja la arquitectura real implementada en el repo.

<div class="mermaid">
flowchart LR
  subgraph Source
    A[CSV files]
  end

  subgraph Ingest
    B[load_csvs]
    C[ingest_shell]
  end

  subgraph RawDB
    D[raw_tables]
  end

  subgraph Transform
    E[dbt_models]
  end

  subgraph AnalyticsDB
    F[analytics_tables]
  end

  subgraph Viz
    G[streamlit]
  end

  A --> B
  A --> C
  B --> D
  C --> D
  D --> E
  E --> F
  F --> G
  H[docker_compose] -.-> D
  H -.-> F
</div>

<!-- Static fallbacks in case client-side Mermaid fails to render -->
<picture>
  <source type="image/svg+xml" srcset="/diagrams/architecture.svg">
  <img src="/diagrams/architecture.png" alt="Arquitectura del pipeline (fallback)" style="max-width:100%;height:auto;">
</picture>

<script>
// Hide/show fallback image depending on whether mermaid rendered successfully.
// If mermaid produced an error SVG (aria-roledescription="error"), hide the mermaid block
// and leave the fallback picture visible. If mermaid succeeds hide the fallback.
document.addEventListener('DOMContentLoaded', function(){
  // Wait briefly for mermaid to render
  setTimeout(function(){
    document.querySelectorAll('.mermaid').forEach(function(m){
      var pic = m.nextElementSibling;
      var isError = !!m.querySelector('svg[aria-roledescription="error"]');
      if (isError){
        m.style.display = 'none';
        if (pic && pic.tagName && pic.tagName.toLowerCase() === 'picture') pic.style.display = '';
      } else {
        if (pic && pic.tagName && pic.tagName.toLowerCase() === 'picture') pic.style.display = 'none';
      }
    });
  }, 600);
});
</script>

Descripción de componentes (referencias reales):

- Origen: `datasets/` (CSV). Los archivos reales están en la carpeta `datasets/` del repo.
- Ingestor (staging): `scripts/load_csvs_to_clickhouse.py` y `scripts/ingest_csvs_with_docker.sh` — crean tablas `raw.raw_<name>` con todas las columnas como `String` y cargan datos inicialmente (ver `scripts/README.md`).
- Warehouse/Transform: `dbt_project/` — contiene modelos que consumen los `raw` tables y generan tablas en la base `analytics`.
- Visualización: `streamlit_app/` (ya presente en el repo) que lee desde la base analítica.
- Orquestación/despliegue local: `docker-compose.yml` levanta `clickhouse` y `dbt-runner` según el repositorio.

Notas importantes observadas en el código:

- La ingestión es intencionalmente de dos pasos: primero cargas en tablas `String` en `raw` para evitar errores de tipo, luego `dbt` hace las castings y validaciones.
- El contenedor `dbt-runner` en `docker-compose.yml` ejecuta `dbt run` y `dbt test` automáticamente en el ejemplo.
