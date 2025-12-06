## Driver -> Constructor SCD (Type 2)
## Snapshot SCD Type 2 — Driver → Constructor

Esta página documenta el snapshot de dbt que añadimos para registrar, como SCD Type 2, el histórico de asignaciones "piloto → constructor".

Objetivo
- Mantener el historial completo de qué constructor tenía cada piloto en cada punto del tiempo. Con esto podemos responder preguntas como "¿cuántas veces cambió de equipo el piloto X?" o calcular métricas por periodo.

Ubicación en el repositorio
- Definición del snapshot: `dbt_project/snapshots/driver_constructors_snapshot.sql`
- Metadatos del snapshot: `dbt_project/snapshots/snapshots.yml`
- Tabla materializada en ClickHouse: `analytics.driver_constructors_snapshot`

Cómo funciona (resumen)
- Estrategia: `check` sobre la columna `constructorId`. En cada ejecución de `dbt snapshot` dbt compara `constructorId` para cada `driverId`; si cambia, inserta una nueva fila y actualiza `dbt_valid_to` de la fila anterior.
- Columnas SCD2 típicas generadas por dbt:
  - `dbt_scd_id` (surrogate id interno, UInt64)
  - `driverId` (clave única por piloto)
  - `constructorId` (equipo asignado)
  - `sk_fecha` (fecha/clave de carrera, UInt32)
  - `dbt_updated_at` (timestamp del snapshot run)
  - `dbt_valid_from` (fecha/hora en que esta versión empezó a ser válida)
  - `dbt_valid_to` (fecha/hora en que dejó de ser válida; NULL = vigente)

Estado observado
- Tras ejecutar `dbt snapshot --select driver_constructors_snapshot` la tabla `analytics.driver_constructors_snapshot` quedó creada y poblada (aprox. 26.7k filas en la comprobación inicial).

Esquema (salida de DESCRIBE TABLE)

```
driverId        String
constructorId   String
sk_fecha        UInt32
dbt_scd_id      UInt64
dbt_updated_at  DateTime
dbt_valid_from  DateTime
dbt_valid_to    Nullable(DateTime)
```

Comandos listos para copiar y pegar (Docker)

Los siguientes comandos están preparados para ejecutarse desde tu terminal y llaman a `clickhouse-client` dentro del contenedor Docker `clickhouse` (no hace falta instalar el cliente localmente):

- Ver el esquema de la tabla (DESCRIBE TABLE):

```bash
docker exec -it clickhouse clickhouse-client --query "DESCRIBE TABLE analytics.driver_constructors_snapshot"
```

- Conteo total de filas en el snapshot:

```bash
docker exec -it clickhouse clickhouse-client --query "SELECT count() FROM analytics.driver_constructors_snapshot"
```

- Top-10 pilotos que MENOS cambiaron de equipo en los últimos 5 años (conteo de equipos distintos):

```bash
docker exec -it clickhouse clickhouse-client --query "\
SELECT driverId, countDistinct(constructorId) AS n_teams \
FROM analytics.driver_constructors_snapshot \
WHERE dbt_valid_from >= subtractYears(now(), 5) \
GROUP BY driverId \
ORDER BY n_teams ASC, driverId ASC \
LIMIT 10;"
```

- Top-10 pilotos por menor número de transiciones (cambios entre versiones consecutivas) en los últimos 5 años — utiliza funciones de ventana:

```bash
docker exec -it clickhouse clickhouse-client --query "\
SELECT driverId, sumIf(1, prev_c != constructorId) AS n_transitions \
FROM ( \
  SELECT driverId, constructorId, lag(constructorId) OVER (PARTITION BY driverId ORDER BY dbt_valid_from) AS prev_c \
  FROM analytics.driver_constructors_snapshot \
  WHERE dbt_valid_from >= subtractYears(now(), 5) \
) \
GROUP BY driverId \
ORDER BY n_transitions ASC \
LIMIT 10;"
```

- Ver una muestra de filas (ej.: 10 filas):

```bash
docker exec -it clickhouse clickhouse-client --query "SELECT driverId, constructorId, dbt_valid_from, dbt_valid_to FROM analytics.driver_constructors_snapshot ORDER BY driverId LIMIT 10"
```

Ejecutar el snapshot (dbt)

Si quieres materializar (o refrescar) el snapshot con dbt desde Docker:

```bash
docker compose run --rm dbt-runner bash -lc "dbt snapshot --select driver_constructors_snapshot --profiles-dir /root/.dbt -t dev"
```

O desde tu entorno local (si ejecutas dbt localmente):

```bash
# situándote en la carpeta dbt_project/
dbt snapshot --select driver_constructors_snapshot -t dev
```

Notas y recomendaciones
- Las filas con `dbt_valid_to = \\N` son las versiones vigentes (actuales) — esto es el comportamiento SCD Type 2 esperado.
- Para presentaciones y pruebas reproducibles puedes usar los comandos anteriores y pegar la salida en la documentación para mostrar ejemplos reales.

## Resultados de la verificación

A continuación se muestra la tabla con los Top-10 pilotos activos (han corrido en los últimos 5 años) que menos equipos distintos han tenido en ese periodo, calculada a partir de `analytics.fact_race_results` JOIN `analytics.stg_races`.

| Rank | driverId | Piloto | n_teams |
|------:|---------:|:-------|--------:|
| 1 | 1 | Lewis Hamilton | 1 |
| 2 | 8 | Kimi Räikkönen | 1 |
| 3 | 825 | Kevin Magnussen | 1 |
| 4 | 826 | Daniil Kvyat | 1 |
| 5 | 830 | Max Verstappen | 1 |
| 6 | 841 | Antonio Giovinazzi | 1 |
| 7 | 844 | Charles Leclerc | 1 |
| 8 | 846 | Lando Norris | 1 |
| 9 | 849 | Nicholas Latifi | 1 |
| 10 | 850 | Pietro Fittipaldi | 1 |

Estos resultados verifican que la consulta que restringe a pilotos activos en los últimos 5 años produce un ranking coherente con los datos en `analytics`.
