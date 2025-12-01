ATTACH TABLE _ UUID '1047e1ab-1e6c-474c-a18f-cf5ef9a5da04'
(
    `statusId` String,
    `status` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
