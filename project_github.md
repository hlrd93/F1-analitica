# Presentación del Proyecto - F1 Analytics Pipeline

**Estudiante:** Herwin Leonardo Rey Diaz 
**Programa:** Maestría en Ciencia de Datos - Universidad Católica del Uruguay (UCU)  
**Fecha:** Diciembre 2025

---

## 📖 Documentación Completa con MkDocs

> **⚠️ IMPORTANTE:** Para visualizar la **documentación completa del proyecto**, incluyendo arquitectura, metodología, diagramas y decisiones técnicas, debe levantar el servidor MkDocs.

### Cómo Acceder a la Documentación

```bash
# 1. Instalar MkDocs (si no está instalado)
pip install mkdocs-material

# 2. Compilar la documentación
mkdocs build

# 3. Levantar el servidor local
mkdocs serve

# 4. Abrir en el navegador
# La documentación estará disponible en: http://localhost:8000
```

La documentación en MkDocs incluye:
- 🏗️ **Arquitectura** - Diagramas del pipeline y componentes
- 📊 **Metodología** - Enfoque y decisiones metodológicas
- 🔧 **Implementación** - Guías técnicas detalladas
- 💉 **Ingesta de datos** - Proceso ETL/ELT
- 📸 **Snapshots** - SCD Type 2
- 🎯 **Casos de uso** - Ejemplos de análisis
- 📋 **ADR** - Architecture Decision Records

---

## 📍 Ubicación del Proyecto

### Repositorio GitHub
- **URL:** https://github.com/hlrd93/F1-analitica
- **Branch Principal:** `main`
- **Visibilidad:** Público

### Documentación en Línea
- **Sitio MkDocs:** https://hlrd93.github.io/F1-analitica/ 
- **Documentación local:** Disponible en el directorio `/docs`

---

## 🎯 Descripción del Proyecto

Pipeline de análisis de datos de Fórmula 1 construido con arquitectura ELT moderna, utilizando ClickHouse como motor OLAP columnar, dbt para transformaciones SQL, y Streamlit para visualizaciones interactivas.

### Objetivo Principal
Implementar un pipeline de datos end-to-end que cumpla con los requisitos académicos de la maestría UCU, demostrando:
- Modelado dimensional (Star Schema)
- Procesos ETL/ELT automatizados
- Calidad de datos con tests automatizados
- Visualización mediante dashboards interactivos
- Documentación técnica completa

---

## 🏗️ Arquitectura Técnica

```
┌─────────────┐
│  CSV Files  │
│  (datasets/)│
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Python Ingestion   │
│  load_csvs_to_ch.py │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  ClickHouse RAW     │
│  (raw.raw_*)        │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  dbt Transformations│
│  (models/)          │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ClickHouse Analytics │
│ (analytics.*)       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Streamlit Dashboard │
│ (streamlit_app/)    │
└─────────────────────┘
```

---

## 💻 Stack Tecnológico

| Componente | Tecnología | Propósito |
|------------|-----------|-----------|
| **Base de datos OLAP** | ClickHouse | Almacenamiento columnar de alto rendimiento |
| **Transformaciones** | dbt (Data Build Tool) | Transformaciones SQL con tests y docs |
| **Orquestación** | Docker Compose | Containerización y despliegue |
| **Visualización** | Streamlit | Dashboards interactivos |
| **Análisis exploratorio** | Pandas | EDA y generación de reportes |
| **Control de versiones** | Git/GitHub | Versionado de código |
| **Documentación** | MkDocs Material | Documentación técnica |

---

## 📂 Estructura del Repositorio

```
F1-analitica/
│
├── datasets/                    # Datos fuente (CSV de Fórmula 1)
│   ├── circuits.csv
│   ├── races.csv
│   ├── drivers.csv
│   ├── constructors.csv
│   ├── results.csv
│   └── ... (más tablas)
│
├── scripts/                     # Scripts de ingesta
│   ├── load_csvs_to_clickhouse.py
│   ├── ingest_csvs_with_docker.sh
│   ├── eda_pandas.py
│   └── .env (configuración)
│
├── dbt_project/                 # Proyecto dbt
│   ├── models/
│   │   ├── staging/            # Capa de staging
│   │   │   └── stg_races.sql
│   │   ├── dim/                # Tablas de dimensión
│   │   │   └── dim_fecha.sql
│   │   ├── fact/               # Tablas de hechos
│   │   │   └── fact_race_results.sql
│   │   └── marts/              # Data marts
│   ├── snapshots/              # SCD Type 2
│   │   └── driver_constructors_snapshot.sql
│   ├── dbt_project.yml
│   └── profiles.yml.example
│
├── streamlit_app/              # Dashboard interactivo
│   ├── constructor_dashboard.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docs/                       # Documentación MkDocs
│   ├── architecture.md
│   ├── implementation.md
│   ├── metodologia.md
│   ├── ingestion.md
│   ├── snapshots.md
│   ├── use_case.md
│   └── adr/                    # Architecture Decision Records
│
├── docker-compose.yml          # Orquestación de servicios
├── environment.yml             # Ambiente Conda
├── mkdocs.yml                  # Configuración MkDocs
└── README.md                   # Documentación principal
```

---

## 🚀 Cómo Ejecutar el Proyecto

### Prerrequisitos
- Docker y Docker Compose instalados
- Python 3.9+ (para desarrollo local)
- Conda (opcional)

### Pasos de Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/hlrd93/F1-analitica.git
cd F1-analitica

# 2. Configurar variables de entorno
cat > scripts/.env << EOF
CLICKHOUSE_HOST=clickhouse
CLICKHOUSE_PORT=9000
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=
EOF

# 3. Levantar ClickHouse
docker-compose up -d clickhouse

# 4. Ingestar datos
python scripts/load_csvs_to_clickhouse.py

# 5. Ejecutar transformaciones dbt
docker-compose up dbt-runner

# 6. Lanzar dashboard
cd streamlit_app
streamlit run constructor_dashboard.py
```

---

## 📊 Componentes Implementados

### 1. Capa de Ingesta (Raw Layer)
- **Script:** `scripts/load_csvs_to_clickhouse.py`
- **Función:** Carga CSVs a ClickHouse en schema `raw`
- **Características:**
  - Lectura automática de esquema desde CSVs
  - Manejo de valores nulos (`\\N`)
  - Carga por lotes (BATCH_SIZE=10000)
  - Creación automática de bases de datos

### 2. Capa de Transformación (Analytics Layer)
- **Herramienta:** dbt
- **Modelos implementados:**
  - `staging/stg_races.sql` - Normalización de carreras
  - `dim/dim_fecha.sql` - Dimensión temporal
  - `fact/fact_race_results.sql` - Hechos de resultados
- **Características:**
  - Tests de calidad de datos
  - Documentación en `schema.yml`
  - Snapshots SCD Type 2

### 3. Capa de Visualización
- **Dashboard:** `streamlit_app/constructor_dashboard.py`
- **Funcionalidad:** Análisis interactivo de constructores
- **Características:**
  - Filtros dinámicos
  - Gráficos interactivos
  - Conexión directa a ClickHouse Analytics

### 4. Análisis Exploratorio
- **Script:** `scripts/eda_pandas.py`
- **Output:** `datasets/eda_report.md`
- **Incluye:**
  - Estadísticas descriptivas por tabla
  - Detección de valores faltantes
  - Análisis de unicidad
  - Distribuciones de variables

---

## ✅ Requisitos Académicos Cumplidos

| Requisito | Estado | Evidencia |
|-----------|--------|-----------|
| Modelado dimensional (Star Schema) | ✅ | `dbt_project/models/dim/` y `fact/` |
| Procesos ETL/ELT | ✅ | `scripts/load_csvs_to_clickhouse.py` + dbt |
| Calidad de datos | ✅ | Tests dbt en `schema.yml` |
| Dashboards BI | ✅ | `streamlit_app/constructor_dashboard.py` |
| Documentación completa | ✅ | `docs/` + `README.md` |
| SCD Type 2 | ✅ | `dbt_project/snapshots/` |
| Containerización | ✅ | `docker-compose.yml` + Dockerfiles |

---

## 📖 Documentación Disponible

### En el Repositorio
1. **README.md** - Guía principal del proyecto
2. **docs/architecture.md** - Arquitectura del pipeline
3. **docs/implementation.md** - Referencias al código
4. **docs/metodologia.md** - Enfoque metodológico
5. **docs/ingestion.md** - Proceso de ingesta
6. **docs/snapshots.md** - SCD Type 2
7. **docs/use_case.md** - Casos de uso
8. **docs/adr/** - Decisiones de arquitectura

### Generada
- **datasets/eda_report.md** - Reporte de análisis exploratorio
- **dbt_project/target/** - Documentación dbt compilada

---

## 🔍 Puntos Destacados del Proyecto

### Modelado Dimensional
- Implementación de **Star Schema** con tablas de dimensión y hechos
- Dimensión temporal (`dim_fecha`) con granularidad diaria
- Snapshots para rastrear cambios históricos (SCD Type 2)

### Calidad de Datos
- Tests automatizados con dbt:
  - Unicidad de claves primarias
  - Integridad referencial
  - Valores no nulos en campos críticos
  - Valores aceptados en campos categóricos

### Performance
- ClickHouse como motor OLAP columnar
- Optimización de consultas con índices
- Carga por lotes en la ingesta

### Buenas Prácticas
- Código versionado en Git
- Containerización con Docker
- Documentación como código (MkDocs)
- Separación de ambientes (raw/analytics)
- Variables de entorno para configuración

---

## 🎓 Contexto Académico

**Universidad:** Universidad Católica del Uruguay (UCU)  
**Programa:** Maestría en Ciencia de Datos  
**Materia:** Gestión y Gobernanza de Datos *(o materia correspondiente)*  
**Período:** 2025

### Objetivos de Aprendizaje Demostrados
1. Diseño e implementación de pipelines de datos
2. Modelado dimensional para análisis
3. Uso de herramientas modernas de ingeniería de datos
4. Gestión de calidad de datos
5. Documentación técnica profesional

---

## 📧 Contacto

**Estudiante:** Herwin  
**GitHub:** [@hlrd93](https://github.com/hlrd93)  
**Repositorio:** [F1-analitica](https://github.com/hlrd93/F1-analitica)

---

## 📝 Notas para Revisión

### Para Ejecutar el Proyecto
1. El repositorio es **público** y accesible desde cualquier lugar
2. Todos los scripts y configuraciones están incluidos
3. Los datos están en el directorio `datasets/`
4. La documentación está completa en `docs/` y `README.md`

### Para Evaluación
- El código está organizado por capas (raw → analytics)
- Cada componente tiene su directorio claramente identificado
- La documentación explica el propósito de cada archivo
- Los commits en Git muestran la evolución del proyecto

---

<p align="center">
  <strong>Proyecto desarrollado con dedicación para UCU 🎓</strong>
</p>
