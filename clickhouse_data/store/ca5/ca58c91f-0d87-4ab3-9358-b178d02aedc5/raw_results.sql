ATTACH TABLE _ UUID '4d45c89c-1d57-419c-b283-be1597a8537c'
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
    `rank` String,
    `fastestLapTime` String,
    `fastestLapSpeed` String,
    `statusId` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
