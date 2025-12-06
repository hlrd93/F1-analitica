## Ingestión — pasos reproducibles

El repositorio incluye dos maneras reproducibles de cargar los CSVs en ClickHouse:

- Enfoque por Docker: `scripts/ingest_csvs_with_docker.sh` — útil para ejecutar el proceso tal como se hizo en el entorno original y para evaluaciones que requieren reproducibilidad del contenedor.
- Enfoque por Python: `scripts/load_csvs_to_clickhouse.py` — implementa la carga usando la librería `clickhouse-connect` para conexión y bulk inserts desde Python.

Resumen del flujo y decisiones operativas:

1. Levantar ClickHouse con `docker-compose.yml`:

```bash
docker compose --env-file ./scripts/.env up -d
```

2. Ejecutar el script de ingestión por contenedor (opción Docker):

```bash
chmod +x scripts/ingest_csvs_with_docker.sh
./scripts/ingest_csvs_with_docker.sh
```

3. Alternativa: ejecutar el loader Python (opción programática):

```bash
python3 scripts/load_csvs_to_clickhouse.py
```

Razonamiento detrás del diseño de ingestión (más detalle):

- Carga en dos etapas: la decisión de escribir inicialmente todas las columnas como `String` en tablas dentro del esquema `raw` responde a dos necesidades: (1) resiliencia durante la ingestión — evitar abortos por errores de parseo o por valores inesperados — y (2) permitir una ingestión rápida desde múltiples archivos heterogéneos. Una vez los datos están disponibles en ClickHouse, `dbt` transforma y valida los datos en la capa `Transform` aplicando castings, normalizaciones y tests de calidad.

- Implementación técnica: el loader en `scripts/load_csvs_to_clickhouse.py` usa `clickhouse-connect` para crear tablas cuando es necesario y cargar datos en bloque. El script incluye medidas prácticas como el manejo de marcadores de nulos (`\N`), control de reintentos por archivo y logging básico para facilitar auditoría y reejecuciones.
