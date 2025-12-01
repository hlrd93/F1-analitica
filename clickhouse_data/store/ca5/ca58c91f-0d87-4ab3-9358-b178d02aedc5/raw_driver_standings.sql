ATTACH TABLE _ UUID 'd1fee664-2317-4e07-bfbf-d428b299f5ba'
(
    `driverStandingsId` String,
    `raceId` String,
    `driverId` String,
    `points` String,
    `position` String,
    `positionText` String,
    `wins` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
