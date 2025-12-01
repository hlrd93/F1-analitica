ATTACH TABLE _ UUID '73980ccc-48de-47e1-a6ed-ee60a2a87738'
(
    `constructorResultsId` String,
    `raceId` String,
    `constructorId` String,
    `points` String,
    `status` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
