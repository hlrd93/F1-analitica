{% snapshot driver_constructors_snapshot %}
{{
  config(
    target_schema='analytics',
    unique_key='driverId',
    strategy='check',
    check_cols=['constructorId'],
    alias='driver_constructors_snapshot'
  )
}}

-- Snapshot that tracks which constructor each driver raced for.
-- Uses `check` strategy on constructorId so a new SCD record is created
-- whenever a driver's constructor changes.

select
  driverId,
  constructorId,
  -- keep the race-level date/key so we can filter by recent years when
  -- analysing changes. `fact_race_results` provides `sk_fecha` (YYYYMMDD int).
  sk_fecha
from {{ ref('fact_race_results') }}

{% endsnapshot %}
