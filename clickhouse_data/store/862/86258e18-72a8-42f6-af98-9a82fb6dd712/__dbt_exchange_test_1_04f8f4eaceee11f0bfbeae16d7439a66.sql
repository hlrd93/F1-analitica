ATTACH TABLE _ UUID 'dfcb11d0-57a8-4914-b4eb-588049028a29'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
