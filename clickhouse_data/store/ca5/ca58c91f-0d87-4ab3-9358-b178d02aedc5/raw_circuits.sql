ATTACH TABLE _ UUID 'bf77c764-2b01-45f0-8399-cae1188169ad'
(
    `circuitId` String,
    `circuitRef` String,
    `name` String,
    `location` String,
    `country` String,
    `lat` String,
    `lng` String,
    `alt` String,
    `url` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
