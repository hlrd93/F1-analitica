ATTACH VIEW _ UUID 'c909b2b5-e0d7-47fc-b5aa-94d837513e6e'
(
    `raceId` UInt32,
    `year` UInt16,
    `round` UInt16,
    `circuitId` UInt32,
    `name` String,
    `fecha` Date,
    `time` String
)
AS SELECT
    toUInt32(raceId) AS raceId,
    toUInt16(year) AS year,
    toUInt16(round) AS round,
    toUInt32(circuitId) AS circuitId,
    name,
    toDate(date) AS fecha,
    time
FROM raw.raw_races
