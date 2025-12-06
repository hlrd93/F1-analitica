## Caso de Uso

Objetivo principal

Proveer un pipeline reproducible que transforme los CSVs originales en
tablas analíticas hospedadas en ClickHouse para permitir análisis exploratorio
y visualizaciones con `streamlit_app/`.

Actores

- Data Engineer: prepara el entorno, ejecuta la ingestión y mantiene scripts.
- Analista: ejecuta dbt, valida los modelos y crea visualizaciones.
- Profesor/Reviewer: valida reproducibilidad y calidad de datos.

Entradas

- CSVs en `datasets/` (drivers, races, lap_times, etc.).

Salidas

- Tablas staging en la base `raw` de ClickHouse (`raw.raw_<name>`).
- Tablas transformadas en la base `analytics` (generadas por `dbt`).
- Documentación en `docs/` y visualizaciones en `streamlit_app/`.

Escenarios principales

1. Flujo normal
   - Levantar ClickHouse con `docker compose --env-file ./scripts/.env up -d`.
   - Ejecutar `scripts/ingest_csvs_with_docker.sh` o `scripts/load_csvs_to_clickhouse.py`.
   - Ejecutar `dbt run` (el repo incluye `dbt-runner` en `docker-compose.yml`).
   - Verificar tablas en `analytics` y abrir `streamlit_app/` para visualización.

2. Reprocesado por calidad de datos
   - Si `generate_datasets_profile.py` muestra columnas con nulos o tipos incorrectos,
     editar scripts de transformación en `dbt_project/` y re-run `dbt`.

3. Entrega académica
   - Generar site MkDocs con toda la documentación y exportar a PDF/HTML para el profesor.

Criterios de éxito

- Reproducibilidad: siguiendo las instrucciones, el evaluador puede levantar el entorno y
  obtener las mismas tablas y conteos reportados en `scripts/README.md`.
- Calidad: modelos dbt pasan `dbt test` o se documentan claramente los tests fallidos.
- Documentación: incluye arquitectura, metodologías y ADRs para justificar decisiones.
