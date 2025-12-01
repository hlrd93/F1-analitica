ATTACH TABLE _ UUID '0733f519-126d-445f-90c1-c67eb1951d58'
(
    `raceId` String,
    `driverId` String,
    `lap` String,
    `position` String,
    `time` String,
    `milliseconds` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
