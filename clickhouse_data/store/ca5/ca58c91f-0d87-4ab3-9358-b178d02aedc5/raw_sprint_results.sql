ATTACH TABLE _ UUID '2361a5dd-656b-4048-a4d1-c6f89aff2903'
(
    `resultId` String,
    `raceId` String,
    `driverId` String,
    `constructorId` String,
    `number` String,
    `grid` String,
    `position` String,
    `positionText` String,
    `positionOrder` String,
    `points` String,
    `laps` String,
    `time` String,
    `milliseconds` String,
    `fastestLap` String,
    `fastestLapTime` String,
    `statusId` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
