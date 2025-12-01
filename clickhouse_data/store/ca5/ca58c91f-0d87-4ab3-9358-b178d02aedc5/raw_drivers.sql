ATTACH TABLE _ UUID 'd9a564c3-b99a-4d0f-bb18-75ac1ff85da8'
(
    `driverId` String,
    `driverRef` String,
    `number` String,
    `code` String,
    `forename` String,
    `surname` String,
    `dob` String,
    `nationality` String,
    `url` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
