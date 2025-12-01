{{
  config(
    materialized='table'
  )
}}

-- Constructor-level metrics to support sponsorship ROI analysis
-- Produces: constructor_id, constructor_name, seasons_active, total_races,
-- total_podiums, podium_rate, avg_points_per_race, avg_position,
-- podiums_last_12, recent_podium_rate (last 12 races), cost_proxy_score

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

-- metric looking at last N races per constructor (recent performance)
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

-- cost proxy: relative score derived from average points & recent performance.
-- This is a heuristic (higher score => more expensive); it's a relative indicator
-- not an actual monetary value.
with_score as (
  select
    b.*,
    -- normalize avg_points_per_race to a 0..1 by dividing by a reasonable cap (e.g., 25 pts max per race)
    least(1.0, b.avg_points_per_race / 25.0) as pts_score,
    b.recent_podium_rate as recent_score
  from base b
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
    -- simple proxy: weighted combination (0.6 recent, 0.4 historical points)
    round( (0.6 * recent_podium_rate) + (0.4 * least(1.0, avg_points_per_race/25.0)), 4) as cost_proxy_score
  from with_score
)

select * from final
