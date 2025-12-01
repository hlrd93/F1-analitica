{{
  config(
    materialized='table'
  )
}}

-- Time-series per constructor: rolling metrics over the last 12 races
with races_with_date as (
  select
    toUInt32(raceId) as race_id,
    toDate(date) as race_date
  from raw.raw_races
),

results_parsed as (
  select
    toUInt32(resultId) as result_id,
    toUInt32(raceId) as race_id,
    toUInt32(constructorId) as constructor_id,
    toInt64(positionOrder) as position_order,
    toFloat32OrNull(point) as points
  from raw.raw_results
),

joined as (
  select
    r.*,
    rw.race_date
  from results_parsed r
  left join races_with_date rw using (race_id)
),

with_rn as (
  select
    constructor_id,
    race_id,
    race_date,
    position_order,
    points,
    row_number() over (partition by constructor_id order by race_date asc, race_id asc) as rn
  from joined
),

rolling as (
  select
    constructor_id,
    race_id,
    race_date,
    rn,
    -- last 12 races rolling counts using frame of 11 preceding rows + current
    sumIf(position_order <= 3, 1) over (partition by constructor_id order by race_date asc, race_id asc rows between 11 preceding and current row) as podiums_last_12,
    count() over (partition by constructor_id order by race_date asc, race_id asc rows between 11 preceding and current row) as races_last_12,
    -- average points over the window
    avg(points) over (partition by constructor_id order by race_date asc, race_id asc rows between 11 preceding and current row) as avg_points_last_12
  from with_rn
)

select
  rt.constructor_id,
  c.name as constructor_name,
  rt.race_date,
  rt.race_id,
  rt.rn,
  coalesce(rt.podiums_last_12,0) as podiums_last_12,
  coalesce(rt.races_last_12,0) as races_last_12,
  case when rt.races_last_12 = 0 then 0 else round(rt.podiums_last_12 / rt.races_last_12,6) end as recent_podium_rate,
  round(coalesce(rt.avg_points_last_12,0),3) as avg_points_last_12
from rolling rt
left join raw.raw_constructors c on c.constructorId::UInt32 = rt.constructor_id

-- partition by constructor+date; materialized as table for efficient Tableau time-series queries
