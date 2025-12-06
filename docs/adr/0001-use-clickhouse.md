# ADR 0001: Usar ClickHouse como almacén analítico

Status: Accepted

Date: 2025-12-06

Context:

- El repositorio incluye un servicio `clickhouse` definido en `docker-compose.yml`.
- Los datos de entrada son CSVs tabulares (datasets/). Se requieren consultas analíticas rápidas para dashboards y agregaciones.

Decision:

- Usar ClickHouse como almacén analítico principal. Se usa una base `raw` para ingestión inicial y una base `analytics` para los resultados transformados por `dbt`.

Consecuencias:

- Ventajas: alto rendimiento en consultas analíticas, buenas capacidades de compresión y escalado para cargas de datos históricas.
- Costes: ClickHouse requiere diseño cuidadoso de `ORDER BY` y tipos para obtener máximo rendimiento; la ingestión inicial realiza staging con `String` para evitar parseos al vuelo.

Alternativas consideradas:

- PostgreSQL (fácil de usar, pero menos óptimo para OLAP en grandes volúmenes) — descartado por rendimiento en consultas analíticas.

Referencias en el repo:

- `docker-compose.yml` (servicio clickhouse)
- `scripts/load_csvs_to_clickhouse.py` (crea bases `raw` y `analytics`, y carga CSVs)
