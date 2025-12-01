ATTACH TABLE _ UUID '6a7bec04-0b2b-4ac7-9726-83628a018295'
(
    `raceId` String,
    `driverId` String,
    `stop` String,
    `lap` String,
    `time` String,
    `duration` String,
    `milliseconds` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
