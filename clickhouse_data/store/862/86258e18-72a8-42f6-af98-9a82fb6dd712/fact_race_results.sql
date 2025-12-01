ATTACH VIEW _ UUID 'cfebceac-ccda-4cfd-9652-278243715d86'
(
    `resultId` String,
    `raceId` UInt32,
    `driverId` String,
    `constructorId` String,
    `positionOrder` Int8,
    `points` Nullable(Float32),
    `sk_fecha` UInt32
)
AS SELECT
    r.resultId,
    toUInt32(r.raceId) AS raceId,
    r.driverId,
    r.constructorId,
    toInt8(r.positionOrder) AS positionOrder,
    toFloat32OrNull(r.points) AS points,
    toUInt32(replaceAll(toString(rc.date), '-', '')) AS sk_fecha
FROM raw.raw_results AS r
LEFT JOIN raw.raw_races AS rc ON r.raceId = rc.raceId
