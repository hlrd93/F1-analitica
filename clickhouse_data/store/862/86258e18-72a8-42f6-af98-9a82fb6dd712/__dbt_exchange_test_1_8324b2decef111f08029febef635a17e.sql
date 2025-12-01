ATTACH TABLE _ UUID 'b6d1d21c-5ae8-4076-b79d-53fa0c05d945'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
