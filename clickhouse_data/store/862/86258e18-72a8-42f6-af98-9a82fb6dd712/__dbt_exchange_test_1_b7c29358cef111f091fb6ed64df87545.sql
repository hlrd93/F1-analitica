ATTACH TABLE _ UUID '4a9ef42e-2595-4eea-8dff-3b71a7721187'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
