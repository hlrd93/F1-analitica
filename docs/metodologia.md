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


## Resumen Ejecutivo - Cierre Q4 2025

### Estado del Proyecto: ✅ COMPLETADO EN TIEMPO Y FORMA

El proyecto **Pipeline Analytics F1** ha alcanzado exitosamente la fase de Go-Live en Q4 2025 (21 días), cumpliendo con todos los objetivos estratégicos definidos en el roadmap inicial. El equipo de desarrollo completó **15/15 historias de usuario (100%)** sin incidentes críticos en producción.

---

### Métricas de Desempeño Q4

| Métrica | Objetivo | Alcanzado | Estado |
|---------|----------|-----------|--------|
| **Historias de Usuario Completadas** | 15 | 15 | ✅ 100% |
| **Defectos Críticos** | 0 | 0 | ✅ 0 bugs |
| **Cobertura de Requerimientos** | 100% | 100% | ✅ Completo |
| **Cumplimiento de Timeline** | 21 días | 21 días | ✅ On-time |
| **Velocidad del Equipo** | 24+ pts/sem | 24.67 pts/sem | ✅ Above Target |
| **Disponibilidad Sistema** | 99.9% | 100% | ✅ Uptime |

---

### Logros Entregados al Cliente

**Infraestructura & Datos:**
- ✅ Pipeline automatizado de ingesta: **26,759 registros** procesados sin pérdida de datos
- ✅ Data warehouse escalable: ClickHouse con particionamiento por año y constructor
- ✅ 13 tablas staging + 6 modelos transformados (dbt) listos para producción

**Analytics & Visualización:**
- ✅ Dashboard Streamlit interactivo con **5+ visualizaciones dinámicas**
- ✅ KPIs en tiempo real: desempeño constructor, historial piloto, cambios de equipo
- ✅ Exportación de reportes en CSV para integración con sistemas legacy

**Calidad & Documentación:**
- ✅ **0 defectos críticos** atendidos en Q4
- ✅ Documentación técnica completa: ADRs, arquitectura, lineage de datos
- ✅ Runbooks operacionales para on-call engineers

---

### Roadmap Refinado - Sprint Backlog Q1 2026

#### Preparado para Ejecución Inmediata

| Épica | Historia | Equipo Asignado | Estado | Puntos |
|-------|---------|-----------------|--------|--------|
| **IA/ML Enhancement** | US-401: Modelo predictivo de victorias (SPIKE) | Data Science + ML Eng | 🔵 Discovery | 13 |
| **Automation** | US-402: Pipeline Airflow para jobs dbt (Refinado) | DE + DevOps | 🟢 Ready | 8 |
| **Expansion** | US-403: Integración F2 Championship (SPIKE) | Data Architect | 🔵 Discovery | 13 |
| **Observability** | US-404: Alertas tiempo real cambios équipos | Backend Eng + Analytics | 🟢 Ready | 5 |
| **Scale** | US-405: Migración a Data Lake (Refinado) | Cloud Arch + DE | 🟢 Ready | 8 |

**Total Backlog Refinado:** 47 puntos (4-5 semanas de trabajo)

---

#### Historias en Discovery/Refinamiento (Spike en Progreso)

| Épica | Historia | Propósito | Entrega Spike |
|-------|---------|-----------|----------------|
| **IA/ML Enhancement** | US-401 | Estimar esfuerzo para predicción de resultados con datos históricos F1 | 15 Dic 2025 |
| **Expansion** | US-403 | Validar compatibilidad de datos F2, mapeo de pilotos/constructores | 22 Dic 2025 |

---

### Equipo de Desarrollo Asignado

| Rol | Nombre | Asignación Q1 | Disponibilidad |
|-----|--------|--------------|----------------|
| **Tech Lead / Data Architect** | - | US-402, US-405 (leadership) | 80% |
| **Data Engineer Senior** | - | US-402, US-405, US-403 (support) | 100% |
| **ML Engineer / Data Scientist** | - | US-401 (spike + implementation) | 100% |
| **Backend Engineer** | - | US-404 implementation | 50% |
| **DevOps / Cloud Architect** | - | US-405 infrastructure | 60% |

---

### Puntos de Contacto Siguientes

- **Sprint Planning Q1:** 8 Enero 2026
- **Spike Deliverables:** 15-22 Diciembre 2025
- **Status Review Mensual:** Último viernes de cada mes, 10:00 AM CET
- **POC Técnico:** arquitecto@project.com

---

### Riesgos Identificados & Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|--------|-----------|
| Volumen F2 supera capacidad actual | Media | Alto | US-405 (scale infrastructure) |
| Latencia en dashboard al agregar F2 | Media | Medio | Indexación + caché Redis (US-404) |
| Continuidad equipo ML | Baja | Alto | Documentación modelos, pair programming |

