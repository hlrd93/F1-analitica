## Ingestión — pasos reproducibles (basado en `scripts/`)

El repositorio ya incluye dos maneras reproducibles de cargar los CSVs en
ClickHouse:

- Enfoque por Docker (recomendado para evaluación): `scripts/ingest_csvs_with_docker.sh`.
- Enfoque por Python: `scripts/load_csvs_to_clickhouse.py` (usa `clickhouse-connect`).

Resumen de los pasos (tal como están en `scripts/README.md`):

1. Levantar ClickHouse con `docker-compose.yml`:

```bash
docker compose --env-file ./scripts/.env up -d
```

2. Ejecutar el script de ingestión (el mismo loop usado en la carga original):

```bash
chmod +x scripts/ingest_csvs_with_docker.sh
./scripts/ingest_csvs_with_docker.sh
```

3. Verificar conteos (ejemplo):

```bash
docker exec -i clickhouse clickhouse-client --query "SELECT table, sum(rows) AS rows FROM system.parts WHERE database='raw' GROUP BY table ORDER BY table;"
```

Decisiones observadas en el código y su justificación:

- Las tablas `raw.raw_<name>` se crean con todas las columnas como `String` para evitar problemas de parsing en la primera ingestión. Esto aparece en `scripts/load_csvs_to_clickhouse.py`.
- El loader Python reemplaza literal `\\N` por cadena vacía antes de insertar para evitar que ClickHouse lo interprete literalmente.

Recomendaciones para la entrega:

- Mantener la copia exacta de `scripts/ingest_csvs_with_docker.sh` y el `docker-compose.yml` en la carpeta de entrega.
- Documentar en el informe por qué se hace la ingestión en `String` y cómo `dbt` hace el casting posterior. Esto ya está indicado en `scripts/README.md`.
