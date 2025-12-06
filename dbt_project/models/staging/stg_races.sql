{{ config(materialized='table') }}
-- Staging table for races
SELECT
  toUInt32(raceId) AS raceId,
  toUInt16(year) AS year,
  toUInt16(round) AS round,
  toUInt32(circuitId) AS circuitId,
  name,
  toDate(date) AS fecha,
  time
FROM raw.raw_races
