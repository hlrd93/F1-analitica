ATTACH TABLE _ UUID 'ff2390b7-09c1-4493-82f4-9c9a99a43ae2'
(
    `constructorStandingsId` String,
    `raceId` String,
    `constructorId` String,
    `points` String,
    `position` String,
    `positionText` String,
    `wins` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
