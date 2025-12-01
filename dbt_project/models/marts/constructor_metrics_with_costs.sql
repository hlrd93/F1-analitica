{{
  config(
    materialized='table'
  )
}}

-- Variant of constructor_metrics that uses a real cost table `raw.raw_constructor_costs`.
-- This model will fail if the source table does not exist. Create or load
-- `raw.raw_constructor_costs` with columns (constructorId, cost_amount) to use it.

with races_with_date as (
  select
    toUInt32(raceId) as race_id,
    toDate(date) as race_date,
    toUInt16(year) as race_year
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
    rw.race_date,
    rw.race_year
  from results_parsed r
  left join races_with_date rw using (race_id)
),

per_constructor as (
  select
    c.constructorId::UInt32 as constructor_id,
    c.name as constructor_name,
    min(j.race_year) as first_year,
    max(j.race_year) as last_year,
    countDistinct(j.race_id) as total_races,
    sum(if(j.position_order <= 3, 1, 0)) as total_podiums,
    avg(j.position_order) as avg_position,
    avg(j.points) as avg_points_per_race
  from raw.raw_constructors c
  left join joined j on j.constructor_id = c.constructorId::UInt32
  group by c.constructorId::UInt32, c.name
),

last_races as (
  select
    constructor_id,
    race_id,
    race_date,
    position_order,
    points,
    row_number() over (partition by constructor_id order by race_date desc, race_id desc) as rn
  from joined
),

recent as (
  select
    constructor_id,
    sum(if(position_order <= 3, 1, 0)) filter (where rn <= 12) as podiums_last_12,
    sum(if(rn <= 12, 1, 0)) as races_last_12
  from last_races
  group by constructor_id
),

base as (
  select
    p.constructor_id,
    p.constructor_name,
    coalesce(p.total_races,0) as total_races,
    coalesce(p.total_podiums,0) as total_podiums,
    case when coalesce(p.total_races,0) = 0 then 0 else round(p.total_podiums / p.total_races, 6) end as podium_rate,
    round(coalesce(p.avg_points_per_race,0),3) as avg_points_per_race,
    round(coalesce(p.avg_position,0),3) as avg_position,
    coalesce(r.podiums_last_12,0) as podiums_last_12,
    coalesce(r.races_last_12,0) as races_last_12,
    case when coalesce(r.races_last_12,0)=0 then 0 else round(r.podiums_last_12 / r.races_last_12,6) end as recent_podium_rate,
    (p.last_year - p.first_year + 1) as seasons_active
  from per_constructor p
  left join recent r using (constructor_id)
),

costs as (
  select toUInt32(constructorId) as constructor_id, toFloat64(cost_amount) as cost_amount from raw.raw_constructor_costs
),

cost_stats as (
  select max(cost_amount) as max_cost from costs
),

with_score as (
  select
    b.*,
    least(1.0, b.avg_points_per_race / 25.0) as pts_score,
    b.recent_podium_rate as recent_score,
    coalesce(c.cost_amount, 0.0) as cost_amount,
    case when cs.max_cost > 0 then coalesce(c.cost_amount,0.0) / cs.max_cost else 0 end as normalized_cost
  from base b
  left join costs c using (constructor_id)
  cross join cost_stats cs
),

final as (
  select
    constructor_id,
    constructor_name,
    seasons_active,
    total_races,
    total_podiums,
    podium_rate,
    avg_points_per_race,
    avg_position,
    podiums_last_12,
    races_last_12,
    recent_podium_rate,
    round(normalized_cost,4) as cost_proxy_score,
    cost_amount
  from with_score
)

select * from final
