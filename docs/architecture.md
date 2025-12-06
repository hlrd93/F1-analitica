## Arquitectura del Pipeline

El diagrama muestra la estructura del pipeline tal y como está implementada en este repositorio.

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

Descripción de componentes:

- Origen: `datasets/` — CSVs de entrada (drivers, races, lap_times, etc.) que sirven como fuentes primarias para el pipeline. Los archivos de ejemplo se encuentran en la carpeta `datasets/` del repositorio.
- Ingestor (staging): cargas reproducibles mediante los scripts en `scripts/`. El flujo práctico que seguimos fue:
  - Primero se colocan los datos en tablas `raw.raw_<name>` con columnas definidas como `String` para evitar fallos de parsing y acelerar la ingestión inicial. Esto permite incorporar datos heterogéneos sin abortar la carga.
  - A continuación se muestra un extracto simplificado (ejemplo) que refleja la aproximación usada en `scripts/load_csvs_to_clickhouse.py` (usa `clickhouse-connect`):

```python
# extract: simplified example of the loader pattern used in "scripts/load_csvs_to_clickhouse.py"
import csv
from clickhouse_connect import Client

client = Client(host='localhost', port=8123, username='default')

def create_raw_table(table_name, columns):
    cols_sql = ', '.join(f'`{c}` String' for c in columns)
    ddl = (
        f"CREATE TABLE IF NOT EXISTS raw.{table_name} (" + cols_sql + ") "
        "ENGINE = MergeTree() ORDER BY tuple()"
    )
    client.command(ddl)

def load_csv_to_table(csv_path, table_name, batch_size=10000):
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        create_raw_table(table_name, header)
        batch = []
        for row in reader:
            # replace ClickHouse-null-marker if present
            row = [None if v == '\\N' else v for v in row]
            batch.append(row)
            if len(batch) >= batch_size:
                client.insert(f"raw.{table_name}", batch, column_names=header)
                batch = []
        if batch:
            client.insert(f"raw.{table_name}", batch, column_names=header)
```

- Por qué este diseño y cuáles son las ventajas:
  - Resiliencia en ingestión: escribir inicialmente todo como `String` evita que filas sucias o columnas con formatos inesperados provoquen fallos y paradas en la carga.
  - Rendimiento: el uso de inserciones en bloque (batch inserts) reduce el overhead de la conexión y las latencias de red al agrupar filas. `clickhouse-connect` puede usar el protocolo nativo y formatos optimizados (por ejemplo, inserción en bloque CSV o en formatos columnar cuando esté disponible), lo que es sustancialmente más rápido que insertar fila a fila.
  - Paralelización y reintentos: procesar un archivo por tarea (o varios en paralelo) facilita reintentos por archivo y mejora la utilización de recursos (IO/CPU) sin perder consistencia en el resto de los datos.
  - Separación de preocupaciones: al delegar_CASTs y validaciones a `dbt` en la etapa Transform, se mantiene la carga inicial rápida y simple, mientras que las reglas de negocio, tipos y tests se aplican en una capa diseñada para eso (dbt). Esto simplifica la trazabilidad y las correcciones posteriores.

- Warehouse / Transform: `dbt_project/` — contiene los modelos que consumen las tablas `raw` y aplican castings, validaciones y reglas de negocio para producir las tablas en la base `analytics`. Las pruebas (`dbt test`) y los snapshots allí definidos ayudan a asegurar la calidad de los modelos.
- Visualización: `streamlit_app/` — dashboard que consume las tablas en `analytics` y ofrece vistas interactivas.
- Visualización: `streamlit_app/` — dashboard que consume las tablas en `analytics` y ofrece vistas interactivas.

Sección destacada — SCD Type 2 (Driver -> Constructor)

En este proyecto hemos añadido un snapshot dbt que implementa un SCD Type 2 para rastrear los cambios de constructor por piloto. La definición está en `dbt_project/snapshots/driver_constructors_snapshot.sql` y la tabla materializada en ClickHouse es `analytics.driver_constructors_snapshot`.

Resumen rápido:

- Estrategia: `check` sobre `constructorId` — dbt crea una nueva fila cuando `constructorId` cambia para un `driverId`.
- Columnas relevantes: `driverId`, `constructorId`, `sk_fecha`, `dbt_scd_id`, `dbt_updated_at`, `dbt_valid_from`, `dbt_valid_to`.
- Uso: esta tabla permite analizar historial de movimientos de pilotos entre equipos (por ejemplo, calcular cuántos cambios tuvo un piloto en los últimos N años o identificar pilotos que rara vez cambian de equipo).

Hay una página dedicada con más detalles y ejemplos de consultas: [Snapshots](/snapshots/).
- Orquestación / despliegue local: `docker-compose.yml` arranca los servicios necesarios (ClickHouse, y un contenedor `dbt-runner` usado para ejecutar comandos dbt en el entorno de desarrollo).

Notas importantes observadas en el código (explicadas):

- Diseño de la ingestión en dos pasos: la ingestión inicial escribe todos los campos como `String` en esquema `raw` para minimizar los puntos de fallo durante la carga (por ejemplo, formatos inconsistentes, valores nulos o marcadores especiales). Posteriormente, los modelos `dbt` realizan los castings a los tipos esperados, aplican transformaciones y validaciones (por ejemplo, convertir columnas de fecha, normalizar identificadores y validar cardinalidades). Este patrón reduce el tiempo de carga y separa las preocupaciones entre ingestión y transformación.

- Implementación concreta del loader: `scripts/load_csvs_to_clickhouse.py` muestra una implementación en Python que utiliza `clickhouse-connect` para conectarse a ClickHouse, crear tablas `raw.raw_<name>` cuando es necesario y bulk-insertar filas. El script incluye manejo básico de valores especiales (p. ej. reemplazo de `\\N`) y particionado por archivos para facilitar reintentos.

- Uso de `dbt` dentro de contenedores: el `dbt-runner` definido en `docker-compose.yml` se usa en este repositorio para ejecutar tareas de transformación y pruebas (`dbt run`, `dbt test`) en un entorno controlado. Esto permite que las transformaciones sean reproducibles y que las pruebas de contratos (tests de dbt) se ejecuten de forma consistente en CI/local.
