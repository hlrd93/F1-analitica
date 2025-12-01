ATTACH TABLE _ UUID '14d2fedf-d324-49ca-a83a-18d44f5d223f'
(
    `qualifyId` String,
    `raceId` String,
    `driverId` String,
    `constructorId` String,
    `number` String,
    `position` String,
    `q1` String,
    `q2` String,
    `q3` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
