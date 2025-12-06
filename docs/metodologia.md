## Metodología — Scrum

### Visión General del Proyecto

Implementación de un pipeline de análisis de Fórmula 1 utilizando arquitectura moderna de datos con Docker, ClickHouse y dbt, incluyendo visualización interactiva y documentación completa.

---

## Estructura Scrum

### Roles

- **Product Owner**: Definición de requisitos y priorización del backlog
- **Scrum Master**: Facilitador del proceso, eliminación de impedimentos
- **Equipo de Desarrollo**: Análisis, desarrollo, testing y documentación

### Épica Principal

**EPF-001: Pipeline Completo de Analytics para Fórmula 1 con Visualización Interactiva**

Descripción: Desarrollar e implementar un sistema completo de ingesta, transformación y visualización de datos de Fórmula 1, con arquitectura escalable basada en contenedores y tecnologías de datos modernas.

---

## Sprints (3 sprints de 1 semana)

### Sprint 1: Infraestructura y Ingesta de Datos (Semana 1: 25 Nov - 1 Dic)

**Objetivo Sprint**: Establecer la infraestructura base y validar la ingesta de datos desde fuentes externas.

#### Historias de Usuario

| ID | Título | Descripción | Puntos | Criterios de Aceptación |
|---|---|---|---|---|
| **US-101** | Configurar contenedores Docker para ClickHouse y ambiente local | Como desarrollador, necesito tener un ambiente local reproducible con Docker para poder desarrollar sin dependencias de máquina. | **8** | ✅ docker-compose.yml funcional<br>✅ ClickHouse inicia correctamente<br>✅ Volúmenes persistentes configurados<br>✅ Readme con instrucciones de setup |
| **US-102** | Implementar script de ingesta de CSV a ClickHouse | Como ingeniero de datos, necesito cargar automáticamente los datos CSV del dataset de F1 a ClickHouse para poder procesarlos. | **5** | ✅ Script Python funcional<br>✅ Carga exitosa de 13 tablas<br>✅ Validación de integridad de datos<br>✅ Logging de errores |
| **US-103** | Crear tablas staging en ClickHouse | Como data engineer, necesito normalizar los datos en tablas staging para poder aplicar transformaciones posteriores. | **5** | ✅ Tablas staging creadas<br>✅ Datos sin duplicados<br>✅ Tipos de datos correctos<br>✅ DDL documentado |
| **US-104** | Documentar arquitectura del pipeline | Como stakeholder, necesito documentación clara de la arquitectura para entender el flujo de datos. | **3** | ✅ Diagrama de arquitectura<br>✅ Descripción de componentes<br>✅ Flujo de datos explicado<br>✅ Formatos incluidos |
| **US-105** | Validar conectividad y performance inicial | Como QA engineer, necesito validar que el sistema funciona correctamente y tiene performance aceptable. | **3** | ✅ 26K+ registros ingestados<br>✅ Queries < 1 segundo<br>✅ Sin errores de conexión<br>✅ Report de performance |

**Total Sprint 1: 24 puntos**

---

### Sprint 2: Transformación de Datos y Modelos (Semana 2: 2-8 Dic)

**Objetivo Sprint**: Crear modelos de datos transformados utilizando dbt y validar calidad de datos.

#### Historias de Usuario

| ID | Título | Descripción | Puntos | Criterios de Aceptación |
|---|---|---|---|---|
| **US-201** | Crear modelos dbt de staging (stg_*) | Como data engineer, necesito crear modelos intermedios en dbt para normalizar y limpiar los datos crudos. | **8** | ✅ 6+ modelos stg_ creados<br>✅ Documentación en YAML<br>✅ Tests de no nulos<br>✅ Lineage visible en dbt docs |
| **US-202** | Crear modelos dbt de dimensiones (dim_*) | Como analista, necesito tablas dimensión bien estructuradas para poder hacer análisis multidimensionales. | **5** | ✅ dim_drivers, dim_races creadas<br>✅ Llaves primarias definidas<br>✅ Jerarquías de tiempo implementadas<br>✅ Documentación completa |
| **US-203** | Implementar tabla de hechos (fact_race_results) | Como analista, necesito una tabla de hechos consolidada con métricas clave para análisis de desempeño. | **5** | ✅ Tabla fact_race_results poblada<br>✅ Métricas calculadas correctamente<br>✅ Granularidad race-driver<br>✅ Tests de integridad |
| **US-204** | Crear snapshots dbt para históricos (driver_constructors) | Como analista, necesito registros históricos de cambios de constructores por piloto para análisis de tendencias. | **5** | ✅ Snapshot configurado y corriendo<br>✅ Cambios capturados correctamente<br>✅ Fechas de validez presentes<br>✅ Queries validadas |
| **US-205** | Documentar modelos y generar lineage | Como técnico, necesito documentación clara de todos los modelos para mantener el sistema. | **3** | ✅ README de modelos<br>✅ Documentación YAML completa<br>✅ Lineage graph generado<br>✅ Diccionario de datos |

**Total Sprint 2: 26 puntos**

---

### Sprint 3: Visualización y Entrega Final (Semana 3: 9-15 Dic)

**Objetivo Sprint**: Crear dashboards interactivos, corregir problemas de datos y finalizar documentación.

#### Historias de Usuario

| ID | Título | Descripción | Puntos | Criterios de Aceptación |
|---|---|---|---|---|
| **US-301** | Implementar dashboard de métricas constructores en Streamlit | Como usuario final, necesito un dashboard interactivo que me muestre el desempeño de constructores para tomar decisiones. | **8** | ✅ Dashboard cargado en localhost:8501<br>✅ Filtros por constructor y año<br>✅ 3+ visualizaciones interactivas<br>✅ Performance < 2s por actualización |
| **US-302** | Crear visualización de pilotos con menos cambios de constructor | Como analista, necesito ver qué pilotos tuvieron menos cambios de equipo en los últimos 5 años. | **5** | ✅ Tabla con nombres de pilotos<br>✅ Gráfico de barras en Plotly<br>✅ Datos desde ClickHouse via docker exec<br>✅ Descarga CSV funcional |
| **US-303** | Corregir mapeo de nombres en Streamlit | Como usuario, necesito ver nombres reales de pilotos en lugar de IDs numéricos. | **5** | ✅ Merge correcto con datasets/drivers.csv<br>✅ Rutas absolutas correctas (ROOT/datasets)<br>✅ Debug logs funcionales<br>✅ Pruebas manuales exitosas |
| **US-304** | Generar documentación técnica final y ADRs | Como arquitecto, necesito documentar decisiones arquitectónicas y guías de uso del sistema. | **3** | ✅ ADRs creados para decisiones clave<br>✅ README actualizado<br>✅ Guía de deployment<br>✅ Troubleshooting incluido |
| **US-305** | Crear diagrama de Gantt del proyecto en documentación | Como PM, necesito visualizar el cronograma del proyecto y validar cumplimiento de tiempos. | **3** | ✅ Diagrama Gantt generado<br>✅ 3 sprints visibles<br>✅ Dependencias mostradas<br>✅ Hito de entrega marcado |

**Total Sprint 3: 24 puntos**

---

**Total General: 74 puntos Fibonacci**

---

## Burndown y Avance

### Estimación por Sprint

| Sprint | Puntos Estimados | Puntos Completados | % Completado | Estado |
|--------|-----------------|-------------------|--------------|--------|
| Sprint 1 | 24 | 24 | ✅ 100% | Completado |
| Sprint 2 | 26 | 26 | ✅ 100% | Completado |
| Sprint 3 | 24 | 24 | ✅ 100% | Completado |
| **TOTAL** | **74** | **74** | **✅ 100%** | **EXITOSO** |

---

## Diagrama de Gantt - Cronograma del Proyecto

```
Proyecto: Pipeline Analytics F1
Duración: 3 semanas (25 Nov - 15 Dic 2025)
Escala: Semana

                    Semana 1        Semana 2        Semana 3
                   (Nov 25-Dec1)  (Dec 2-8)       (Dec 9-15)
                    |--------|--------|--------|--------|--------|
Sprint 1
  US-101 Docker     |████████|
  US-102 Ingesta    |████████|
  US-103 Staging    |████████|
  US-104 Arquitect. |████████|
  US-105 Validac.   |████████|
                                |--------|
Sprint 1 Review              |R|
                                |--------|
Sprint 2
  US-201 Staging dbt          |████████|
  US-202 Dimensiones          |████████|
  US-203 Fact Table           |████████|
  US-204 Snapshots            |████████|
  US-205 Documentación        |████████|
                                            |--------|
Sprint 2 Review                        |R|
                                            |--------|
Sprint 3
  US-301 Dashboard Streamlit              |████████|
  US-302 Visualización Pilotos            |████████|
  US-303 Mapeo Nombres                    |████████|
  US-304 Documentación Final              |████████|
  US-305 Diagrama Gantt                   |████████|
                                                        |--------|
Sprint 3 Review / Entrega                         |R|E|
                                                        |--------|

Leyenda: |████████| = Ejecución | |R| = Sprint Review | |E| = Entrega
```

---

## Tabla de Dependencias

```
US-101 Docker          ─────┐
US-102 Ingesta         ──────┤──→ US-103 Staging ─────┐
US-104 Arquitectura    ──────┘                         │
                                                        ├──→ US-105 Validación
                                                        │
US-201 dbt Staging ────┐                               │
US-202 Dimensiones ────┼──→ US-203 Fact Table ──────┐  │
US-204 Snapshots ──────┘                            │  │
                                                     ├──→ US-301 Dashboard Streamlit
                                                     │   ├──→ US-302 Visualización
                                                     │   ├──→ US-303 Mapeo Nombres
                                                     │   ├──→ US-304 Documentación
                                                     │   └──→ US-305 Gantt

US-105 Validación ────────────────────────────────────┐
                                                       └──→ Proyecto COMPLETADO ✅
```

---

## Ceremonias Scrum

### Planificación de Sprint
- **Duración**: 2 horas
- **Participantes**: Product Owner, Scrum Master, Equipo
- **Artefacto**: Sprint Backlog definido y estimado

### Daily Standup
- **Duración**: 15 minutos (asincrónico en este caso)
- **Preguntas**: ¿Qué hice? ¿Qué haré? ¿Bloqueantes?

### Sprint Review
- **Duración**: 1 hora
- **Demostración**: Features completadas funcionales
- **Feedback**: Stakeholders validan resultados

### Retrospectiva
- **Duración**: 1 hora
- **Discusión**: Qué salió bien, qué mejorar, acciones para próximo sprint

---

## Definition of Done (DoD)

Una historia se considera HECHA cuando:

- ✅ Código escrito y revisado
- ✅ Tests unitarios > 80% cobertura
- ✅ Documentación actualizada
- ✅ Integración en rama main
- ✅ Deploy validado en ambiente local
- ✅ Aceptación del Product Owner

---

## Métricas Clave

| Métrica | Sprint 1 | Sprint 2 | Sprint 3 | Total |
|---------|----------|----------|----------|-------|
| **Velocidad (pts)** | 24 | 26 | 24 | 74 |
| **Historias Completadas** | 5/5 | 5/5 | 5/5 | 15/15 |
| **% Completado** | 100% | 100% | 100% | 100% |
| **Bloqueantes** | 0 | 0 | 0 | 0 |
| **Defectos** | 1* | 0 | 1** | 2 |

*Sprint 1: Ruta de datasets incorrecta
**Sprint 3: Merge de nombres fallaba inicialmente

---

## Resumen Ejecutivo

El proyecto **Pipeline Analytics F1** ha sido completado exitosamente en 3 sprints (21 días) con una velocidad promedio de **24.67 puntos por semana**. 

### Logros Principales:
✅ Sistema completo de ingesta de datos (26K+ registros)
✅ Pipeline dbt con 15+ modelos transformados
✅ Dashboard Streamlit interactivo con visualizaciones dinámicas
✅ Documentación técnica completa con ADRs
✅ 100% de historias de usuario completadas
✅ Cero bloqueantes críticos

### Próximas Fases (Futuros Sprints):
- Implementación de ML para predicción de resultados
- Automatización de reportes via airflow
- Expansión a otras series motorsport (F2, F3, MotoGP)
- Implementación de alertas en tiempo real
