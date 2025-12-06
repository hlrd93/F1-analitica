{{ config(materialized='table') }}
-- Fact table for race results
SELECT
  r.resultId,
  toUInt32(r.raceId) AS raceId,
  r.driverId,
  r.constructorId,
  toInt8(r.positionOrder) AS positionOrder,
  toFloat32OrNull(r.point) AS points,
  toUInt32(replaceAll(toString(rc.date), '-', '')) AS sk_fecha
FROM raw.raw_results AS r
LEFT JOIN raw.raw_races AS rc ON r.raceId = rc.raceId
