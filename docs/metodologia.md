## Metodología — Scrum (plantilla para entrega académica)

Aunque la metodología no está codificada, incluyo aquí la estructura de Scrum
que puedes adaptar al informe de evaluación.

- Roles: Product Owner (profesor/requirements), Scrum Master (tú), Equipo (estudiante/desarrollador).
- Ceremonias: planificación de sprint, daily (breve), review y retrospective.
- Artefactos: Product Backlog, Sprint Backlog, Definition of Done.

Propuesta práctica para este proyecto (sugerida):

- 3 sprints de 2 semanas cada uno:
  - Sprint 1: Diseño y puesta en marcha (docker, ingestión, diagramas, ADRs).
  - Sprint 2: Limpieza y modelos (imputación, dbt models, tests).
  - Sprint 3: Documentación final, visualización y entrega.

EDT (WBS) mínima — ejemplo:

1. Pipeline
  1.1. Ingestión (scripts)
  1.2. Staging (ClickHouse raw)
  1.3. Transformación (dbt)
2. Documentación
3. Visualización

Incluye un cronograma simple en la documentación final (Gantt o tabla por sprint).
