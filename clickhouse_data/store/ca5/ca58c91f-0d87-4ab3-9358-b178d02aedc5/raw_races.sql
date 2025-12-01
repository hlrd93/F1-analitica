ATTACH TABLE _ UUID '8ce462d9-537b-4aac-8591-e6e8b52bae83'
(
    `raceId` String,
    `year` String,
    `round` String,
    `circuitId` String,
    `name` String,
    `date` String,
    `time` String,
    `url` String,
    `fp1_date` String,
    `fp1_time` String,
    `fp2_date` String,
    `fp2_time` String,
    `fp3_date` String,
    `fp3_time` String,
    `quali_date` String,
    `quali_time` String,
    `sprint_date` String,
    `sprint_time` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
